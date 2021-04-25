import sys
from typing import List

# https://leetcode.com/problems/russian-doll-envelopes/

def maxEnvelops(envelopes: List[List[int]]) -> int:
    envelopes.sort(key=lambda t: (t[0], -t[1]))
    arr = [t[1] for t in envelopes]
    m = len(envelopes)
    dp = [0 for i in range(m)]
    L = 0
    for i in range(m):
        lo = 0
        hi = L
        while lo < hi:
            mid = (lo + hi) // 2
            if dp[mid] >= arr[i]:
                hi = mid
            else:
                lo = mid + 1
        dp[lo] = arr[i]
        if lo == L:
            L += 1

    return L

def test_maxEnvelops():
    arr = [[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]
    print(maxEnvelops(arr))

def main():
    test_maxEnvelops()

if __name__ == '__main__':
    sys.exit(main())
