#!/usr/bin/python
# -*- coding:UTF-8 -*-

s = "hello world "

# print s
# print s[0]
# print s[2:5]
# print s[2:]
# print s*2

# print s+"rokcy"

# 列表

list_a = ["str", 1, ["a", "b", "c"], 4]
list_b = ["var"]
# print list_a[0]
# print list_a[1:3]
# print list_b*2
# print list_a+list_b

# 浅拷贝

list_c=list_a
# print list_c
list_a[0]="strs"
# print list_c

# 表层拷贝
list_d=list_a[:]
list_a[0]="strs"
# print list_d

list_a[2][1]="d"
# print list_d

# 深拷贝

import copy

list_e=copy.deepcopy(list_a)

list_a[0]="strs"
list_a[2][1]="d"

# print list_e


# print len(list_a)
list_a.append("Candy")
list_a.insert(0, "Hello")
list_a.pop()

# 元组
# 不可改变的列表
tuple_a = ("str", 1, ["a", "b", "c"], 4)
tuple_b = ("var",)

# print tuple_a[0]
# print tuple_a[1:3]
# print tuple_b * 2
# print tuple_a+tuple_b

# 字典

person_a = {
    "name": "rocky",
    "age": 24,
    1: "level_1"
}

# print person_a["name"]
# print person_a["age"]
# print person_a[1]
#
# print "rocky" in person_a
# print "xxx" in person_a
#
# print person_a.keys()
# print person_a.values()
# print person_a.items()


# 第一个参数是dict的key值 第二个是找不到这个key值所对应的输入值
# print person_a.get(1,"failed")

person_a["address"] = "China"
person_a.pop("address")

# for  key in count:
#     print key,count[key]
# for key,value in count.items():
#     print key,value
# for key,value in count.iteritems():
#     print key,value
# for key,value in zip(count.iterkeys(),count.itervalues()):
#     print key,value

# s='abcdefghijk'
# for (index,char) in enumerate(s):
#     print index
#     print char


# Set

set_a = set(['luck', 'lily'])
set_b = set(['luck', 'linxiao'])
# print set_a & set_b 交
# print set_a | set_b 并

set_a.remove('luck')
set_a.add('lucky')

# print set_a


# 运算符

# 算术运算符
# +-*/% ...
# a=2
# b=2
# print a**b # 幂运算

# 比较运算符
# !=  ==  <>  > < <= >=

# == 比较值的运算符
# is 比较对象

# 逻辑运算符
# and or not

# for a in list_a:
# if type(a) ==list : #type()  判断一个变量是否为某个数据类型
#     for a_b in a:
#         print a_b
# else:
#     print a


# 函数

# 无参数
# 有参数
# 不定长参数
# 参数次序可变

# def print_hello(s=3,*args):
# def print_hello(s,args):
#     print "hello"
#     print s
#     for a in args:
#         print a
#     return s*2


# print_hello(1,4)
# print_hello(1)
# print print_hello(2)

# 匿名函数
# func=lambda x,y :x+y
# print func(1,2)

# 类

# class human(object):
#     def __init__(self,name):
#         # self.name=name
#         self.__name=name
#     def hello(self):
#         self.name="name1"
#     def get_name(self):
#         return self.__name
#     def set_name(self,name):
#         self.__name=name
#
# if __name__ == '__main__':
#     human_a=human("number")
# human_a.name="number1"
# human_a.hello();

# human_a.set_name("setNumber")
# print human_a.get_name()
# print human_a.name

# 多态

# class Human(object):
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#
# class Man(Human):
#     #初始化Human的构造函数
#     def __init__(self,name,age,has_wife):
#         super(Man, self).__init__(name,age)
#         self.__has_wife=has_wife

# 模块

# 如果在不同的路径下要使用sys
# import sys
# sys.path.append('')


# 调用包下的模块
# 只要用sys.path.append('')加载这个包
# 每个包下都有__init__.py __init__pyc
# from 包 import *(要使用的模块)


# import module
# from module import print_hello
# module.print_hello(1,2,3)
# print_hello(1,2,3)


# 字符串
# str="abcabc"
# print str.find("c")
# print str.split("b")
#
# print str[0].upper()+str[1:]
# print str.lower()
# print str[::-1]

# 文件
# a 追加写 b 二进制用于图片
# f=open("hello","arw+")
# content=f.read()
# f.close()
# print content


# 如果文件比内存大的话
# while True:
#     lines= f.readlines(10240)
#     if not lines:
#         break
#     for line in lines:
#         print line.strip()

# f.close()

# 0-100的总和

# sum=0
# for i in range(0,101):
#     sum += i
# print sum

# 1-100的质数

# for i in range(3,100):
#     sum=0
#     j=1
#     while j <= i:
#         if i%j==0:
#             sum +=1
#         j +=1
#     if sum == 2:
#         print i

# def judge(x):
#     for  i in range(2,x):
#         if x % i==0:
#             return False
#     return True

# for i in range(2,101):
#     if judge(i):
#         print i


# 文件单词计数

# f=open("hello","arw+")
# lines=f.readlines()
# count={}

# for line in lines:
#     words=line.strip().split();
#     for word in words:
#         if word not in count:
#             count[word]=0
#         count[word] +=1

# for  key in count:
#     print key,count[key]
# f.close()









