import sys
from typing import List

def kmp_search(s: str, w: str) -> List[int]:
    partial_match_table = [0 for i in range(len(w)+1)]
    partial_match_table[0] = -1
    pos = 1
    cnd = 0
    while pos < len(w):
        if w[pos] == w[cnd]:
            partial_match_table[pos] = partial_match_table[cnd]
        else:
            partial_match_table[pos] = cnd
            cnd = partial_match_table[cnd]
            while cnd >= 0 and w[pos] != w[cnd]:
                cnd = partial_match_table[cnd]
        pos += 1
        cnd += 1
    partial_match_table[pos] = cnd

    result = []
    i = j = 0
    while j < len(s):
        if w[i] == s[j]:
            i += 1
            j += 1
            if i == len(w):
                result.append(j - i)
                i = partial_match_table[i]
        else:
            i = partial_match_table[i]
            if i < 0:
                j += 1
                i += 1

    return result

def test_kmp_search():
    s = 'ABC ABCDAB ABCDABCDABDE'
    w = 'ABCDABD'
    print(kmp_search(s, w))

def main():
    test_kmp_search()

if __name__ == '__main__':
    sys.exit(main())
