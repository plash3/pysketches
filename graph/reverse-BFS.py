import sys
from collections import defaultdict, Counter, deque
from typing import List

# https://www.hackerrank.com/challenges/kingdom-division/problem
# https://jimmy-shen.medium.com/kingdom-division-problem-from-hackerrank-e4aa3a8208c8

def traverse(n: int, roads: List[List[int]]) -> int:
    graph = defaultdict(set)
    degree = Counter()
    for u, v in roads:
        graph[u].add(v)
        graph[v].add(u)
        degree[u] += 1
        degree[v] += 1

    count = {u: {True: 1, False: 1} for u in degree}
    leaves = deque([u for u in degree if degree[u] == 1])
    while True:
        node = leaves.popleft()
        count[node][False] = count[node][True] - count[node][False]
        if degree[node] == 0:
            root = node
            break
        else:
            parent = graph[node].pop()
            graph[parent].discard(node)
            degree[parent] -= 1
            if degree[parent] == 1:
                leaves.append(parent)
            count[parent][True] *= count[node][True] + count[node][False]
            count[parent][False] *= count[node][False]

    total = 2 * count[root][0]
    return total % (10**9 + 7)

def test_traverse():
    n = 4
    roads = [[1,2], [1,3], [3,4], [3,5]]
    print(traverse(n, roads))

def main():
    test_traverse()

if __name__ == '__main__':
    sys.exit(main())
