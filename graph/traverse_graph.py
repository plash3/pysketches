import sys
import csv
from collections import Counter, defaultdict, deque
from typing import List

def traverse_graph(rows: List[str]) -> List[str]:
    degree = Counter()
    graph = defaultdict(list)
    for id,p1,p2 in rows:
        degree[id] += 0
        if p1:
            graph[id].append(p1)
            degree[p1] += 1
        if p2:
            graph[id].append(p2)
            degree[p2] += 1

    queue = deque([u for u in degree if degree[u] == 0])
    count = {u: 0 for u in degree}
    while queue:
        node = queue.popleft()
        for v in graph.get(node, []):
            count[v] += 1 + count[node]
            degree[v] -= 1
            if degree[v] == 0:
                queue.append(v)

    for row in rows:
        row.append(str(count[row[0]]))
    return [','.join(row) for row in rows]

def test_traverse_graph():
    data = []
    with open('FamilyTree.csv', 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            data.append(row)
    print(traverse_graph(data))

def main():
    test_traverse_graph()

if __name__ == '__main__':
    sys.exit(main())
