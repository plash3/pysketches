import sys
from typing import List

# https://leetcode.com/problems/largest-rectangle-in-histogram/

def largest_rectangle_in_histogram(heights: List[int]) -> int:
    max_area = 0
    stack = [] # stack of pairs: (index, height)
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index
        stack.append((start, h))

    # remaining heights extended to the end of the histogram
    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))

    return max_area

def test_largest_rectangle_in_histogram():
    heights = [2,1,5,6,2,3]
    print(largest_rectangle_in_histogram(heights))

def main():
    test_largest_rectangle_in_histogram()

if __name__ == '__main__':
    sys.exit(main())
