class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.result =  list()

    def insert(self, char):
        self.children[char] = TrieNode()
    
    def suffixes(self, prefix, result):
        if self.children:
            for char, node in self.children.items():
                if node.is_word:
                    result.append(prefix+char)

                node.suffixes( prefix+char , result)
        return result                

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
            

    def autocomplete(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return -1
            node = node.children[char]
        result = node.suffixes(word, list())
        return result

trie = Trie()
word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra']
for word in word_list:
    trie.insert(word)

# test_words = ['bear', 'goo', 'good', 'goos']
# for word in test_words:
#     print(trie.search(word))

# Tests

print("Pass" if trie.autocomplete("ap")==['apple'] else "Fail")
print("Pass" if trie.autocomplete("g")==['goo', 'gooses', 'good', 'goods', 'goodbye', 'goodwill'] else "Fail")
# When prefix do not exist 
print("Pass" if trie.autocomplete("s")==-1 else "Fail")
# When prefix do not exist 
print("Pass" if trie.autocomplete("dog")==-1 else "Fail")
# Empty string edge case  
print("Pass" if trie.autocomplete("")==['apple', 'bear', 'zebra', 'goo', 'gooses', 'good', 'goods', 'goodbye', 'goodwill'] else "Fail")

    
