// 环境配置表
const envConfig = {
    window: {
        location: { href: 'https://example.com', host: 'example.com' },
        localStorage: new Map(),
        sessionStorage: new Map(),
        navigator: { userAgent: 'Chrome/120.0.0.0' }
    },
    document: {
        cookie: '',
        referrer: '',
        title: 'Test Page'
    }
};

// 自动创建完整环境
class EnvironmentBuilder {
    constructor() {
        this.env = {};
        this.proxied = new Set();
    }

    // 自动补全对象
    build(config, path = '') {
        for (const [key, value] of Object.entries(config)) {
            const fullPath = path ? `${path}.${key}` : key;

            if (typeof value === 'object' && value !== null && !Array.isArray(value)) {
                // 创建代理对象
                this.env[key] = this.createProxy(this.build(value, fullPath), fullPath);
            } else if (typeof value === 'function') {
                this.env[key] = this.mockFunction(fullPath);
            } else {
                this.env[key] = value;
            }
        }
        return this.env;
    }

    // 创建代理
    createProxy(obj, name) {
        if (this.proxied.has(obj)) return obj;
        this.proxied.add(obj);

        return new Proxy(obj, {
            get: (target, prop) => {
                if (prop === Symbol.toPrimitive) return;
                console.log(`✅ 访问: ${name}.${String(prop)}`);

                // 自动补未定义的属性
                if (!(prop in target) && typeof prop === 'string') {
                    console.log(`⚠️ 未定义属性: ${name}.${prop}, 自动创建`);
                    target[prop] = this.autoGenerate(prop);
                }
                return target[prop];
            },
            set: (target, prop, value) => {
                console.log(`📝 设置: ${name}.${String(prop)} =`,
                    typeof value === 'function' ? '[Function]' : value);
                target[prop] = value;
                return true;
            }
        });
    }

    // 自动生成常见属性
    autoGenerate(prop) {
        const generators = {
            addEventListener: () => () => {},
            removeEventListener: () => () => {},
            getElementById: () => () => ({ innerHTML: '', style: {} }),
            querySelector: () => () => null,
            setAttribute: () => () => {},
            getAttribute: () => () => null
        };

        return generators[prop] ? generators[prop]() : {};
    }

    // 模拟函数
    mockFunction(name) {
        const fn = function(...args) {
            console.log(`🎯 调用函数: ${name}`, args);
            return undefined;
        };
        fn.toString = () => `function ${name.split('.').pop()}() { [native code] }`;
        return fn;
    }
}

// 使用
const builder = new EnvironmentBuilder();
const env = builder.build(envConfig);

// 挂载到全局
Object.assign(globalThis, env);
globalThis.window = env.window;
globalThis.document = env.document;


require("./source")


