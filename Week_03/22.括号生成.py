#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 20-12-29 下午2:15


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:　#
        def recurse(s,n,left,right):
            if left==n and right==n:
                result.append(s)
            if left<n:
                recurse(s+'(',n,left+1,right)
            if right<left:
                recurse(s+')',n,left,right+1)
        result=[]
        recurse('',n,0,0)
        return result
 