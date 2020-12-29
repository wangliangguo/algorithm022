class Solution:

    def nthUglyNumber(self, n: int) -> int:
        ans = [1] * n
        two, three, five = 0, 0, 0
        for i in range(1, n):
            t1, t2, t3 = ans[two] * 2, ans[three] * 3, ans[five] * 5
            t = min(min(t1, t2), t3)
            if t == t1: two += 1
            if t == t2: three += 1
            if t == t3: five += 1
            ans[i] = t
        return ans[n - 1]
