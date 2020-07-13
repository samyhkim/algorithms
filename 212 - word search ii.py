class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True

    def search(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.word


def findWords(board, words):
    res = []
    trie = Trie()
    node = trie.root
    for word in words:
        trie.insert(word)
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(board, node, i, j, "", res)
    return res


def dfs(board, node, i, j, path, res):
    if node.word:
        res.append(path)
        node.word = False  # ?
    if not 0 <= i < len(board) or not 0 <= j < len(board[0]):
        return False
    temp = board[i][j]
    # returns None while node.children[temp] doesn't
    node = node.children.get(temp)
    if not node:
        return False
    board[i][j] = '#'
    dfs(board, node, i+1, j, path+temp, res)
    dfs(board, node, i-1, j, path+temp, res)
    dfs(board, node, i, j+1, path+temp, res)
    dfs(board, node, i, j-1, path+temp, res)
    board[i][j] = temp


board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]
words = ["oath", "pea", "eat", "rain"]

print(findWords(board, words))
