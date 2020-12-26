class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
    #使用哈希表，时间复杂度：O(n)
        hashMap=dict()
        for i in s:
            hashMap[i]=hashMap.get(i,0)+1
        for j in t:
            hashMap[j]=hashMap.get(j,0)-1
        for value in hashMap.values():
            if value!=0:
                return False
        return True


class Solution2:
    # 排序后比较是否相等,O(nlogn)
    def isAnagram(self, s: str, t: str) -> bool:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        if s == t:
            return True
        else:
            return False



#2020-12-21 第一次
