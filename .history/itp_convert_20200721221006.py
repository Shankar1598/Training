class Compiler:
  def infixToPostfix(self, exp):
    for element in exp:
      print(element)

compiler = Compiler()
compiler.infixToPostfix("123")