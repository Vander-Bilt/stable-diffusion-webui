# User Info Middleware Extension

这个扩展为Stable Diffusion WebUI添加了一个中间件，用于获取用户的浏览器语言设置。

## 功能

- 获取用户的浏览器语言设置并存储在`shared.user_language`中
- 优化的中间件只在首次请求时获取用户语言，减少资源消耗
- 提供重置功能，允许手动刷新用户语言信息

## 使用方法

安装此扩展后，您可以在任何脚本中通过以下方式访问用户信息：

```python
from modules import shared

# 获取用户浏览器语言
user_language = shared.user_language

# 如果需要重置用户语言
from scripts.user_info_middleware import reset_user_language
reset_user_language()
```

在`webui()`函数中，您可以通过相同的方式访问这些信息。

用户语言只会在首次HTTP请求时获取，并保存在全局变量中，直到手动重置或重启WebUI。

## 包含的示例

**webui_example.py**: 演示如何在webui()函数中访问和使用用户信息

## 注意事项

- 浏览器语言设置取决于用户的浏览器配置