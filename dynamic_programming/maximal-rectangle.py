import sys
from typing import List

def maximalRectangle(matrix: List[List[str]]) -> int:
    def largest_rectangle_under_histogram(heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area

    M = len(matrix)
    if M == 0:
        return 0
    N = len(matrix[0])
    auxm = [int(n) for n in matrix[0]]
    result = largest_rectangle_under_histogram(auxm)
    for i in range(1, M):
        for j in range(N):
            if matrix[i][j] != '0':
                auxm[j] += 1
            else:
                auxm[j] = 0
        curr_val = largest_rectangle_under_histogram(auxm)
        if result < curr_val:
            result = curr_val

    return result

def test_maximalRectangle():
    matrix = [
              ['0','1','1','0','1'],
              ['1','1','0','1','0'],
              ['0','1','1','1','0'],
              ['1','1','1','1','0'],
              ['1','1','1','1','1'],
              ['0','0','0','0','0']
             ]
    print(maximalRectangle(matrix))

def main():
    test_maximalRectangle()

if __name__ == '__main__':
    sys.exit(main())
