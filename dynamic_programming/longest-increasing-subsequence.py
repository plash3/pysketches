import sys
from typing import List

# https://leetcode.com/problems/longest-increasing-subsequence/

def longest_increasing_subsequence(nums: List[int]) -> int:
    m = len(nums)
    dp = [0 for i in range(m)]
    L = 0
    for n in nums:
        lo = 0
        hi = L
        while lo < hi:
            mid = (lo + hi) // 2
            if n > dp[mid]:
                lo = mid + 1
            else:
                hi = mid
        dp[lo] = n
        if lo == L:
            L += 1

    return L

def test_longest_increasing_subsequence():
    nums = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print(longest_increasing_subsequence(nums))

def main():
    test_longest_increasing_subsequence()

if __name__ == '__main__':
    sys.exit(main())
