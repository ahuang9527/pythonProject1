// ==================== run.js ====================
console.log('=== 小红书加密补环境调试 ===\n');

// 加载补环境模板
require('./js_env/env_base.js');

// 加载目标加密JS
console.log('加载目标加密文件 xhs_crypto.js...');
try {
    require('./target_js/xhs_crypto.js');
    console.log('✅ 文件加载完成\n');
} catch(e) {
    console.error('❌ 加载失败:', e.message);
    console.error(e.stack);
    process.exit(1);
}

// 你的测试参数
const u = "/api/redcaptcha/v2/getconfig{}";
const m = "701d7db129f79737abc1c57cc97e69da";
const w = "040a1d360bddd5d9c6fe7097ff1437e0";

console.log('=== 开始测试 window.mnsv2 ===\n');



// 检查 mnsv2 函数
console.log('1. 检查 window.mnsv2 类型:', typeof window.mnsv2);
console.log('2. 检查 window.mnsv2 是否可调用:', typeof window.mnsv2 === 'function');

if (typeof window.mnsv2 === 'function') {
    console.log('\n3. 开始调用 window.mnsv2...');
    console.log(`   参数1(u): ${u}`);
    console.log(`   参数2(m): ${m}`);
    console.log(`   参数3(w): ${w}\n`);

    try {
        const startTime = Date.now();
        const sign = window.mnsv2(u, m, w);
        const endTime = Date.now();

        console.log(`\n📤 加密结果: ${sign}`);
        console.log(`⏱️ 耗时: ${endTime - startTime}ms`);

        if (sign && sign.length > 0) {
            console.log('\n✅ 成功获取到签名！');
        } else {
            console.log('\n⚠️ 签名结果是空/undefined，可能还需要补充环境');
        }
    } catch(e) {
        console.log('\n❌ 调用出错:', e.message);
        console.log('错误堆栈:', e.stack);
    }
} else {
    console.log('\n❌ window.mnsv2 不存在！');
    console.log('\n当前 window 上的函数:');
    const funcs = Object.keys(window).filter(k => typeof window[k] === 'function');
    console.log(funcs.slice(0, 30));  // 只显示前30个
}


