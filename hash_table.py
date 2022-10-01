# Manual Hash Table implementation

class HashTable:
    def __init__(self):
        self.size = 40
        self.hash_table = [[] for i in range(self.size)]