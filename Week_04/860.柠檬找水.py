#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 21-1-5 下午2:19

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        five, ten, twen = 0, 0, 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                five -= 1
                ten += 1
                if five < 0:
                    return False
            elif bill == 20:
                if ten > 0:
                    ten -= 1
                    five -= 1
                    if ten < 0 or five < 0:
                        return False
                else:
                    five -= 3
                    if five < 0:
                        return False
        return True