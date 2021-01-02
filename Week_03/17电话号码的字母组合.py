#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 2021/1/2 下午7:37

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap={}
        hashmap['2']='abc'
        hashmap['3']='def'
        hashmap['4']='ghi'
        hashmap['5']='jkl'
        hashmap['6']='mno'
        hashmap['7']='pqrs'
        hashmap['8']='tuv'
        hashmap['9']='wxyz'
        def recurse(index,combinate):
            if index==len(digits):
                ans.append(combinate[:])
                return
            for cchar in hashmap[digits[index]]:
                combinate=combinate+cchar
                recurse(index+1,combinate)
                combinate=combinate[:-1]
        ans=[]
        combinate=''
        if not digits:
            return []
        recurse(0,combinate)
        return ans