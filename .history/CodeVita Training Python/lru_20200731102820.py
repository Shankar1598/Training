class LRUMemory:
  def __init__(self, capacity):
    self.capacity = capacity
    # 3
    # 3 items
    self.memory = {}
    self.touch = {}
    self.touch_count = 0
    self.full = False

  