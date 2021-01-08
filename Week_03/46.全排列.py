#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 2021/1/2 下午9:19


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        exist = []

        def recurse(nums, index, state):
            if index >= len(nums):
                ans.append(state[:])
                return

            for i in range(len(nums)):
                if i in exist:
                    continue
                exist.append(i)
                state.append(nums[i])
                recurse(nums, index + 1, state)
                exist.pop()
                state.pop()

        recurse(nums, 0, [])
        return ans


