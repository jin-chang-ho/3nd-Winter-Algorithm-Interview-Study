class Trie:
    def __init__(self):
        self.queue = []

    def insert(self, word: str) -> None:
        temp = []
        for w in word:
            temp.append(w)
        self.queue.append(temp)

    def search(self, word: str) -> bool:
        for que in self.queue:
            if que[0] == word[0] and len(que) == len(word):
                count = 1
                for i in range(1, len(que)):
                    if que[i] != word[i]:
                        break
                    count = count + 1
                if count == len(word):
                    return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for que in self.queue:
            if que[0] == prefix[0] and len(que) >= len(prefix):
                count = 1
                for i in range(1, len(prefix)):
                    if que[i] != prefix[i]:
                        break
                    count = count + 1
                if count == len(prefix):
                    return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)