class Compiler:

  def __init__(self):
    self.array = []

  def isOparand(self, el):
    return el.isalpha()

  def infixToPostfix(self, exp):
    for element in exp:
      if self.isOparand(element):
        print("hi")




compiler = Compiler()
compiler.infixToPostfix("123")