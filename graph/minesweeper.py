import sys
import random
from collections import defaultdict

def minesweeper(cols: int, rows: int, mine_num: int):
    directions = [(-1,0), (0,-1), (1,0), (0,1)]
    def adj(i, j):
        adj_list = []
        for d in directions:
            m,n = i + d[0], j + d[1]
            if 0 <= m < rows and 0 <= n < cols:
                adj_list.append((m,n))
        return adj_list

    visited_set = set()
    def recurse(i, j):
        if (i,j) in mine_map:
            matrix[i][j] = str(mine_map[(i,j)])
        else:
            matrix[i][j] = '.'
            for m,n in adj(i,j):
                if (m,n) not in visited_set:
                    visited_set.add((m,n))
                    recurse(m,n)

    def update_state(i, j):
        if (i,j) in mine_set:
            for (m,n) in mine_set:
                matrix[m][n] = '*'
            return False
        recurse(i, j)
        return True

    def print_state():
        print(header)
        for i, row in enumerate(matrix):
            print(i+1, ' '.join(row))

    random.seed()
    mine_set = set()
    while len(mine_set) < mine_num:
        mine_set.add((random.randrange(rows), random.randrange(cols)))

    mine_map = defaultdict(int)
    for i,j in mine_set:
        for m in range(max(0, i-1), min(rows, i+2)):
            for n in range(max(0, j-1), min(cols, j+2)):
                if (m,n) not in mine_set:
                    mine_map[(m,n)] += 1

    matrix = [['H' for _ in range(cols)] for _ in range(rows)]
    header = '  ' + ' '.join(str(i) for i in range(1, cols+1))
    print_state()

    state = True
    while state:
        print('Row:', end=' ')
        row = int(input()) - 1
        print('Col:', end=' ')
        col = int(input()) - 1
        if (row, col) in visited_set:
            continue
        visited_set.add((row, col))
        state = update_state(row, col)
        print_state()
        if len(visited_set) == rows * cols - mine_num:
            break

    print('You win!' if state else 'You lose!')

def test_minesweeper():
    pass

def main():
    test_minesweeper()

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('# Usage: ./minesweeper <cols> <rows> <# of mines>')
        exit()
    t = tuple(map(int, sys.argv[1:]))
    minesweeper(*t)
