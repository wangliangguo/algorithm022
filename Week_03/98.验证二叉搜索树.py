#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 20-12-29 下午5:34

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution():
    def isValidBST(self, root: TreeNode) -> bool:　#中徐遍历在验证是否符合顺序
        ans = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            ans.append(root)
            inorder(root.right)

        inorder(root)
        for i in range(len(ans) - 1):
            if ans[i].val >= ans[i + 1].val:
                return False
        return True


    def isValidBST(self, root: TreeNode) -> bool:
        # ans=[]
        # def inorder(root):
        #     if not root:
        #         return
        #     inorder(root.left)
        #     ans.append(root)
        #     inorder(root.right)
        # inorder(root)
        # for i in range(len(ans)-1):
        #     if ans[i].val>=ans[i+1].val:
        #         return False
        # return True

        # def inorder(root):　#中序遍历改进
        #     if not root:
        #         return True
        #     if not inorder(root.left):
        #         return False
        #     if root.val <= self.pre:
        #         return False
        #     self.pre = root.val
        #     return inorder(root.right)
        #
        # self.pre = float('-inf')
        # return inorder(root)


        def recurse(root, minVal, maxVal): #递归方法
            if not root:
                return True
            if root.val <= minVal or root.val >= maxVal:
                return False
            if not recurse(root.left, minVal, root.val):
                return False
            if not recurse(root.right, root.val, maxVal):
                return False
            return True


        return recurse(root, float('-inf'), float('inf'))