---
title: python的django框架中的POST和GET的一些认知，和使用是用到的问题(已解决)
tags: POST['']和POST.get('')的异同点，和使用方法的不同
notebook: python-web后端
---
#### 逻辑：通过前端表单传到后端的内容，然后进行下一步的操作


#### 1. 创建视图
1. 用于显示表单内容
```python
def gpcon(request):
    return render(request,'gp.html')
```
2. 后端接收前段传过来的值，并进行一些操作
```python
def gp(request):
    # a = request.GET['name'] 
    ##使用这种方式取值的使用，前端如果没有这个值就报错
    # b = request.GET.get('ame','这里没有你要找的那个值')
    ##用这种方式获取前端的值的时候，如果取不到对应的值的时候，不会报错，在没有默认值的情况下，会返回一个None，有默认值的话就返回默认值
    
    # c = request.GET.getlist('name') 
    ## 使用getlist()的方法的时候，返回的是一个列表，会把前端对应的所有的name的值进行匹配，一列表的形式返回
    # print(c)
    # # c = set(c)
    # print(c)
    # print(len(c))

    ############下面是post方法的一些内容
    aa = request.POST['name']  
    ##用post方法时前端的name值不能相同，否则post方法会取到后面的那个值，前面的值不会被取到的
    aa = request.POST.get('nam','POST.get()使用默认值也是好使的') 
    ##和get方法一样，上面的如果取不到值的时候，会报错，但是用get()方法后，就不会了，有个返回值None，依旧可以使用默认值
    aa = request.POST.getlist('name')  #使用POST.getlist()方法后会把对应的的name的值的内容一list的形式显示出来的，
    ########### so 可以使用这种方式进行 完成确认密码的要求(通过前端两个相同的name值取到所有的内容，使用python的set()方法去重之后，通过list的长度就可以判断两次输入的是否是一样的了)
    print(type(aa))
    print(len(aa))

    print(type(aa))
    return HttpResponse(aa)

    ################ 小总结 ###############
    # GET/POST ['前端的表单的value的值'] 
    ### 会从前端的表单中取值过来，但是如果索取的的内容不存在的情况下就会报错

    # request.GET/POST.get('前端表单中的value值','可以有一个默认值') 
    ### 会从前段取值，但是如果前端的这个值不存在或者是没有传过来都不会报错，而是显示一个None，并且get可以给一个默认值，就是前端的内容不存在的时候会使用的值

    #request.GET/POST.getlist('name值')
    ### 返回前端对应的内容的list，GET和POST通用

```

#### 2. 配置urls
```python
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^gp/',views.gp),
    url(r'^gpcon/',views.gpcon)
]
```
#### 3. 创建html文件
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>这是get和GET的展示</title>
</head>
<body>
{#<a href="/gp/" methods="get">这里是get</a>#}
<form action="/gp/" method="post">
    {% csrf_token %}
    请输入姓名：<input type="text" name="name">
    请输入你的姓名：<input type="text" name="name">
    请输入年龄：<input type="text" name="sex">
    <input type="submit" value="提交">
</form>

</body>
</html>
```


