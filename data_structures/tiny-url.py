import sys
import random
import string

class Codec:
    def __init__(self):
        self.long_to_short = {}
        self.short_to_long = {}

    def random_string(self) -> str:
        seed = string.digits + string.ascii_letters
        return ''.join(random.choice(seed) for i in range(6))

    def encode(self, longUrl: str) -> str:
        if longUrl in self.long_to_short:
            return self.long_to_short[longUrl]
        while True:
            unique_id = self.random_string()
            if unique_id not in self.short_to_long:
                self.long_to_short[longUrl] = unique_id
                self.short_to_long[unique_id] = longUrl
                break
        return f'http://tinyurl.com/{unique_id}'

    def decode(self, shortUrl: str) -> str:
        key = shortUrl.split('/')[-1]
        if key in self.short_to_long:
            return self.short_to_long[key]
        return None

def test_Codec():
    longUrl = 'https://leetcode.com/problems/encode-and-decode-tinyurl'
    cd = Codec()
    print(cd.encode(longUrl))

def main():
    test_Codec()

if __name__ == '__main__':
    sys.exit(main())
