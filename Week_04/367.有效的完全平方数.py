#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 21-1-6 下午1:44

class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        l, r = 0, num

        while l <= r:
            middle = (l + r) // 2
            if middle * middle == num:
                return True
            elif middle * middle < num:
                l = middle + 1
            else:
                r = middle - 1
        return False
