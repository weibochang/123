---
title: django中发送邮件的配置
tags: 
notebook: python-web后端
---
### python的django框架中内置了发送邮件的功能

###1. 首先注册163邮箱,登录后设置
1) 进入设置中
![选区_015](https://i.loli.net/2018/09/24/5ba865caf19cb.png)
2)在新页面中点击“客户端授权密码”，勾选“开启”，弹出新窗口填写手机验证码
![123](https://i.loli.net/2018/09/24/5ba8666ccbb5e.png)
3)设置自己的授权码
4)设置完成之后，会提示开启成功（要记下来自己的授权码，以后配置django的时候要用到的）

###2. 创建一个django的项目(工程)
1）打开项目的settings.py文件，进行 类似如下的配置：
```python
# 这个是django内置的发送邮件的模块
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# stmp服务器的地址，（不同的邮箱的email_host是不同的）
EMAIL_HOST = 'smtp.163.com'
# stmp服务器的端口号
EMAIL_PORT = 25
#用来发送邮件的邮箱
EMAIL_HOST_USER = 'django_eamil_test@163.com'
#在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'wwy123456789'
#收件人看到的发件人(前面的名称可以不一样，但是后面的<django_eamil_test@163.com>，这个必须和上面的 发送邮件的地址是一样的)
EMAIL_FROM = 'python<django_eamil_test@163.com>'
```
2）在自己的应用下创建一个视图，用来发送邮件
```python
from django.conf import settings  #导入settings的内容
from django.core.mail import send_mail #导入django中定义好的发送邮件的函数
from django.http import HttpResponse
...
def send(request):
    # 自己定义的内容，发送邮件的内容可以是 文本或者是html，
    # (但是 文本和html不同同时存在，当一起存在的时候，html会优先显示)
    msg='<a href="#" target="_blank">点击激活</a>' 
    # django中定义好的发送邮件的函数，可以从上面导入的send_mail中查看包含的字段
    #send_mail(subject(邮件的标题), message(发送的文本内容), from_email(发件人的看到的收件人，在settings中有配置), recipient_list(要接收此邮件的人的邮箱，这里是用一个列表表示),fail_silently=False, auth_user=None, auth_password=None,connection=None, html_message=None(这里是html文本)):
    send_mail('注册激活','',settings.EMAIL_FROM,
              ['django_eamil_test@163.com'],
              html_message=msg)
    return HttpResponse('ok')

```
3）配置urls.py 中的路由
4）启动服务器，输入对应的网址即可，显示成功后，可以登录到邮箱查看发送的邮件