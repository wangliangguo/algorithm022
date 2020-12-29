#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 20-12-29 下午6:33

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def recurse(root, level):
            if not root:
                return level
            level += 1
            return max(recurse(root.left, level), recurse(root.right, level))

        return recurse(root, 0)
 