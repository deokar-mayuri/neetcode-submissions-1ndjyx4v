class RandomizedSet:

    def __init__(self):
        self.hashmap = dict()
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.hashmap[val] = 1
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            self.hashmap.pop(val)
            self.size -= 1
            return True
        return False

    def getRandom(self) -> int:
        idx = random.randint(0, self.size - 1)
        return list(self.hashmap.keys())[idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()