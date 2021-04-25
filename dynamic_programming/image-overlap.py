import sys
from collections import defaultdict
from typing import List

# https://leetcode.com/problems/image-overlap/

def largestOverlap(img1: List[List[int]], img2: List[List[int]]) -> int:
    dim = len(img1)

    def non_zero_cells(M):
        ret = []
        for m in range(dim):
            for n in range(dim):
                if M[m][n] == 1:
                    ret.append((m,n))
        return ret

    a_ones = non_zero_cells(img1)
    b_ones = non_zero_cells(img2)

    transformation_count = defaultdict(int)
    max_overlaps = 0

    for x_a, y_a in a_ones:
        for x_b, y_b in b_ones:
            vec = (x_b - x_a, y_b - y_a)
            transformation_count[vec] += 1
            max_overlaps = max(max_overlaps, transformation_count[vec])

    return max_overlaps

def test_largestOverlaps():
    img1 = [[1,1,0],[0,1,0],[0,1,0]]
    img2 = [[0,0,0],[0,1,1],[0,0,1]]
    print(largestOverlap(img1, img2))

def main():
    test_largestOverlaps()

if __name__ == '__main__':
    sys.exit(main())
