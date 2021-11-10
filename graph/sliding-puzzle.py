import sys
from collections import deque
from typing import List

# https://leetcode.com/problems/sliding-puzzle/

def slidingPuzzle(board: List[List[int]]) -> int:
    def adj(state):
        adjacency_list = []
        l = list(state)
        i = state.index(0)
        mi = i % 3
        l[mi], l[mi+3] = l[mi+3], l[mi]
        adjacency_list.append(tuple(l))
        l[mi], l[mi+3] = l[mi+3], l[mi]
        if mi > 0:
            l[i], l[i-1] = l[i-1], l[i]
            adjacency_list.append(tuple(l))
            l[i], l[i-1] = l[i-1], l[i]
        if mi < 2:
            l[i], l[i+1] = l[i+1], l[i]
            adjacency_list.append(tuple(l))
        return adjacency_list

    state = tuple(n for row in board for n in row)
    queue = deque([state])
    visited_set = set([state])
    level = 0
    while queue:
        m = len(queue)
        for _ in range(m):
            state = queue.popleft()
            if state == (1, 2, 3, 4, 5, 0):
                return level
            for t in adj(state):
                if t not in visited_set:
                    queue.append(t)
                    visited_set.add(t)
        level += 1

    return -1

def test_slidingPuzzle():
    board = [[4,1,2],[5,0,3]]
    print(slidingPuzzle(board))

def main():
    test_slidingPuzzle()

if __name__ == '__main__':
    sys.exit(main())
