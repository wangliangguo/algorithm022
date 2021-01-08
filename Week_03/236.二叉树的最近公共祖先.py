#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 2021/1/2 下午10:32

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def recurse(root,p,q):
            if not root or root==p or root==q:
                return root
            left=recurse(root.left,p,q)
            right=recurse(root.right,p,q)
            if left and right:
                return root
            elif left:
                return left
            else:
                return right
        return recurse(root,p,q)