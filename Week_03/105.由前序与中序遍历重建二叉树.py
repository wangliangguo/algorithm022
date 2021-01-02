#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 2021/1/2 下午10:09

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recurse(preorder, inorder):
            if len(inorder) == 0:
                return
            root = TreeNode(preorder[0])
            rindex = inorder.index(root.val)
            root.left = recurse(preorder[1:rindex + 1], inorder[:rindex])
            root.right = recurse(preorder[rindex + 1:], inorder[rindex + 1:])
            return root

        return recurse(preorder, inorder)
