// ==================== env_base.js（增强版） ====================

console.log('=== 加载小红书补环境模板 ===\n');

const LOG = true;
const missingProps = new Set();
const fakeWasmInstances = new Map();  // 存储假WASM实例

// ========== 创建代理（改进版） ==========
function createProxy(obj, name) {
    return new Proxy(obj, {
        get(target, prop) {
            // 避免记录访问过多的内部属性
            if (LOG && typeof prop !== 'symbol' && !prop.startsWith('_')) {
                console.log(`[GET] ${name}.${String(prop)}`);
            }

            // 重点：如果属性存在，直接返回
            if (prop in target) {
                const value = target[prop];
                // 如果值是对象且不是数组和函数，递归代理
                if (value && typeof value === 'object' && !Array.isArray(value) && !(value instanceof Function)) {
                    return createProxy(value, `${name}.${String(prop)}`);
                }
                return value;
            }

            // 属性不存在：记录缺失
            if (typeof prop !== 'symbol' && prop !== 'then' && prop !== 'inspect') {
                missingProps.add(`${name}.${String(prop)}`);
                console.log(`⚠️ 缺失: ${name}.${String(prop)}`);

                // 根据属性名返回智能默认值
                return getDefaultValue(prop);
            }

            return undefined;
        },

        set(target, prop, value) {
            if (LOG && typeof prop !== 'symbol' && !prop.startsWith('_')) {
                console.log(`[SET] ${name}.${String(prop)} =`,
                    typeof value === 'function' ? '[Function]' :
                    value && typeof value === 'object' ? '[Object]' : value);
            }
            target[prop] = value;
            return true;
        },

        // 添加 has 陷阱，解决 "in" 操作符检查
        has(target, prop) {
            const exists = prop in target;
            if (LOG && typeof prop !== 'symbol') {
                console.log(`[HAS] ${name}.${String(prop)} -> ${exists}`);
            }
            return exists;
        }
    });
}

// 智能默认值生成函数
function getDefaultValue(prop) {
    const propStr = String(prop);

    // WebAssembly 相关
    if (propStr === 'WebAssembly') {
        console.log('  🔧 返回模拟的 WebAssembly 对象');
        return createFakeWebAssembly();
    }

    // Object 对象
    if (propStr === 'Object') {
        console.log('  🔧 返回全局 Object');
        return global.Object;
    }

    // 函数类型默认值
    if (propStr.startsWith('get')) return () => null;
    if (propStr.includes('Event')) return () => ({ preventDefault: () => {}, stopPropagation: () => {} });
    if (propStr === 'addEventListener') return (event, fn) => { console.log(`[EVENT] 监听 ${event}`); };
    if (propStr === 'removeEventListener') return () => {};

    // 对象类型默认值
    if (propStr === 'prototype') return {};
    if (propStr === 'then') return undefined;  // Promise 相关

    // 默认返回空函数
    return () => {};
}

