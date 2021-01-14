#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 21-1-14 下午6:15

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data=[]


    def push(self,x):
        self.data.append(x)
    def pop(self):
        self.data.pop()
    def top(self):
        return self.data[-1]

    def getMin(self):
        return min(self.data)