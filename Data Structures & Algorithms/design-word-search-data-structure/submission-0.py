class TrieNode():
    def __init__(self, c: str):
        self.isEndOfWord = False
        self.char = c
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode("")

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        curr.isEndOfWord = True
    def search(self, word: str) -> bool:
        curr = self.root

        def backtrack(node: Optional[TrieNode()], i: int) -> bool:

            if not node:
                return False
            
            if i >= len(word):
                if node.isEndOfWord:
                    return True
                else:
                    return False
            
            c = word[i]
            if c == ".":
                for child in node.children.values():
                    found = backtrack(child, i + 1)
                    if found:
                        return True

                return False
            elif c in node.children:
                return backtrack(node.children[c], i + 1)
            else:
                return False
        
        return backtrack(curr, 0)