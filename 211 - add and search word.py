class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        """
        Adds a word into the data structure.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res

    def dfs(self, node, word):
        if not word:
            if node.word == True:
                self.res = True
            # have to return regardless of node.word's value
            return
        if word[0] == ".":
            # node.children = { d: TrieNode() }
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            # check if node corresponding to word[0] exists
            node = node.children.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])


'''
We have to use a global self.res bc if we try to use normal recursion,

def dfs(self, node, word):
    if not word:
        return node.word == True

    if word[0] == ".":
        # node.children = { d: TrieNode() }
        for n in node.children.values():
            return self.dfs(n, word[1:])
    else:
        # check if node corresponding to word[0] exists
        node = node.children.get(word[0])
        if not node:
            return False

        return self.dfs(node, word[1:])

consider the test cases:
add_word("at")
add_word("and")
add_word("add")
add_word("bat")

node a has children: {t, n, d}
node b has children: {a}

Call search(".at"):
In the first iteration of "for n in node.children",
node a is going to start a new function call with:
    node.children = {t, n, d}
    word = "at"
When it determines that char "a" is not in its children,
it will return False to the function call before itself,
which will then trigger "return self.dfs(n, word[1:])".
This will terminate our function with a return value of False,
even though we didn't get to check node b's children yet.
'''


dictionary = WordDictionary()
# dictionary.add_word("dad")
# dictionary.add_word("bad")
# dictionary.add_word("mad")
# dictionary.add_word("pad")
# dictionary.search("bad")
# dictionary.search(".ad")
# dictionary.search("b..")
# dictionary.search("t..")


dictionary.add_word("at")
dictionary.add_word("and")
dictionary.add_word("an")
dictionary.add_word("add")
dictionary.search("a")
dictionary.search(".at")
dictionary.add_word("bat")
dictionary.search(".at")
