import sys
from typing import List

# https://leetcode.com/problems/word-ladder-ii/

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    parent = {}
    def BFS(s, t):
        level = {s}
        frontier = {s}
        i = 1
        while frontier:
            next_level = set()
            for u in frontier:
                for k in range(len(u)):
                    key = u[:k] + '*' + u[k+1:]
                    if key in adjacency_list:
                        for v in adjacency_list[key]:
                            if v not in level:
                                if v in parent:
                                    parent[v].append(u)
                                else:
                                    parent[v] = [u]
                                next_level.add(v)
            level.update(next_level)
            frontier = next_level
            i += 1

    def DFS(s, res):
        res.append(s)
        if s in parent:
            for v in parent[s]:
                DFS(v, res)
        else:
            sequence = res.copy()
            sequence.reverse()
            result.append(sequence)
        res.pop()

    adjacency_list = {}
    for word in wordList:
        for i in range(len(word)):
            key = word[:i] + '*' + word[i+1:]
            if key in adjacency_list:
                adjacency_list[key].append(word)
            else:
                adjacency_list[key] = [word]

    BFS(beginWord, endWord)
    if endWord not in parent:
        return []
    result = []
    DFS(endWord, [])
    return result

def test_ladderLength():
    beginWord = 'hit'
    endWord = 'cog'
    wordList = ['hot','lit','dot','dog','lot','log','cog']
    print(ladderLength(beginWord, endWord, wordList))

def main():
    test_ladderLength()

if __name__ == '__main__':
    sys.exit(main())
