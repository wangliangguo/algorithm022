#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 20-12-29 下午2:11

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        def recurse(node):  #我的实现　　　　　　　　　　　　　　　　　　　　　　　　　　　　　

            if node.left is None and node.right is None:
                return node
            node.left,node.right=node.right,node.left

            if node.left is not None:
                recurse(node.left)
            if node.right is not None:
                recurse(node.right)
        if root is not None:
            recurse(root)
        return root

class Solution(object):
	def invertTree(self, root):　#高赞实现
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		# 递归函数的终止条件，节点为空时返回
		if not root:
			return None
		# 将当前节点的左右子树交换
		root.left,root.right = root.right,root.left
		# 递归交换当前节点的 左子树和右子树
		self.invertTree(root.left)
		self.invertTree(root.right)
		# 函数返回时就表示当前这个节点，以及它的左右子树
		# 都已经交换完了
		return root
