---
title: jQuery的$('selector').empty()方法
tags: 
notebook: jQuery知识
---
jQuery中的empty()方法
####定义和用法
<font color=red size=4>empty() 方法从被选元素所有子节点和内容</font>

**注意：** 该方法不会移除元素本身，或它的属性。

**提示：** 如需移除元素，但保留数据和事件，请使用 detach() 方法。

**提示：** 如需移除元素及它的数据和事件，请使用 remove() 方法。

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
            $('#btn').click(function(){
                $('#con').empty();
            });
        });
    </script>
</head>
<body>
    <div id="con" style="height: 100px;width: 100px;background-color: yellowgreen">这里是div块中的内容<p>123</p></div>
    <button id="btn">移除div块中的内容</button>
</body>
</html>
```

