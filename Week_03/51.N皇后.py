#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 2021/1/2 下午8:58

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        cols,pie,na=[],[],[]
        ans=[]
        def recurse(row,state):
            if row>=n:
                state=[''.join(s) for s in state]
                ans.append(state.copy())
                return
            tmp=['.']*n
            for col in range(n):
                if col in cols or col+row in pie or row-col in na:
                    continue
                cols.append(col)
                pie.append(col+row)
                na.append(row-col)
                tmp[col]='Q'
                state.append(tmp)
                recurse(row+1,state)
                cols.pop()
                pie.pop()
                na.pop()
                state.pop()
                tmp[col]='.'
        recurse(0,[])
        return ans