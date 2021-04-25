import sys
from typing import List

# https://leetcode.com/problems/sliding-puzzle/

def slidingPuzzle(board: List[List[int]]) -> int:
    def adjacency_list(t: tuple) -> List[tuple]:
        res = []
        ind = t.index(0)
        l = list(t)
        if ind != 0 and ind != n:
            l[ind], l[ind-1] = l[ind-1], l[ind]
            res.append(tuple(l))
            l[ind], l[ind-1] = l[ind-1], l[ind]
        if ind != n-1 and ind != m-1:
            l[ind], l[ind+1] = l[ind+1], l[ind]
            res.append(tuple(l))
            l[ind], l[ind+1] = l[ind+1], l[ind]
        if ind < n:
            l[ind], l[ind+n] = l[ind+n], l[ind]
            res.append(tuple(l))
            l[ind], l[ind+n] = l[ind+n], l[ind]
        if ind >= n:
            l[ind], l[ind-n] = l[ind-n], l[ind]
            res.append(tuple(l))
            l[ind], l[ind-n] = l[ind-n], l[ind]
        return res

    n = len(board[0])
    m = n * 2
    t = tuple(n for row in board for n in row)
    target = (1, 2, 3, 4, 5, 0)
    if t == target:
        return 0
    level = {t: 0}
    parent = {t: None}
    i = 1
    frontier = [t]
    while frontier:
        next_level = []
        for u in frontier:
            for v in adjacency_list(u):
                if v == target:
                    return i
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next_level.append(v)
        frontier = next_level
        i += 1

    return -1

def test_slidingPuzzle():
    board = [[4,1,2],[5,0,3]]
    print(slidingPuzzle(board))

def main():
    test_slidingPuzzle()

if __name__ == '__main__':
    sys.exit(main())
