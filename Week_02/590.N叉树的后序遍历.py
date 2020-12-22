#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 20-12-22 下午8:28

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # def postorder(self, root: 'Node') -> List[int]:

    #     ans=[]
    #     def post(root):
    #         if root:
    #             for child in root.children:
    #                 post(child)
    #             ans.append(root.val)

    #     post(root)
    #     return ans

    def postorder(self, root: 'Node') -> List[int]:
        stack,ans=[root],[]
        if root is None:
            return ans
        while stack:
            root=stack.pop()
            ans.append(root.val)
            for child in root.children:
                stack.append(child)
        return ans[::-1]