import sys

def crackSafe(n: int, k: int) -> str:
    # De Bruijn sequence
    def recurse(i):
        if permutation[i] > 0:
            next_ind = permutation[i]
            permutation[i] = 0
            nonlocal index
            cycle[index] = i
            index += 1
            recurse(next_ind)

    span = k ** (n - 1)
    r = span * k
    cycle = [0 for i in range(r)]
    permutation = [0 for i in range(r)]
    for d in range(k):
        for i in range(span):
            permutation[span * d + i] = k * i + d

    index = 1
    for i in range(r):
        if permutation[i] > 0:
            recurse(i)

    for i in range(1, k):
        for j in range(span):
            permutation[span * i + j] = i

    return ''.join(str(permutation[i]) for i in cycle) + '0' * (n - 1)

def test_crackSafe():
    n = 3
    k = 2
    print(crackSafe(n, k))

def main():
    test_crackSafe()

if __name__ == '__main__':
    sys.exit(main())
