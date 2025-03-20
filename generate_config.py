import json
from pathlib import Path
from .core.game.conf import conf
import inspect
from js2py.pyjs import PyJsObject, JsObjectWrapper

# PyJsObject转换函数
def convert_js_to_python(obj):
    if isinstance(obj, JsObjectWrapper):
        return convert_js_to_python(obj.object)
    
    if isinstance(obj, (PyJsObject, dict)):
        return {k: convert_js_to_python(v) for k, v in obj.items()
                if not k.startswith('__') and not callable(v)}
    
    if hasattr(obj, '__dict__'):
        return {k: convert_js_to_python(v) for k, v in vars(obj).items()
                if not k.startswith('__') and not callable(v)}
    
    if isinstance(obj, list):
        return [convert_js_to_python(i) for i in obj]
    
    if isinstance(obj, (int, float, str, bool)) or obj is None:
        return obj

# 构建配置数据
def collect_config_methods(obj):
    config = {}
    for attr in dir(obj):
        if attr.startswith('__'):
            continue
        try:
            member = getattr(obj, attr)
            if callable(member):
                # 调用无参方法获取结果
                if not inspect.ismethod(member) or not member.__self__:
                    continue
                result = member()
                config[attr] = convert_js_to_python(result)
            else:
                config[attr] = convert_js_to_python(member)
        except Exception as e:
            print(f"处理属性{attr}时出错: {str(e)}")
    return config

# 递归收集所有配置方法
def collect_all_configs(obj):
    config = {}
    for attr in dir(obj):
        if attr.startswith('__'):
            continue
        try:
            member = getattr(obj, attr)
            if callable(member):
                # 带参数方法的特殊处理
                if 'LevelUpTime' in attr:
                    config[attr] = convert_js_to_python(member(1))
                else:
                    config[attr] = convert_js_to_python(member())
            else:
                config[attr] = convert_js_to_python(member)
        except Exception as e:
            print(f"处理属性{attr}时出错: {str(e)}")
    return config

config_data = collect_all_configs(conf.K)

# 获取配置文件路径
config_path = Path(__file__).parent / "config.json"

# 序列化并保存配置
with open(config_path, 'w', encoding='utf-8') as f:
    json.dump(config_data, f, ensure_ascii=False, indent=2)

print(f"配置文件已生成至：{config_path}")