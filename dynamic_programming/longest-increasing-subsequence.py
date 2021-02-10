import sys
from typing import List

class LIS:
    def longest_increasing_subsequence(self, nums: List[int]) -> int:
        m = len(nums)
        arr = [0 for i in range(m)]
        L = 0
        for i in range(m):
            lo = 0
            hi = L
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] >= nums[i]:
                    hi = mid
                else:
                    lo = mid + 1
            arr[lo] = nums[i]
            if lo == L:
                L += 1

        return L

def test_longest_increasing_subsequence():
    nums = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    sl = LIS()
    print(sl.longest_increasing_subsequence(nums))

def main():
    test_longest_increasing_subsequence()

if __name__ == '__main__':
    sys.exit(main())
