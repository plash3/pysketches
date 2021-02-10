import sys

class RollingHash:
    def __init__(self, modulo, length, base=256):
        self.modulo = self.next_prime(modulo)
        self.base = base % self.modulo
        self.degree = 1
        for i in range(length - 1):
            self.degree = self.degree * self.base % self.modulo
        self.u = 0

    def next_prime(self, n: int) -> int:
        m = (n + 1) * 2
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
                return i
        return -1

    def append(self, c: str) -> None:
        self.u = (self.u * self.base + ord(c)) % self.modulo

    def skip(self, c: str) -> None:
        self.u = (self.u - self.degree * ord(c)) % self.modulo

    def hash(self) -> int:
        return self.u

def RabinKarp(t: str, s: str) -> int:
    rs = RollingHash(len(t), len(s))
    for c in s: rs.append(c)
    rt = RollingHash(len(t), len(s))
    for i in range(len(s)):
        rt.append(t[i])
    if rs.hash() == rt.hash():
        if s == t[:len(s)]:
            return 0
        else:
            print('False positive at 0')
    for i in range(len(t) - len(s)):
        rt.skip(t[i])
        rt.append(t[i+len(s)])
        if rs.hash() == rt.hash():
            if s == t[i+1:i+1+len(s)]:
                return i+1
            else:
                print('False positive at', i+1)
    return -1

def test_RabinKarp():
    t = 'abracadabra'
    s = 'dab'
    print(RabinKarp(t, s))

def main():
    test_RabinKarp()

if __name__ == '__main__':
    sys.exit(main())
