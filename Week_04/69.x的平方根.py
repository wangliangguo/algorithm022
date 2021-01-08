#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 21-1-6 下午5:23

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, anx = 0, x, -1

        while l <= r:
            mid = (l + r) // 2

            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans

 