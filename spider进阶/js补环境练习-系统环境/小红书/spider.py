import subprocess
import json
import re


class JSEnvironment:
    def __init__(self, js_code_path):
        self.js_code_path = js_code_path

    def execute_js(self, func_name=None, args=None):
        """
        在补环境中执行JS代码
        """
        # 构建执行脚本
        exec_script = f'''
        const fs = require('fs');

        // 加载补环境
        require('./js_env/env_base.js');

        // 加载目标代码
        const targetCode = require('{self.js_code_path}');

        // 执行并返回结果
        let result;
        try {{
            if ({func_name}) {{
                result = window[{func_name}]({json.dumps(args) if args else ''});
            }} else if (typeof targetCode === 'function') {{
                result = targetCode();
            }}
            console.log(JSON.stringify({{status: 'success', data: result}}));
        }} catch(e) {{
            console.log(JSON.stringify({{status: 'error', message: e.message, stack: e.stack}}));
        }}
        '''

        # 写入临时文件
        temp_file = 'temp_run.js'
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(exec_script)

        # 执行
        result = subprocess.run(
            ['node', temp_file],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )

        # 解析输出
        for line in result.stdout.split('\n'):
            if line.startswith('{') and line.endswith('}'):
                return json.loads(line)

        return {'status': 'error', 'message': 'No valid output'}

    def get_missing_props(self):
        """获取缺失的环境属性"""
        # 运行并收集缺失属性
        exec_script = '''
        require('./js_env/env_base.js');
        console.log('收集完成');
        '''
        # ... 执行逻辑
        pass


# 使用示例
env = JSEnvironment('target_js/xhs_crypto.js')
result = env.execute_js('encrypt_func', {'input': 'hello'})
print(result)