class Compiler:

  def isOparand(self, el):
    el.isalpha()

  def infixToPostfix(self, exp):
    for element in exp:
      if self.isOparand(element):
        print("hi")




compiler = Compiler()
compiler.infixToPostfix("123")