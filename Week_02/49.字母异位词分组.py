
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 暴力法
        hashMap = {}
        for i in range(len(strs)):
            res = ''.join(sorted(strs[i]))
            if res in hashMap:
                hashMap[res].append(strs[i])
            else:
                hashMap[res] = [strs[i]]

        return list(hashMap.values())

if __name__=='__main__':
    s=Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))