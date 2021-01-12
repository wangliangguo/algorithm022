#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 21-1-12 下午4:05

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans=[]
        for i in range(m):
            ans.append([1])
        for j in range(n-1):
            ans[0].append(1)
        for i in range(1,m):
            for j in range(1,n):
                ans[i].append(ans[i-1][j]+ans[i][j-1])
        return ans[-1][-1]