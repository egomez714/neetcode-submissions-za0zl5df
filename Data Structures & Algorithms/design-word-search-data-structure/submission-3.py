class Node:
    def __init__(self):
        self.data = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.data:
                cur.data[c] = Node()
            cur = cur.data[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.data.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.data:
                        return False
                    cur = cur.data[c]
            return cur.endOfWord

        return dfs(0, self.root)