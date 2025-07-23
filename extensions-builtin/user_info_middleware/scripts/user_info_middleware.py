import os
from fastapi import Request
from modules import script_callbacks, shared

# 创建全局变量来存储用户浏览器语言
if not hasattr(shared, 'user_language'):
    shared.user_language = None

# 创建中间件来获取用户浏览器语言，但只获取一次
async def user_info_middleware(request: Request, call_next):
    # 只有当用户语言为空时才获取
    print("=======  languaage =======")
    if shared.user_language is None:
        print("=======  获取用户浏览器语言....... =======")
        # 获取用户浏览器语言
        accept_language = request.headers.get('accept-language')
        print(f"=======  accept_language: {accept_language} =======")
        if accept_language:
            # 解析Accept-Language头，获取首选语言
            languages = accept_language.split(',') if accept_language else []
            if languages:
                # 提取首选语言代码（例如：zh-CN;q=0.9 -> zh-CN）
                primary_language = languages[0].split(';')[0].strip()
                shared.user_language = primary_language
    
    # 继续处理请求
    response = await call_next(request)
    return response

# 提供重置用户语言的函数，可以在需要时调用
def reset_user_language():
    shared.user_language = None
    print("User language has been reset.")

# 在应用启动时添加中间件
def on_app_started(_, app):
    # 添加自定义中间件
    app.middleware('http')(user_info_middleware)
    print("User info middleware installed successfully.")

# 注册回调函数
script_callbacks.on_app_started(on_app_started)