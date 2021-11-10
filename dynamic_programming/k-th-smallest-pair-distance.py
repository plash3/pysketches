import sys
from typing import List

# https://leetcode.com/problems/find-k-th-smallest-pair-distance/

def smallestDistancePair(nums: List[int], k: int) -> int:
    def possible(guess):
        count = left = 0
        for right in range(m):
            while nums[right] - nums[left] > guess:
                left += 1
            count += right - left
        return count >= k

    m = len(nums)
    nums.sort()
    lo = 0
    hi = nums[m-1] - nums[0]
    while lo < hi:
        mid = (lo + hi) // 2
        if possible(mid):
            hi = mid
        else:
            lo = mid + 1

    return lo

def test_smallestDistancePair():
    nums = [1,3,1]
    k = 3
    print(smallestDistancePair(nums, k))

def main():
    test_smallestDistancePair()

if __name__ == '__main__':
    sys.exit(main())
