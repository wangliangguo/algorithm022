#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 21-1-5 下午2:49

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g=sorted(g)
        s=sorted(s)
        ans=0
        j=0
        for i in range(len(g)):
            while j<len(s):
                if g[i]<=s[j]:
                    ans+=1
                    j+=1
                    break
                else:
                    j+=1
        return ans