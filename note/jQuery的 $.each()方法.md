---
title: jQuery的 $.each()方法
tags: 
notebook: jQuery知识
---

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="https://cdn.bootcss.com/jquery/1.10.2/jquery.min.js"></script>
    <script>
        $(function(){
            var list=['a','b','c','d']
            var dic={'a':'aaa','b':'bbb','c':'ccc'}
            var tuple=('q','w','e','r')
            $.each(list,function (index,info) {
                alert('这里是内容：'+info+','+'这里是下标: '+index)
            
            })
                // 如果前面传入的是 一个列表，后面的index就是返回的下标，info是返回的列表中的内容
                //  若果前面传入的是一个字典，后面的index就是字典对应的值，info就是字典的value
                //  前面不能传入元祖
                // 前面可以传入对象，返回的index是下标，info是对象的内容
        })
    </script>
</head>
<body>
    
</body>
</html>

```
