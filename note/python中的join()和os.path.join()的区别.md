---
title: python中的join()和os.path.join()的区别
tags: 
notebook: python常识
---
1. python中的join()函数，用于对字符串，元祖，列表，字典里的内容进行分割
```python
a = '哈哈哈哈哈哈哈哈哈哈哈哈'
b = {'a':1,'b':2,'c':3}
c = ('a','b','c','d')  #可以对元祖里的内容进行拼接，但是如果元祖里的内容是int类型，不能进行拼接
d = ['aaa','bbb','ccc']  #列表跟元祖一样，里面内容是数字的时候，都不能进行拼接

a = '-'.join(a)  #表示使用'-',把 a 中的字符进行分割
print(a)
b = '+'.join(b)
print(b)
c = '~'.join(c)
print(c)
d = '='.join(d)
print(d)
```
![选区_009](https://i.loli.net/2018/09/19/5ba210706097a.png)

2. os.path.join() 用于路径的拼接
```python
import os
print('{:=^20}'.format(''))
#os.path.join(path1,path2,...)的用法
#1.会从最后一个'/'开头的参数开始拼接，之前的参数全部丢弃，如下面的 3
#2.优先判定上一种情况，若没有的话，则查找以 './' 开头的参数，会从 './' 开头的参数的上一个参数开始拼接
print('1:',os.path.join('aaaa','bb','/abc'))
print('2:',os.path.join('aaa','./bb','bc'))
print('3:',os.path.join('/aaa','/bbb','/ccc'))
print('4:',os.path.join('aaa','/bbb','./abc'))
```
![选区_010](https://i.loli.net/2018/09/19/5ba2106247635.png)

