class Compiler:

  def isOparand(self):
    

  def infixToPostfix(self, exp):
    for element in exp:
      if self.isOparand(element):
        print("hi")




compiler = Compiler()
compiler.infixToPostfix("123")