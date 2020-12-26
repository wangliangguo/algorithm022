#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 20-12-22 下午8:13
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     ans=[]
    #     def pre(root):
    #         if root:
    #             ans.append(root.val)
    #             pre(root.left)
    #             pre(root.right)
    #     pre(root)
    #     return ans

    #栈的方式
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack,ans=[root],[]
        while stack:
            root=stack.pop()
            ans.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
        return ans

 