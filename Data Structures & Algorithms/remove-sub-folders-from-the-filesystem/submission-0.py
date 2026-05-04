class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

    def add(self, file):
        cur = self
        files = file.split("/")
        for f in files:
            if f not in cur.children:
                cur.children[f] = Trie()
            cur = cur.children[f]
        cur.end = True

    def search(self, file):
        cur = self
        files = file.split("/")
        for i in range(len(files) - 1):
            cur = cur.children[files[i]]
            if cur.end:
                return True
        return False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            trie.add(f)
        res = []
        for f in folder:
            if not trie.search(f):
                res.append(f)
        return res