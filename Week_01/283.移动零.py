#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 21-1-13 下午6:28

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros=0
        for i in range(len(nums)):
            if nums[i]==0:
               zeros+=1
            else:
                nums[i-zeros]=nums[i]
        for i in range(len(nums)-zeros,len(nums)):
            nums[i]=0