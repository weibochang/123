---
title: python中format函数
tags: python中format函数的简单的使用
notebook: python常识
---
---内容开始---
python中format函数用于字符串的格式化

1. 通过关键字
```python
print('{名字}今天{动作}'.format(名字='陈某某',动作='拍视频'))#通过关键字
grade = {'name' : '陈某某', 'fenshu': '59'}
print('{name}电工考了{fenshu}'.format(**grade))#通过关键字，可用字典当关键字传入值时，在字典前加**即可

```
2. 通过位置
```python
print('{1}今天{0}'.format('拍视频','陈某某'))#通过位置(用的是下标取值的方式)
print('{0}今天{1}'.format('陈某某','拍视频'))
```
3. 填充和对齐
^, <, > 分别是居中、左对齐、右对齐，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。 
```python
print('{:^14}'.format('陈某某'))
print('{:>14}'.format('陈某某'))
print('{:<14}'.format('陈某某'))
print('{:*<14}'.format('陈某某'))
print('{:&>14}'.format('陈某某'))
print('{:=^20}'.format('hello world'))#填充和对齐^<>分别表示居中、左对齐、右对齐，:后面带的是要填充的字符，只能是一个字符，不指定则默认使用 空格 来填充
```
![选区_008](https://i.loli.net/2018/09/18/5ba0d6904d072.png)
4. 精度和类型f通常一起使用
```python
print('{:.1f}'.format(4.234324525254)) #保留一位小数
print('{:.4f}'.format(4.1)) #保留四位小数，不够的用0补齐
```
5. 进制的转化，b o d x 分别表示二、八、十、十六进制
```python
print('{:b}'.format(250))  #二进制
print('{:o}'.format(250))  #八进制
print('{:d}'.format(250))  #十进制
print('{:x}'.format(250))  #十六进制
```
6. 千分位分隔符，这种情况只针对数字
```python
print('{:,}'.format(100000000))
print('{:,}'.format(235445.234235))
```




