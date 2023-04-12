from Generated_files.MARVisitor import MARVisitor
from Generated_files.MARParser import MARParser
from antlr4 import *

#test

class MARCustomVisitor(MARVisitor):
    variables = {}

    def visitAssignment(self, ctx:MARParser.AssignmentContext):
        varName = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[varName] = value

    def visitConstant(self, ctx:MARParser.ConstantContext):
        if ctx.INTEGER() is not None:
            return int(ctx.INTEGER().getText())

        if ctx.FLOAT() is not None:
            return float(ctx.FLOAT().getText())

        if ctx.STRING() is not None:
            return ctx.STRING().getText()

        if ctx.BOOL() is not None:
            return bool(ctx.BOOL().getText())

        if ctx.NULL() is not None:
            return None


