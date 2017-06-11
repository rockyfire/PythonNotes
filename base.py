#!/usr/bin/python
# -*- coding:UTF-8 -*-

s = "hello world "

# print s
# print s[0]
# print s[2:5]
# print s[2:]
# print s*2

# print s+"rokcy"
# print "**************"

# 列表

list_a = ["str", 1, ["a", "b", "c"], 4]
list_b = ["var"]
# print list_a[0]
# print list_a[1:3]
# print list_b*2
# print list_a+list_b


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
# print  "************************"
# print person_a["name"]
# print person_a["age"]
# print person_a[1]
#
# print "rocky" in person_a
# print "xxx" in person_a
#
# print person_a.keys()
# print person_a.values()

# 第一个参数是dict的key值 第二个是找不到这个key值所对应的输入值
# print person_a.get(1,"failed")

person_a["address"] = "China"
person_a.pop("address")

# print person_a.items()


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
# def print_hello(s=3,*args):
# def print_hello(s,args):
#     print "hello"
#     print s
#     for a in args:
#         print a
#     return s*2


# 无参数
# 有参数
# 不定长参数
# 参数次序可变

# print_hello(1,4)
# print_hello(1)
# print print_hello(2)


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
#
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
# a 追加写
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
# f.writelines(['abcdefg','123456789'])
# f.close()


# sum=0
# for i in range(0,101):
#     sum += i
# print sum

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
# for key,value in count.items():
#     print key,value
# for key,value in count.iteritems():
#     print key,value
# for key,value in zip(count.iterkeys(),count.itervalues()):
#     print key,value
# f.close()


# 队列和戰



# class Queue(object):
# class Stack(object):
#     def __init__(self):
#         self.data_list=[]
#
#     def insert(self,data):
#         self.data_list.append(data)
#
#     def pop(self):
#         if len(self.data_list)==0:
#             return None
        # data=self.data_list[0]
        # data=self.data_list[-1]
        # del self.data_list[-1]
        # del self.data_list[0]

        # return data

    # def size(self):
    #     return len(self.data_list)

# queue = Queue()
# stack = Stack()
# print stack.size()
# stack.insert(1)
# stack.insert(2)
# stack.insert(3)
# head = stack.pop()
# print head
# head = stack.pop()
# print head
# head = stack.pop()
# print head
# head = stack.pop()
# print head


class Node(object):
    def __init__(self,index):
        self.index=index
        self.left_child=None
        self.right_child=None

class BinaryTree(object):
    def __init__(self,root):
        self.root=root

    def pre_travel(self,node):
        if not node:
            return
        print node.index
        self.pre_travel(node.left_child)
        self.pre_travel(node.right_child)

    def cen_travel(self,node):
        if not node:
            return
        self.cen_travel(node.left_child)
        print node.index
        self.cen_travel(node.right_child)
    def next_travel(self,node):
        if not node:
            return
        self.next_travel(node.left_child)
        self.next_travel(node.right_child)
        print node.index

node_dict={}
for i in range(1,12):
    node_dict[i]=Node(i)
node_dict[1].left_child = node_dict[2]
node_dict[1].right_child = node_dict[3]
node_dict[2].left_child = node_dict[5]
node_dict[2].right_child = node_dict[6]
node_dict[6].left_child = node_dict[10]
node_dict[6].right_child = node_dict[11]
node_dict[3].left_child = node_dict[7]
node_dict[7].left_child = node_dict[8]
node_dict[7].right_child = node_dict[9]


tree=BinaryTree(node_dict[1])
# tree.pre_travel(tree.root)
# tree.cen_travel(tree.root)
# tree.next_travel(tree.root)


def binary_search(search_list,target):
    left=0
    right=len(search_list)-1
    while left <= right:
        mid=(right+left)/2
        if search_list[mid] < target:
            left = mid + 1
            continue
        if search_list[mid] == target:
            return mid
        if search_list[mid] > target:
            right=mid-1
    return None


search_list=[1,4,7,8,9]
# print binary_search(search_list,8)

def insert_sort(origin_list):
    sorted_list=[]
    for i in range(0,len(origin_list)):
        if len(sorted_list) ==0:
            sorted_list.append(origin_list[i])
            continue
        for j in range(len(sorted_list)-1,-1,-1):
            if sorted_list[j]<=origin_list[i]:
                sorted_list.insert(j+1,origin_list[i])
                break
            if j==0:
                sorted_list.insert(0,origin_list[i])
    origin_list[:]=sorted_list[:]

origin_list=[2,4,1,6,3]
insert_sort(origin_list)
print origin_list







