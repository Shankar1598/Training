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

  def getValue(self, variable):
    return self.memory[variable]

  def popAndEval(self, op):
    val1 = self.pop()
    val2 = self.pop()
    print(val1, val2)
    self.push(str(eval(val1 + op + val2)))


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

    return "".join(self.output)

  def evaluate(self, exp):
    self.clear()
    for element in exp:
      if element.isdigit():
        self.push(element)
      elif element.isalpha():
        print(self.getValue(element))
        self.push(self.getValue(element))
      else:
        # operator
        self.popAndEval(element)
    
    return int(self.pop())



c=Compiler()
exp = "a+b*(c*d-e)-f"
postfix = c.getPostfix(exp)
print(postfix)

exp = "2563*7-*+2-"
print(c.evaluate(postfix))


# Assignment:
# Optimize the isEmpty method, bring support to multi-digit numbers and get int values from variables in memory