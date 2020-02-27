class TrieNode:
    def __init__(self, handler = None):
        self.next = {}
        self.handler = handler

    def insert (self, small_path, handler = None):
        self.next[small_path] = TrieNode(handler)
    
class Trie:
    def __init__(self, root_handler = None):
        self.root = TrieNode(root_handler)
    
    def insert (self, path, handler):
        curr_node = self.root
        for node in path_arr:
            if node in curr_node.next:
                curr_node = curr_node.next[node]
                continue
            curr_node.next[node] = TrieNode()
        curr_node.handler = handler            
    
    def split_path(self, path):
        if path == "/":
            return []
        path_arr = path.split("/")
        path_arr.remove("")
        return path_arr
    
    def find(self, path_arr):
        if len(path_arr) == 0:
            return self.root.handler
        curr_node = self.root
        for node in path_arr:
            if node not in curr_node.next:
                return -1
            curr_node = curr_node.next[node]
        return curr_node.handler

class Router:
    def __init__(self):
        


trie = Trie("root handler")
trie.insertRoute("/abc/def/ghi", "handler1")
trie.insertRoute("/abc/def/ghi/jkl", "handler2")

print(trie.get_path_handler("/abc/def/ghi"))