// 创建假的 WebAssembly 对象
function createFakeWebAssembly() {
    // 在 createFakeWebAssembly 函数内，替换原有的 Memory 部分
    class FakeWebAssemblyMemory {
        constructor(descriptor) {
            console.log('[WASM] new Memory() 参数:', descriptor);
            // 页大小固定为 64KB (65536 字节)
            const initial = descriptor?.initial || 1;
            const maximum = descriptor?.maximum || initial;
            this._initial = initial;
            this._maximum = maximum;
            // 创建初始大小的 ArrayBuffer
            this._buffer = new ArrayBuffer(initial * 65536);
            // 添加 buffer 属性（不可枚举，但直接赋值）
            this.buffer = this._buffer;
        }

        // grow 方法：增加指定页数，返回旧的页数
        grow(pages) {
            console.log('[WASM] Memory.grow() pages:', pages);
            const oldSize = this._buffer.byteLength / 65536;
            const newSize = oldSize + pages;
            if (newSize > this._maximum) {
                throw new Error('WebAssembly.Memory.grow: maximum size exceeded');
            }
            // 创建新的更大的 ArrayBuffer 并复制数据
            const newBuffer = new ArrayBuffer(newSize * 65536);
            const oldView = new Uint8Array(this._buffer);
            const newView = new Uint8Array(newBuffer);
            newView.set(oldView);
            this._buffer = newBuffer;
            this.buffer = this._buffer;
            return oldSize;
        }

        // 小红书可能用到的 toFixedLengthBuffer（真实浏览器有这个方法）
        toFixedLengthBuffer() {
            console.log('[WASM] Memory.toFixedLengthBuffer()');
            // 返回当前 buffer 的固定长度副本（实际实现未知，我们直接返回原buffer）
            return this._buffer;
        }

        // toResizableBuffer 同理
        toResizableBuffer() {
            console.log('[WASM] Memory.toResizableBuffer()');
            return this._buffer;
        }
    }

    // 确保 WebAssembly.Memory 的原型上有这些方法
    FakeWebAssemblyMemory.prototype.grow = FakeWebAssemblyMemory.prototype.grow;
    FakeWebAssemblyMemory.prototype.toFixedLengthBuffer = FakeWebAssemblyMemory.prototype.toFixedLengthBuffer;
    FakeWebAssemblyMemory.prototype.toResizableBuffer = FakeWebAssemblyMemory.prototype.toResizableBuffer;
    // 这个对象要模拟真实的 WebAssembly 接口
    const wasm = {
        // WebAssembly.Instance 构造函数
        Instance: function Instance(module, imports) {
            console.log('[WASM] 创建 WebAssembly.Instance');
            return {
                exports: imports?.env || {}
            };
        },
        Memory:FakeWebAssemblyMemory,
        // WebAssembly.Module 构造函数
        Module: function Module(bytes) {
            console.log('[WASM] 创建 WebAssembly.Module');
            return { bytes };
        },

        // 编译方法
        compile: async (bytes) => {
            console.log('[WASM] compile 调用');
            return new wasm.Module(bytes);
        },

        // 实例化方法
        instantiate: async (bytes, imports) => {
            console.log('[WASM] instantiate 调用');
            const module = new wasm.Module(bytes);
            const instance = new wasm.Instance(module, imports);
            return { module, instance };
        },

        // 验证字节码
        validate: (bytes) => {
            console.log('[WASM] validate 调用');
            return true;  // 假装有效
        }
    };

    // 添加 toString 方法，伪装成原生对象
    wasm.toString = () => 'function WebAssembly() { [native code] }';
    wasm.Instance.toString = () => 'function Instance() { [native code] }';
    wasm.Module.toString = () => 'function Module() { [native code] }';

    return wasm;
}

// ========== 补充基础对象 ==========

// 先补充 window.Object（解决缺失问题）
global.Object = Object;  // 确保全局Object存在

const win = {};
const window = createProxy(win, 'window');

// 重要：先把 Object 挂到 window 上
win.Object = global.Object;

// 补充 WebAssembly
win.WebAssembly = createFakeWebAssembly();

// navigator - 小红书可能检测浏览器指纹
const nav = {
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    platform: 'Win32',
    language: 'zh-CN',
    languages: ['zh-CN', 'zh', 'en'],
    cookieEnabled: true,
    hardwareConcurrency: 8,
    deviceMemory: 8,
    webdriver: false,  // 重要：反检测
    plugins: [],
    mimeTypes: [],
    maxTouchPoints: 0,
    vendor: 'Google Inc.',
    productSub: '20030107',
    product: 'Gecko',
    appName: 'Netscape',
    appVersion: '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    appCodeName: 'Mozilla',
    onLine: true
};
const navigator = createProxy(nav, 'navigator');

// location
const loc = {
    href: 'https://www.xiaohongshu.com',
    protocol: 'https:',
    host: 'www.xiaohongshu.com',
    hostname: 'www.xiaohongshu.com',
    pathname: '/',
    search: '',
    hash: '',
    origin: 'https://www.xiaohongshu.com'
};
const location = createProxy(loc, 'location');

// document
const doc = {
    cookie: '',
    referrer: '',
    title: '小红书',
    readyState: 'complete',
    documentElement: {},
    body: {},
    addEventListener: function(type, listener, options) {
        console.log(`[DOC] addEventListener 注册事件: ${type}`);
        // 小红书只是检查该方法是否存在，不需要真正实现
    },
    removeEventListener: function(type, listener) {
        console.log(`[DOC] removeEventListener 移除事件: ${type}`);
    },
    createElement: (tag) => {
        console.log(`[DOC] createElement: ${tag}`);
        return {
            style: {},
            setAttribute: () => {},
            appendChild: () => {},
            getContext: () => ({ fillRect: () => {}, fillText: () => {} }),
            toDataURL: () => 'data:image/png;base64,xxx'
        };
    },
    getElementById: (id) => {
        console.log(`[DOC] getElementById: ${id}`);
        return null;
    },
    querySelector: (sel) => {
        console.log(`[DOC] querySelector: ${sel}`);
        return null;
    },
    querySelectorAll: (sel) => {
        console.log(`[DOC] querySelectorAll: ${sel}`);
        return [];
    }
};
const document = createProxy(doc, 'document');

