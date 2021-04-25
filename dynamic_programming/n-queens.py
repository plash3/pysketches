import sys
from typing import List

# https://leetcode.com/problems/n-queens/

def nqueens(n: int) -> List[List[str]]:
    def isavailable(i, j):
        return cols[j] == 0 and hill_diagonals[i+j] == 0 and dale_diagonals[i-j] == 0

    def set_availability(i, j, v):
        queens[i] = j
        cols[j] = v
        hill_diagonals[i+j] = v
        dale_diagonals[i-j] = v

    def add_solution():
        solution = []
        for i in queens:
            solution.append('.' * i + 'Q' + '.' * (n - i - 1))
        result.append(solution)

    def backtrack(i):
        for j in range(n):
            if isavailable(i, j):
                set_availability(i, j, 1)
                if i == n - 1:
                    add_solution()
                else:
                    backtrack(i + 1)
                set_availability(i, j, 0)

    cols = [0] * n
    hill_diagonals = [0] * (n * 2 - 1)
    dale_diagonals = [0] * (n * 2 - 1)
    queens = [0] * n
    result = []
    backtrack(0)

    return result

def test_nqueens():
    n = 4
    print(nqueens(n))

def main():
    test_nqueens()

if __name__ == '__main__':
    sys.exit(main())
