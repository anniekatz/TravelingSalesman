# Manual Hash Table implementation

class HashTable:
    # Constructor for hash table class
    # Initializes hash table with an optional parameter for capacity
    def __init__(self, capacity=40):
        self.table = []
        for i in range(capacity):
            self.table.append([])

    # Use hash function to get key (bucket)
    def hash_func(self, key):
        hash_bucket = int(key) % len(self.table)
        return hash_bucket

    # Insert method for hash table class
    # Insert new package
    def insert(self, key, val):
        hash_key = self.hash_func(key)
        kv_pair = [key, val]

        if self.table[hash_key] is None:
            self.table[hash_key] = list([kv_pair])
            return True
        else:
            for kv in self.table[hash_key]:
                if kv[0] == key:
                    kv[1] = val
                    return True
            self.table[hash_key].append(kv_pair)
            return True

    # Update method for hash table class
    # Update existing package
    def update(self, key, val):
        hash_key = self.hash_func(key)
        if self.table[hash_key] is not None:
            for kv in self.table[hash_key]:
                if kv[0] == key:
                    kv[1] = val
                    return True
        else:
            print('Error updating packages. Key: ' + key)

    # Delete method for hash table class
    # Delete existing package
    def delete(self, key):
        hash_key = self.hash_func(key)
        if self.table[hash_key] is None:
            print('Key ' + key + ' not found')
            return False
        for kv in range(0, len(self.table[hash_key])):
            if self.table[hash_key][kv][0] == key:
                self.table[hash_key].pop(kv)
                return True

    # Lookup method for hash table class
    # Lookup existing package
    def search(self, key):
        hash_key = self.hash_func(key)
        if self.table[hash_key]:
            for kv in self.table[hash_key]:
                if kv[0] == key:
                    return kv[1]
        return None

    def __str__(self):
        # return hash table as string
        return str(self.table)
