#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 21-1-13 下午5:47

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ans=[[0]*(len(text2)+1)  for _ in range(len(text1)+1)]

        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    ans[i][j]=1+ans[i-1][j-1]
                else:
                    ans[i][j]=max(ans[i-1][j],ans[i][j-1])
        return ans[-1][-1]