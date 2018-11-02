---
title: python闭包
tags: 过了很久终于我愿抬头看，原来当初学的狗屁的不是
notebook: python常识
---

### 要学习闭包，就必须想知道这些
<center><font color=red size=4>函数调用 与 函数引用</font></center>
一段示例代码：

```python {.line-numbers}
def func():
    print('这是一个函数')
# 函数调用
func()
# 函数引用
ret = func
print(id(func))
print(id(ret))
print('++++++++++++++++++++++++++++')
#升级版的
def func(num):
    print('这是一个函数，num的值是：{}'.format(num))
# 函数的调用
func(521)
# 函数的引用
ret = func  # 这里 ret 是 func 函数的一个引用，并不会执行这个函数
ret(777)  # 这时候，用ret这个func函数的引用来传参调用这个函数，这一步才会执行

```


![选区_011](https://i.loli.net/2018/09/24/5ba8664cb6a71.png)
1. 函数的调用
函数的调用是直接使用   <font color=red size=3>函数名(参数)</font>  进行函数的调用
2. 函数的函数的引用
<font color=red size=3>函数的一个引用，并不会执行这个函数，这是对这个函数的引用，在以后用到的时候，可以使用这个应用的值进行调用</font>

##闭包
```python {.line-numbers}

def test(number): 
    print('外部函数')
    #在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，
    #那么将这个函数以及用到的一些变量称之为闭包 
    def test_in(number_in): 
        print("in test_in 函数, number_in is %d"%number_in) 
        return number+number_in 
    print('我在内部函数下面呢！！！') 
    return test_in # !!!  这里是的返回值是 内部函数 test_in 的引用，下面可以用 外部函数的变量传参调用内部函数
a = test(111)
print(a(5))

```


