import sys
import math
from typing import List

def radix_sort(arr: List[int], radix: int) -> List[int]:
    def counting_sort(arr: List[int], digit: int) -> List[int]:
        m = len(arr)
        cnt = [0 for i in range(radix)]
        for i in range(m):
            idigit = (arr[i] // radix ** digit) % radix
            cnt[idigit] += 1
        for i in range(1, radix):
            cnt[i] += cnt[i-1]
        result = [0 for i in range(m)]
        for i in range(m-1, -1, -1):
            idigit = (arr[i] // radix ** digit) % radix
            cnt[idigit] -= 1
            result[cnt[idigit]] = arr[i]
        return result

    max_number = max(arr)
    digits = math.floor(math.log(max_number, radix)) + 1
    output = arr
    for i in range(digits):
        output = counting_sort(output, i)
    return output

def test_radix_sort():
    arr = [407,107,105,104,103,209,402,5,101]
    print(radix_sort(arr, 10))

def main():
    test_radix_sort()

if __name__ == '__main__':
    sys.exit(main())
