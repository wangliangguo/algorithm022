#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 20-12-22 下午5:59

class Solution:
    # 递归调用
    # def preorder(self, root: 'Node') -> List[int]:
    #     ans=[]
    #     def pre(root):
    #         if root:
    #             ans.append(root.val)
    #             for child in root.children:
    #                 pre(child)
    #     dfs(root)
    #     return ans

    # 使用栈
    def preorder(self, root: 'Node') -> List[int]:
        stack, ans = [root], []
        if root is None:
            return []
        while len(stack) > 0:
            par = stack.pop()
            ans.append(par.val)
            for child in par.children[::-1]:
                if child is not None:
                    stack.append(child)
        return ans