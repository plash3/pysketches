import sys
from collections import defaultdict, deque
from typing import List

# https://leetcode.com/problems/word-ladder-ii/

def find_all_shortest_paths(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    graph = defaultdict(list)

    m = len(beginWord)
    for word in wordList:
        for i in range(m):
            key = word[:i] + '*' + word[i+1:]
            graph[key].append(word)

    def adj(word: str) -> List[str]:
        adj_list = []
        for i in range(m):
            key = word[:i] + '*' + word[i+1:]
            for w in graph.get(key, []):
                if w != word:
                    adj_list.append(w)
        return adj_list

    parent = defaultdict(list)
    visited_set = set([beginWord])
    queue = deque([beginWord])
    while queue:
        level = set()
        L = len(queue)
        for _ in range(L):
            word = queue.popleft()
            if word == endWord:
                break
            for w in adj(word):
                if w in visited_set:
                    continue
                parent[w].append(word)
                if w not in level:
                    queue.append(w)
                    level.add(w)
        visited_set.update(level)

    def recurse(word: str):
        arr.append(word)
        parents = parent.get(word)
        if not parents:
            result.append(list(reversed(arr)))
        else:
            for w in parents:
                recurse(w)
        arr.pop()

    arr = []
    result = []
    if endWord in parent:
        recurse(endWord)
    return result

def test_find_all_shortest_paths():
    beginWord = 'hit'
    endWord = 'cog'
    wordList = ['hot','lit','dot','dog','lot','log','cog']
    print(find_all_shortest_paths(beginWord, endWord, wordList))

def main():
    test_find_all_shortest_paths()

if __name__ == '__main__':
    sys.exit(main())
