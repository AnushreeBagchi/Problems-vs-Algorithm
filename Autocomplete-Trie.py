class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.result =  list()
    def insert(self, char):
        self.children[char] = TrieNode()
    
    def suffixes(self, suffix=""):        
        if self.children:
            for char, node in self.children.items():
                if node.is_word:
                    self.result.append(suffix+char)
                node.suffixes(suffix+char)
                
                


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            
        return node.is_word

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.insert(char)
            node = node.children[char]
        node.is_word = True
            
    # def suffix(self, word=""):
    #     node = self.root
    #     for char in word:
    #         if char not in node.children:
    #             return -1
    #         node = node.children[char]
    #     if node.is_word:
    #         return word
    #     elif not node.children:
    #         return
    #     else:
    #         self.suffix(word)

    def autocomplete(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return -1
            node = node.children[char]
        node.suffixes()
        print(node.result)


trie = Trie()
word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra']

for word in word_list:
    trie.insert(word)

test_words = ['bear', 'goo', 'good', 'goos']
for word in test_words:
    print(trie.search(word))

print(trie.autocomplete("ap"))
    