// ========== 常用函数 ==========
const crypto = require('crypto');

global.md5 = function(str) {
    console.log(`[MD5] 计算长度: ${str?.length}`);
    return crypto.createHash('md5').update(String(str)).digest('hex');
};

global.btoa = function(str) {
    return Buffer.from(String(str)).toString('base64');
};

global.atob = function(str) {
    return Buffer.from(str, 'base64').toString();
};

// 添加 setTimeout/setInterval
global.setTimeout = function(fn, time) {
    return setTimeout(fn, time);
};
global.setInterval = function(fn, time) {
    return setInterval(fn, time);
};

// ========== 挂载到全局 ==========
global.window = window;
global.navigator = navigator;
global.location = location;
global.document = document;

// 让 window 指向自身
window.window = window;
window.self = window;
window.top = window;
window.parent = window;
window.global = global;
window.navigator = navigator;
window.location = location;
window.document = document;
window.console = console;

// 确保 window.Object 存在
window.Object = Object;


// 模拟小红书 insight 监控对象
window.insight = {
    // 基础属性（从浏览器复制）
    sessionId: '6bc91435-84a5-438c-be77-57d42981d426',
    version: '1.3.12',
    queue: [],
    options: {
        jsError: {},
        http: {},
        blankScreen: {},
        debug: false,
        beforeSend: function() {}
    },
    isReady: false,

    // 关键方法（空实现或简单日志）
    getBaseDeviceInfo: function() {
        console.log('[INSIGHT] getBaseDeviceInfo 被调用');
        return undefined;
    },
    report: function(e, a) {
        console.log('[INSIGHT] report 被调用', e, a);
        if (!this.isReady) {
            this.queue.push(e);
        }
    },
    push: function(e, a) {
        console.log('[INSIGHT] push 被调用', e, a);
        if (a === 'ApmJSONTracker') {
            this.sendApm(e.value, e.type);
        } else {
            this.report(e);
        }
    },
    config: function(e, a, s) {
        console.log('[INSIGHT] config 被调用', e, a, s);
    },
    init: function(e) {
        console.log('[INSIGHT] init 被调用', e);
        this.isReady = true;
    },
    setKeyResource: function(e) {
        console.log('[INSIGHT] setKeyResource 被调用', e);
    },
    extend: function(e, a) {
        console.log('[INSIGHT] extend 被调用', e, a);
    },
    flush: function(e) {
        console.log('[INSIGHT] flush 被调用', e);
    },
    destroy: function() {
        console.log('[INSIGHT] destroy 被调用');
    },
    setCustomDimensions: function(e) {
        console.log('[INSIGHT] setCustomDimensions 被调用', e);
        if (typeof e === 'function') {
            e({}).then(() => {});
        }
    },
    updateMeta: function(e) {
        console.log('[INSIGHT] updateMeta 被调用', e);
    },
    sendApm: function(e, a) {
        console.log('[INSIGHT] sendApm 被调用', e, a);
        var s = {};
        s[a] = { type: a, value: e };
        var u = { type: 'FrontApmTracker', value: s };
        this.push(u);
    },
    sendCustomPoint: function(e) {
        console.log('[INSIGHT] sendCustomPoint 被调用', e);
        this.report(e);
    },
    // 原型上的其他方法（以防万一）
    innerFlush: function() { console.log('[INSIGHT] innerFlush'); },
    sendCustomError: function(e) { console.log('[INSIGHT] sendCustomError', e); },
    checkBlankScreenError: function() { console.log('[INSIGHT] checkBlankScreenError'); },
    reportBlocked: function() { console.log('[INSIGHT] reportBlocked'); },
    run: function() { console.log('[INSIGHT] run'); },
    initForQiankunSubApp: function() { console.log('[INSIGHT] initForQiankunSubApp'); }
};

window._66062487cf103622475a2f9b17d8293e = 'mns0201';

console.log('\n✅ 基础环境加载完成');
console.log(`📊 当前 window 上的属性数量: ${Object.keys(window).length}\n`);