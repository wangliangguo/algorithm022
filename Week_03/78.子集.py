#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 20-12-31 下午1:12


# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         ans = [[]]  # 迭代法
#         for num in nums:
#             subsets = []
#             for suba in ans:
#                 new_suba = suba + [num]
#                 subsets.append(new_suba)
#             ans.extend(subsets)
#         return ans

class Solution:

    #回溯法
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def recurse(nums,index,track):
            ans.append(track[:])
            for i in range(index,len(nums)):
                track.append(nums[i])#放入当前节点
                recurse(nums,i+1,track)
                track.pop(-1) #回溯

        recurse(nums,0,[])
        return ans

