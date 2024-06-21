class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    def _hash(self, key):
        return hash(key) % self.size
    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            self.table[index].append((key, value))
    def delete(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for i, (existing_key, existing_value) in enumerate(self.table[index]):
                if existing_key == key:
                    del self.table[index][i]
                    break
    def search(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for existing_key, existing_value in self.table[index]:
                if existing_key == key:
                    return existing_value
        return None
hash_table = HashTable(10)
hash_table.insert("bike", 20)
hash_table.insert("car", 30)
hash_table.insert("aeroplane", 40)
print("Search 'car':", hash_table.search("car"))
print("Search 'bike':", hash_table.search("bike"))
hash_table.delete("car")
print("Search 'car' after deletion:", hash_table.search("car"))