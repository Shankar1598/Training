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

  