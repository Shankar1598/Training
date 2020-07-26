class Compiler:

  def __init__(self):
    self.array = []
    self.output = []
    self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    self.memory = {'a': 2, 'b': 5, 'c': 1, 'd': 7, 'e': 4, 'f': 9}

  # operand or not? (a,b,c)
  def isOparand(self, el):
    return el.isalpha()

  def push(self, el):
    self.array.append(el)

  def isEmpty(self):
    return len(self.array) == 0

  def peak(self):
    return self.array[-1]
    # if self.isEmpty():
    #   return "$"
    # else:
    #   return self.array[-1]

  def pop(self):
    if self.isEmpty():
      return "$"
    else:
      return self.array.pop()

  def notGreater(self, el):
    try:
      return self.precedence[el] <= self.precedence[self.peak()]
    except KeyError:
      return False

  def clear(self):
    self.array = []
    self.output = []


  def getPostfix(self, exp):
    self.clear()
    for element in exp:
      if self.isOparand(element):
        self.output.append(element)
      elif element == '(':
        self.push(element)
      elif element == ')':
        while (not self.isEmpty() and self.peak() != '('):
          self.output.append(self.pop())
        if (self.isEmpty() or self.peak() != '('):
          # error
          print("error")
          return None
        else:
          self.pop()
      else:
        # operator
        while(not self.isEmpty() and self.notGreater(element)):
          self.output.append(self.pop())
        self.push(element)
    
    while not self.isEmpty():
      self.output.append(self.pop())

    print("".join(self.output) )
    return self.output

  def evaluate(self, exp):
    self.clear()



exp = "a+b*(c*d-e)-f"
c=Compiler()
c.getPostfix(exp)
