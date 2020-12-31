#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 20-12-31 下午12:56


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # ans=1
        # if n<0:
        #     x=1/x
        #     n=-1*n
        # for i in range(n):
        #     ans=ans*x
        # return ans

        def recurse(x,n):
            if n==0 :
                return 1
            tmp=recurse(x,n//2)
            return tmp*tmp if n%2==0 else tmp*tmp*x
        if n<0:
            x=1/x
            n=-1*n
        return recurse(x,n)