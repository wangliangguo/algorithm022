#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 21-1-6 下午6:17

class Solution:
    def jump(self, nums: List[int]) -> int:

        maxp,end,step=0,0,0

        for i in range(len(nums)-1):
            maxp=max(nums[i]+i,maxp)
            if i==end:
                end=maxp
                step+=1
        return step