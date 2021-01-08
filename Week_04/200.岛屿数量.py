#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 21-1-8 下午1:41


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def recurse(grid, r, c):
            if not (r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])):
                return
            if grid[r][c] != '1':
                return
            grid[r][c] = 2

            recurse(grid, r + 1, c)
            recurse(grid, r - 1, c)
            recurse(grid, r, c + 1)
            recurse(grid, r, c - 1)

        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    recurse(grid, i, j)
                    num += 1
        return num