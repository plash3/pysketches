import sys

# https://leetcode.com/problems/longest-duplicate-substring/
# https://cp-algorithms.com/string/suffix-array.html
# https://www.cs.helsinki.fi/u/tpkarkka/opetus/11s/spa/lecture10.pdf

def longestDuplicateSubstring(S: str) -> str:
    def match(length, modulo, base=256):
        base %= modulo
        degree = 1
        for i in range(length - 1):
            degree = degree * base % modulo
        rolling_hash = 0
        for i in range(length):
            rolling_hash = (rolling_hash * base + ord(S[i])) % modulo
        hash_values = { rolling_hash: 0 }
        for i in range(len(S) - length):
            rolling_hash = (rolling_hash - degree * ord(S[i])) % modulo
            rolling_hash = (rolling_hash * base + ord(S[i+length])) % modulo
            if rolling_hash in hash_values:
                j = hash_values[rolling_hash]
                if S[j:j+length] == S[i+1:i+1+length]:
                    nonlocal ans
                    ans = S[i+1:i+1+length]
                    return True
            else:
                hash_values[rolling_hash] = i + 1
        return False

    m = (len(S) + 1) * 2
    arr = [i%2 for i in range(m+1)]
    arr[1] = 0
    arr[2] = 1
    k = round(m ** 0.5)
    for i in range(3, k+1, 2):
        if arr[i] == 1:
            for j in range(i**2, m+1, i*2):
                arr[j] = 0
    for i in range(m, 1, -1):
        if arr[i] == 1:
            modulo = i
            break
    ans = ''
    lo, hi = 0, len(S)
    while lo <= hi:
        median = (lo + hi) // 2
        if match(median, modulo):
            lo = median + 1
        else:
            hi = median - 1
    return ans

def test_longestDuplicateSubstring():
    S = 'banana'
    print(longestDuplicateSubstring(S))

def main():
    test_longestDuplicateSubstring()

if __name__ == '__main__':
    sys.exit(main())
