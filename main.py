from antlr4 import *
from Generated_files.MARParser import MARParser
from Generated_files.MARLexer import MARLexer
from MARCustomVisitor import MARCustomVisitor

file = FileStream('sourceCode.txt')
lexer = MARLexer(file)
stream = CommonTokenStream(lexer)
parser = MARParser(stream)
tree = parser.program()
visitor = MARCustomVisitor()
visitor.visit(tree)

