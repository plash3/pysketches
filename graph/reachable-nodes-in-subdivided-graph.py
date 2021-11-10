import sys
import heapq
from collections import defaultdict
from typing import List

# https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/

def reachableNodes(edges: List[List[int]], maxMoves: int, n: int) -> int:
    graph = defaultdict(dict)
    for u,v,w in edges:
        graph[u][v] = graph[v][u] = w

    distances = {0: 0}
    queue = [(0, 0)]
    reached = {}
    count = 0
    while queue:
        distance, node = heapq.heappop(queue)
        if distance > distances[node]:
            continue
        count += 1
        for nei, weight in graph[node].items():
            reached[(node,nei)] = min(weight, maxMoves - distance)
            dis = distance + weight + 1
            if dis < distances.get(nei, maxMoves + 1):
                distances[nei] = dis
                heapq.heappush(queue, (dis,nei))

    for u,v,w in edges:
        count += min(reached.get((u,v), 0) + reached.get((v,u), 0), w)
    return count

def test_reachableNodes():
    edges = [[0,1,10],[0,2,1],[1,2,2]]
    maxMoves = 6
    n = 3
    print(reachableNodes(edges, maxMoves, n))

def main():
    test_reachableNodes()

if __name__ == '__main__':
    sys.exit(main())
