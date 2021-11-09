import sys
from collections import deque
from typing import List

# https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

def graph(grid: List[List[str]]) -> int:
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'B':
                by,bx = i,j
            elif grid[i][j] == 'S':
                sy,sx = i,j
            elif grid[i][j] == 'T':
                ty,tx = i,j

    def is_reachable(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '#':
            return False
        queue = deque([(sy,sx)])
        visited_set = set([(sy,sx)])
        while queue:
            k,l = queue.popleft()
            if k == i and l == j:
                return True
            for y,x in adj(k,l):
                if (y,x) in visited_set or (y == by and x == bx):
                    continue
                queue.append((y,x))
                visited_set.add((y,x))
        return False

    directions = ((-1,0),(0,-1),(1,0),(0,1))
    def adj(i, j):
        adj_list = []
        for dy,dx in directions:
            k,l = i + dy, j + dx
            if 0 <= k < m and 0 <= l < n and grid[k][l] != '#':
                adj_list.append((k,l))
        return adj_list

    queue = deque([(by,bx,sy,sx)])
    visited_set = set([(by,bx,sy,sx)])
    level = 0
    while queue:
        L = len(queue)
        for _ in range(L):
            by,bx,sy,sx = queue.popleft()
            if by == ty and bx == tx:
                return level
            for i,j in adj(by, bx):
                if (i,j,by,bx) in visited_set:
                    continue
                if is_reachable(by*2 - i, bx*2 - j):
                    queue.append((i,j,by,bx))
                    visited_set.add((i,j,by,bx))
        level += 1

    return -1

def test_graph():
    grid = [['#','.','.','#','T','#','#','#','#'],
            ['#','.','.','#','.','#','.','.','#'],
            ['#','.','.','#','.','#','B','.','#'],
            ['#','.','.','.','.','.','.','.','#'],
            ['#','.','.','.','.','#','.','S','#'],
            ['#','.','.','#','.','#','#','#','#']]
    print(graph(grid))

def main():
    test_graph()

if __name__ == '__main__':
    sys.exit(main())
