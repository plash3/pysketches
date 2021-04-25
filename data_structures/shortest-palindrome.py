import sys

# https://leetcode.com/problems/shortest-palindrome/

def shortestPalindrome(s: str) -> str:
    if len(s) == 0:
        return s
    rev = ''.join(reversed(s))
    word = s + '#' + rev
    pmt = [0 for i in range(len(word)+1)]
    pmt[0] = -1
    pos = 1
    cnd = 0
    while pos < len(word):
        if word[pos] == word[cnd]:
            pmt[pos] = pmt[cnd]
        else:
            pmt[pos] = cnd
            cnd = pmt[cnd]
            while cnd >= 0 and word[pos] != word[cnd]:
                cnd = pmt[cnd]
        pos += 1
        cnd += 1
    pmt[pos] = cnd

    return rev[:len(s)-pmt[-1]] + s

def test_shortestPalindrome():
    s = 'abcd'
    print(shortestPalindrome(s))

def main():
    test_shortestPalindrome()

if __name__ == '__main__':
    sys.exit(main())
