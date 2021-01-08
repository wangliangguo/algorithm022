#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 2021/1/2 下午9:41

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans=[]
        exist=[]
        def recurse(n,index,state):
            if len(state)==k:
                ans.append(state[:])
                return
            for i in range(index,n+1):
                if i in exist:
                    continue
                exist.append(i)
                state.append(i)
                recurse(n,i+1,state)
                state.pop()
                exist.pop()
        recurse(n,1,[])
        return ans