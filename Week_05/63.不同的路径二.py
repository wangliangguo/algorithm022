#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 21-1-12 下午6:30

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        ans = [0] * len(obstacleGrid[0])
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):

                if obstacleGrid[i][j] == 1:
                    ans[j] = 0
                else:
                    if i == 0 and j == 0:
                        ans[j] = 1
                    elif i == 0 and j > 0:
                        ans[j] = ans[j - 1]
                    elif j == 0 and i > 0:
                        ans[j] = ans[j]
                    else:
                        ans[j] = ans[j] + ans[j - 1]

        return ans[-1]