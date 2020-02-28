class TrieNode:
    def __init__(self, handler = None):
        self.next = {}
        self.handler = handler

    def insert (self, small_path, handler = None):
        self.next[small_path] = TrieNode(handler)
    
class Trie:
    def __init__(self, root_handler = None):
        self.root = TrieNode(root_handler)
    
    def insert (self, path_arr, handler):
        curr_node = self.root
        for node in path_arr:
            if node not in curr_node.next:
                curr_node.next[node] = TrieNode()

            curr_node = curr_node.next[node]
        curr_node.handler = handler            
    
    def find(self, path_arr):
        if len(path_arr) == 0:
            return self.root.handler
        curr_node = self.root
        for node in path_arr:
            if node not in curr_node.next:
                return None
            curr_node = curr_node.next[node]
        return curr_node.handler

class Router:
    def __init__(self, root_handler, not_found_handler):
        self.trie = Trie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler( self, path, handler):
        path_arr = self.split_path(path)
        self.trie.insert(path_arr, handler)
    
    def lookup(self, path):
        path_arr = self.split_path(path)
        node_handler = self.trie.find(path_arr)
        if node_handler:
            return node_handler
        else:
            return self.not_found_handler

    def split_path(self, path):
        if path == "/":
            return []
        path_arr = path.split("/")
        path_arr.remove("")
        return path_arr
        
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")

print("Pass" if router.lookup("/") == "root handler" else "Fail")
print("Pass" if router.lookup("/home") == "not found handler" else "Fail")
print("Pass" if router.lookup("/home/about") == "about handler" else "Fail")
print("Pass" if router.lookup("/home/about/") == "not found handler" else "Fail") 
print("Pass" if router.lookup("/home/about/me") == "not found handler" else "Fail") 

