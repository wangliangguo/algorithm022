#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 21-1-6 下午6:00

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_step=0
        for i,num in enumerate(nums):
            if max_step<i:
                return False
            if max_step>=i and i+nums[i]>max_step:
                max_step=i+nums[i]
        return True
 