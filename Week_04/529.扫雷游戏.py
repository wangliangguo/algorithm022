#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 21-1-8 下午1:57
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        dx = [-1, 1, 0, 0, -1, 1, -1, 1]
        dy = [0, 0, -1, 1, -1, 1, 1, -1]
        visited = set()

        def recurse(board, x, y):
            cnt = 0
            for i in range(8):
                tx = dx[i] + x
                ty = dy[i] + y
                if tx < 0 or tx >= len(board) or ty < 0 or ty >= len(board[0]):
                    continue
                if board[tx][ty] == 'M':
                    cnt += 1
            if cnt > 0:
                board[x][y] = str(cnt)
                return

            board[x][y] = 'B'
            visited.add((x, y))
            for k in range(8):
                tx = dx[k] + x
                ty = dy[k] + y
                if tx < 0 or tx >= len(board) or ty < 0 or ty >= len(board[0]):
                    continue
                elif (tx, ty) in visited:
                    continue
                else:
                    recurse(board, tx, ty)

        x, y = click[0], click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            recurse(board, x, y)
        return board