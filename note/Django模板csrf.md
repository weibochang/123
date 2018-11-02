---
title: Django模板
tags: 2
notebook: python-web后端
---
1. CSRF
    1. 全称Cross Site Request Forgery，跨站请求伪造
    2. 某些恶意网站上包含链接、表单按钮或者JavaScript，它们会利用登录过的用户在浏览器中的认证信息试图在你的网站上完成某些操作，这就是跨站攻击
    3. 演示csrf如下
    4. 创建视图csrf1用于展示表单，csrf2用于接收post请求

#一般出现403错误的时候，表示跨站请求的问题
###解决方案：

    1. 注释掉settings中的，'django.middleware.scrf.CsrfViewMiddleware'（这是是关闭了跨站请求的服务，进行跨站请求时，不会在次做验证）
    2. 打开settings中的注释，在html表单中，加入如下代码：
```
    <form>
{% csrf_token %}
...
</form>
```
#取消csrf保护
+ 如果某些视图不需要保护，可以使用装饰器csrf_exempt，模板中也不需要写标签，修改csrf2的视图如下
```
....
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def csrf2(request):
    uname = request.POST['uname']
    return render(request, 'csrf2.html', {'uname': uname})
```
#保护原理
+ 加入标签,可以查看源代码,发现多了如下代码
    <input type='hidden' name='csrfmiddlewaretoken' value='nGjAB3Md9ZSb4NmG1sXDolPmh3bR2g59' />
###其实，CSRF并不是完全安全的，例如在本地文档中加入，自动加入的代码<input type='hidden' name='csrfmiddlewaretoken' value='nGjAB3Md9ZSb4NmG1sXDolPmh3bR2g59' />
