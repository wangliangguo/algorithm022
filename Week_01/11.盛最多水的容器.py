#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 21-1-13 下午6:21


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea=-1
        i,j=0,len(height)-1
        while i<j:
            if (j-i)*min(height[i],height[j])>maxArea:
                maxArea=(j-i)*min(height[i],height[j])
            if height[i]>height[j]:
                j-=1
            else:
                i+=1

        return maxArea