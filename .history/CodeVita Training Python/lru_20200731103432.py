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

  def put(self, key, value):
    self.memory[key] = value
    self.touch_key(key)
    if len(self.memory) > self.capacity