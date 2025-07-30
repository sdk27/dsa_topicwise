class Hashmap:
    def __init__(self):
        self.hash = [None] * 10

    def put(self, key):
        hash_value = key % 10
        self.hash[hash_value] = key

    def get(self, key):
        index = key % 10
        value = self.hash[index]
        return value

    def remove(self, key):
        self.hash[key % 10] = None

    def display(self):
        print(self.hash)


h = Hashmap()
h.put(8)
h.put(1)
h.put(4)
h.put(9)
h.put(2)
h.display()
h.remove(4)
h.display()
value = h.get(9)
print(value)
