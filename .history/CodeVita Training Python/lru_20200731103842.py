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

    