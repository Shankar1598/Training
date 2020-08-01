class LRUMemory:
  def __init__(self, capacity):
    self.capacity = capacity
    self.memory = {}
    self.touch = {}
    self.touch_count = 0
    self.full = False

  def get(self, key):
    if key not in self.memory:
      return -1
    self.touch_key(key)
    return self.memory[key]

  def touch_key(self, key):
    self.touch[key] = self.touch_count
    self.touch_count += 1

  # O(1) and not in O(n)
  def put(self, key, value):
    not_found = key not in self.memory
    self.memory[key] = value
    self.touch_key(key)
    if not_found and self.full:
      self.delete_lru()
    elif not_found:
      self.full = len(self.memory) > self.capacity
      if self.full:
        self.delete_lru()

  def delete_lru(self):
    key = self.lru_key()
    self.memory.pop(key)
    self.touch.pop(key)
    
  def lru_key(self):
    k = list(self.touch.keys())[0]
    # touch -> { 1: 5, 3: 57, 2: 26, 7:0 }
    lru = [k, self.touch[k]]
    # lru = [1, 5]
    for key in self.touch:
      val = self.touch[key]
      if val < lru[1]:
        lru = [key, val]
    return lru[0]


ram = LRUMemory(2)
ram.put(1, "hi")
ram.put(2, "hey")
print(ram.get(1))       # returns 1
ram.put(3, "bye")    # evicts key 2
print(ram.get(2))       # returns -1 (not found)
ram.put(4, 4)    # evicts key 1
print(ram.get(1))       # returns -1 (not found)
print(ram.get(3))       # returns 3
print(ram.get(4))       # returns 4
