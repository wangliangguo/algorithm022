class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 暴力法 O(n^2)
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target and i!=j:
        #             return [i,j]

        # 使用hashmap,O(n)
        hashMap = dict()
        for i in range(len(nums)):
            if target - nums[i] in hashMap:
                return [i, hashMap[target - nums[i]]]
            else:
                hashMap[nums[i]] = i

#2020-12-21 第一次
