class Compiler:
  def infixToPostfix(self, exp):
    for element in exp:
      if self.isOparand(element)



compiler = Compiler()
compiler.infixToPostfix("123")