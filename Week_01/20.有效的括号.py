#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 21-1-14 下午6:08

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hashmap={'(':')','{':'}','[':']'}
        for char in s:
            if char=='(' or char=='{' or char=='[':
                stack.append(char)
            if char==')' or char=='}' or char==']':
                if len(stack)<=0:
                    return False
                else:
                    lastchar=stack.pop()
                    if hashmap[lastchar]!=char:
                        return False
        if len(stack)==0:
            return True
        else:
            return False
 