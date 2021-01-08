#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Author :wangliangguo
#@time : 21-1-5 下午6:14

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        queue=[(beginWord,1)]
        wordList=set(wordList) #转化成set提高判断效率

        if beginWord in wordList:
            wordList.remove(beginWord)
        while queue:
            start,level=queue.pop(0)
            if start==endWord:
                return level
            for i,c in enumerate(start):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    if char==c:
                        continue
                    new_node=start[:i]+char+start[i+1:]
                    if new_node in wordList:
                        queue.append((new_node,level+1))
                        wordList.remove(new_node)
        return 0