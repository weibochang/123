---
title: python中的turtle绘图(海龟绘图)
tags: 海龟绘图
notebook: python常识
---

python中的turtle绘图是一款简单的绘图工具，又叫做 海龟绘图,想象一个小乌龟，在一个横轴为x、纵轴为y的坐标系原点，(0,0)位置开始，它根据一组函数指令的控制，在这个平面坐标系中移动，从而在它爬行的路径上绘制了图形。

###turtle绘图的基础知识
1. 画布
画布就是turtle为我们展开用于绘图区域，我们可以设置它的大小和初始位置。
如：turtle.screensize(800,600, "green")
turtle.screensize() #返回默认大小(400, 300)
<br>
turtle.setup(width=0.5, height=0.75,startx=None, starty=None)，参数：width, height: 输入宽和高为整数时, 表示像素; 为小数时, 表示占据电脑屏幕的比例，(startx, starty): 这一坐标表示矩形窗口左上角顶点的位置, 如果为空,则窗口位于屏幕中心。
如：turtle.setup(width=0.6,height=0.6)
 turtle.setup(width=800,height=800, startx=100, starty=100)

2. 绘图命令：
(1) 画笔运动命令
原址>https://blog.csdn.net/zengxiantao1994/article/details/76588580原址
|---|---|
| turtle.forward(distance) | 向当前画笔方向移动distance像素长度 |