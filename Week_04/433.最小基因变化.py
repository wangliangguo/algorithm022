#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 21-1-5 下午6:04

class Solution:

    #广度优先算法：将仅有一个字符不同的字符串连接构建图
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        queue = [(start, 0)]
        change = {'A': 'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}  # 每个基因对应的可变换基因
        while queue:
            node, step = queue.pop(0)
            if node == end:
                return step
            for i, v in enumerate(node):
                for j in change[v]:
                    new_node = node[:i] + j + node[i + 1:]
                    if new_node in bank:
                        queue.append((new_node, step + 1))
                        bank.remove(new_node)
        return -1