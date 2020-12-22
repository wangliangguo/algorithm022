#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 20-12-22 下午6:44

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 递归调用
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     ans=[]
    #     def inorder(root):
    #         if root:
    #             inorder(root.left)
    #             ans.append(root.val)
    #             inorder(root.right)
    #     inorder(root)
    #     return ans

    # 使用栈
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, ans = [], []
        if root is None:
            return []
        par = root
        while len(stack) > 0 or par is not None:
            while par is not None:
                stack.append(par)
                par = par.left
            par = stack.pop()
            ans.append(par.val)
            par = par.right

        return ans