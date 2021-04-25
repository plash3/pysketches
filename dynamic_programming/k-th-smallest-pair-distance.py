import sys
from typing import List

# https://leetcode.com/problems/find-k-th-smallest-pair-distance/

def smallestDistancePair(nums: List[int], k: int) -> int:
    m = len(nums)
    nums.sort()

    lo = 0
    hi = nums[m-1] - nums[0]
    while lo < hi:
        mi = (lo + hi) // 2
        left = cnt = 0
        for right in range(m):
            while nums[right] - nums[left] > mi:
                left += 1
            cnt += right - left
        if cnt >= k:
            hi = mi
        else:
            lo = mi + 1

    return lo

def test_smallestDistancePair():
    nums = [1,3,1]
    k = 3
    print(smallestDistancePair(nums, k))

def main():
    test_smallestDistancePair()

if __name__ == '__main__':
    sys.exit(main())
