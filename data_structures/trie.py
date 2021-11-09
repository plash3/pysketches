import sys
from typing import List

# https://leetcode.com/problems/search-suggestions-system/

class TrieNode:
    def __init__(self, value=False):
        self.value = value
        self.children = {}
    def __repr__(self):
        return str([*self.children])

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.value = True

    def sort(self):
        def recurse(node):
            if node.children:
                node.children = dict(sorted(node.children.items()))
                for n in node.children.values():
                    recurse(n)
        node = self.root
        recurse(node)

    def find_words_for_prefix(self, prefix: str) -> List[str]:
        def recurse(node):
            if node.value:
                words.append(''.join(arr))
            for c in node.children:
                arr.append(c)
                recurse(node.children[c])
                arr.pop()

        node = self.root
        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]

        words = []
        arr = list(prefix)
        recurse(node)
        return words

def searchSuggestions(repository, customerQuery):
    m = len(customerQuery)
    if m < 2:
        return []

    result = []
    trie = Trie()
    for word in repository:
        trie.insert(word.lower())
    trie.sort()

    query = customerQuery.lower()
    for i in range(2, m+1):
        words = trie.find_words_for_prefix(query[:i])
        if words:
            result.append(words[:3])
        else:
            break

    return result

def test():
    repository = ['mobile','mouse','moneypot','monitor','mousepad']
    customerQuery = 'mouse'
    print(searchSuggestions(repository, customerQuery))

def main():
    test()

if __name__ == '__main__':
    sys.exit(main())
