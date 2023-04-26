from typing import List


class Node:
    def __init__(self, value: str = ""):
        self.value = value
        self.children = {}
        self.is_word = False

    def __repr__(self):
        return f"Node<ch={self.value} is_word={self.is_word}>"


class Trie:
    def __init__(self):
        self.root: Node = Node("")

    def get_ch_index(self, ch: str) -> int:
        return ord(ch) - ord("a")

    def insert(self, word: str) -> None:
        cur = self.root
        for i, w in enumerate(word):
            if not cur.children.get(w):
                cur.children[w] = Node(w)
            cur = cur.children[w]
        cur.is_word = True

    def delete(self, word: str) -> None:
        cur = self.root
        stack = []
        for w in word:
            if not cur.children.get(w):
                return

            stack.append(cur)
            cur = cur.children[w]
        cur.is_word = False

    def dfs(self, node: Node, prefix: str, res: List[str]) -> None:
        if not node:
            return

        if node.is_word:
            res.append(prefix)

        for w, child in node.children.items():
            self.dfs(child, prefix + w, res)

    def find(self, term: str) -> List[str]:
        prefix = ""
        cur = self.root
        for w in term:
            if w in cur.children:
                prefix += w
                cur = cur.children[w]
            else:
                return []

        words = []
        self.dfs(cur, prefix, words)
        return words
