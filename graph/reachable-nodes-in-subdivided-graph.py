import sys
import heapq
from collections import defaultdict
from typing import List

# https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/

def reachableNodes(edges: List[List[int]], M: int, N: int) -> int:
    graph = defaultdict(dict)
    for u, v, w in edges:
        graph[u][v] = graph[v][u] = w

    pq = [(0,0)]
    distances = {0: 0}
    used = {}
    ans = 0
    while pq:
        dis, node = heapq.heappop(pq)
        if dis > distances[node]:
            continue
        ans += 1
        for nei, weight in graph[node].items():
            used[node, nei] = min(weight, M - dis)
            nei_dis = dis + weight + 1
            if nei_dis < distances.get(nei, M + 1):
                heapq.heappush(pq, (nei_dis, nei))
                distances[nei] = nei_dis

    for u, v, w in edges:
        ans += min(w, used.get((u,v), 0) + used.get((v,u), 0))

    return ans

def test_reachableNodes():
    edges = [[0,1,10],[0,2,1],[1,2,2]]
    M = 6
    N = 3
    print(reachableNodes(edges, M, N))

def main():
    test_reachableNodes()

if __name__ == '__main__':
    sys.exit(main())
