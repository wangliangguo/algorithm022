#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 21-1-6 下午4:41


class Solution(object):
    def findMin(self, nums):
        l,r=0,len(nums)-1

        while l<r:
            mid=l+(r-l)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        return nums[l]