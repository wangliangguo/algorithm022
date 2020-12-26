#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 2020/12/26 上午11:25

class Solution:
    #使用排序算法
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     numDict={}
    #     for n in nums:
    #         if n in numDict:
    #             numDict[n]+=1
    #         else:
    #             numDict[n]=1
    #     sort_nums=sorted(numDict.items(),key=lambda x:x[1],reverse=True)
    #     return [v[0] for v in sort_nums[:k]]
    #使用堆
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        numDict = {}
        ans = []
        for n in nums:
            if n in numDict:
                numDict[n] += 1
            else:
                numDict[n] = 1
        maxHeap = [(-val, key) for key, val in numDict.items()]
        heapq.heapify(maxHeap)
        for i in range(k):
            ans.append(heapq.heappop(maxHeap)[1])
        return ans