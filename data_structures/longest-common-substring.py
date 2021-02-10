import sys

def longest_common_substring(S: str) -> str:
    m = len(S)
    p = [0 for i in range(m)]
    c = [0 for i in range(m)]
    cnt = [0 for i in range(256)]
    for a in S:
        cnt[ord(a)] += 1
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]
    for i in range(m):
        cnt[ord(S[i])] -= 1
        p[cnt[ord(S[i])]] = i
    classes = 0
    c[p[0]] = 0
    for i in range(1, m):
        if S[p[i]] != S[p[i-1]]:
            classes += 1
        c[p[i]] = classes
    classes += 1

    h = 1
    pn = [0 for i in range(m)]
    while h < m:
        cn = [0 for i in range(m)]
        for i in range(m):
            pn[i] = p[i] - h
            if pn[i] < 0:
                pn[i] += m
        cnt = [0 for i in range(classes)]
        for i in range(m):
            cnt[c[pn[i]]] += 1
        for i in range(1, classes):
            cnt[i] += cnt[i-1]
        for i in range(m-1, -1, -1):
            cnt[c[pn[i]]] -= 1
            p[cnt[c[pn[i]]]] = pn[i]
        classes = 0
        cn[p[0]] = 0
        for i in range(1, m):
            if c[p[i]] != c[p[i-1]] or c[(p[i]+h)%m] != c[(p[i-1]+h)%m]:
                classes += 1
            cn[p[i]] = classes
        c = cn
        classes += 1
        h <<= 1

    inverse_suffix_array = [0 for i in range(m)]
    for i in range(m):
        inverse_suffix_array[p[i]] = i
    LCP = [0 for i in range(m)]
    l = 0
    max_length = max_ind = 0
    for i in range(m):
        k = inverse_suffix_array[i]
        if k > 0:
            j = p[k-1]
            while i < m-l and j < m-l and S[i+l] == S[j+l]:
                l += 1
            LCP[k] = l
            if l > 0:
                if max_length < l:
                    max_length = l
                    max_ind = i
                l -= 1

    return S[max_ind:max_ind+max_length]

def test_longest_common_substring():
    S = 'BANANA'
    print(longest_common_substring(S))

def main():
    test_longest_common_substring()

if __name__ == '__main__':
    sys.exit(main())
