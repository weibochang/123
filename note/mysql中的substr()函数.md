---
title: mysql中的substr()函数
tags: 挫折才是成功的试金石
notebook: 数据库
---
1. 用法：
substr(string,start,end);
1) string 表示 字符串
2) start 表示 起始位置
3) end 表示 结束位置
2. mysql中的start的起始位置是从1开始的，而hibernate中的start是从0开始的

3. 创表语句
```sql
create table student(
    id int auto_increment,
    name varchar(25) not null,
    gender int not null default 1,
    age int not null,
    idcard varchar(50) not null,
    PRIMARY KEY(id)
);
```
4. 创建好的表
![选区_016](https://i.loli.net/2018/09/27/5bac2c46d98c8.png)
5. 查询语句
```sql
#1.使用substr()查询时，不能以0开始，查出的结果为Null
select * from student where substr(idcard,0,5) >= 11111;
#2.使用时，起始值要从1开始
select * from student where substr(idcard,1,4) >= 1111;
#3.这一种写法也可以
select * from student where substring(idcard,1,6) >= 123456;
```

