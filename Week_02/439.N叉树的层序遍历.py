#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 20-12-23 下午7:54

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # 递归实现
        # ans = []
        #
        # def levelfunction(node, level):
        #     if len(ans) == level:
        #         ans.append([])
        #     ans[level].append(node.val)
        #     for child in node.children:
        #         levelfunction(child, level + 1)
        #
        # if root is None:
        #     return []
        # levelfunction(root, 0)
        # return ans

        #通过队列实现
        if root is None:
            return []
        queue=[root]
        ans=[]
        while queue:
            level=[]
            for i in range(len(queue)):
                node=queue.pop(0)
                level.append(node.val)
                queue.extend(node.children)
            ans.append(level)
        return ans