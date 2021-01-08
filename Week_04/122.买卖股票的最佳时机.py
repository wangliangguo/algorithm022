#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 21-1-7 下午2:13

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result=0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                result+=prices[i+1]-prices[i]
        return result