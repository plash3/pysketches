import sys
from typing import List

def knapsack(value: List[int], size: List[int], S: int) -> int:
    m = len(value)
    dp = [[-1 for _ in range(S + 1)] for _ in range(m)]
    def recurse(i, X):
        if i < 0:
            return 0
        if dp[i][X] != -1:
            return dp[i][X]
        if size[i] > X:
            result = recurse(i-1, X)
        else:
            result = max(value[i] + recurse(i-1, X-size[i]), recurse(i-1, X))
        dp[i][X] = result
        return result

    recurse(m-1, S)
    for row in dp:
        print(row)
    return dp[m-1][S]

def test_knapsack():
    value = [7, 9, 5, 12, 14, 6, 12]
    size  = [3, 4, 2, 6,  7,  3, 5]
    S = 15
    print(knapsack(value, size, S))

def main():
    test_knapsack()

if __name__ == '__main__':
    sys.exit(main())
