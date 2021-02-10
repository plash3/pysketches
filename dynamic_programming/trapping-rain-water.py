import sys
import heapq
from typing import List

def trap(heightMap: List[List[int]]) -> int:
    m = len(heightMap)
    if m == 0:
        return 0
    n = len(heightMap[0])
    if n == 0:
        return 0

    visited = [[0 for j in range(n)] for i in range(m)]
    queue = []
    for i in range(n):
        heapq.heappush(queue, (heightMap[0][i], 0, i))
        heapq.heappush(queue, (heightMap[m-1][i], m-1, i))
        visited[0][i] = 1
        visited[m-1][i] = 1
    for i in range(1, m-1):
        heapq.heappush(queue, (heightMap[i][0], i, 0))
        heapq.heappush(queue, (heightMap[i][n-1], i, n-1))
        visited[i][0] = 1
        visited[i][n-1] = 1

    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    max_height = 0
    ans = 0
    while queue:
        height, i, j = heapq.heappop(queue)
        max_height = max(height, max_height)
        ans += max_height - height
        for k,l in directions:
            row = i + k
            col = j + l
            if row < 0 or col < 0 or row == m or col == n or visited[row][col]:
                continue
            heapq.heappush(queue, (heightMap[row][col], row, col))
            visited[row][col] = 1

    return ans

def test_trap():
    heightMap = [[9,9,9,9,9,9,8,9,9,9,9],
            [9,0,0,0,0,0,1,0,0,0,9],
            [9,0,0,0,0,0,0,0,0,0,9],
            [9,0,0,0,0,0,0,0,0,0,9],
            [9,9,9,9,9,9,9,9,9,9,9]
            ]
    print(trap(heightMap))

def main():
    test_trap()

if __name__ == '__main__':
    sys.exit(main())
