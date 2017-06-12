#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 队列和戰

class Queue(object):
# class Stack(object):
    def __init__(self):
        self.data_list=[]

    def insert(self,data):
        self.data_list.append(data)

    def pop(self):
        if len(self.data_list)==0:
            return None
        data=self.data_list[0]
        # data=self.data_list[-1]
        # del self.data_list[-1]
        del self.data_list[0]

        return data

    def size(self):
        return len(self.data_list)

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


# 二叉树

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

# 二分查找

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



# 插入排序
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
# insert_sort(origin_list)
# print origin_list