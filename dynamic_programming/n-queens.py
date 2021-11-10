import sys
from typing import List

# https://leetcode.com/problems/n-queens/

def nqueens(n: int) -> List[List[str]]:
    def is_available(i, j):
        return cols[j] == 0 and hill_diagonals[i+j] == 0 and dale_diagonals[i-j] == 0

    def set_availability(i, j, v):
        cols[j] = v
        hill_diagonals[i+j] = v
        dale_diagonals[i-j] = v
        queens[i] = j

    def recurse(i):
        if i == n:
            result.append(['.' * k + 'Q' + '.' * (n-k-1) for k in queens])
        else:
            for j in range(n):
                if is_available(i, j):
                    set_availability(i, j, 1)
                    recurse(i + 1)
                    set_availability(i, j, 0)

    queens = [0] * n
    cols = [0] * n
    hill_diagonals = [0] * (n*2 - 1)
    dale_diagonals = [0] * (n*2 - 1)
    result = []
    recurse(0)
    return result

def test_nqueens():
    n = 4
    print(nqueens(n))

def main():
    test_nqueens()

if __name__ == '__main__':
    sys.exit(main())
