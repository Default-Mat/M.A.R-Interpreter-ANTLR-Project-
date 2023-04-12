from Generated_files.MARVisitor import MARVisitor
from Generated_files.MARParser import MARParser
from antlr4 import *


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

        raise Exception('Unknown value type')

    def visitIdentifierExpression(self, ctx:MARParser.IdentifierExpressionContext):
        varName = ctx.ID().getText()
        if varName not in self.variables:
            raise Exception(f'Variable "{varName}" is not defined')

        return self.variables[varName]

    def visitAddExpression(self, ctx:MARParser.AddExpressionContext):
        leftExp = self.visit(ctx.expression(0))
        rightExpt = self.visit(ctx.expression(1))
        op = ctx.addOp().getText()
        if op == '+':
            self.__add(leftExp, rightExpt)

    def __add(self, left, right):
        if type(left) is int and type(right) is int:
            return left + right

        elif type(left) is float and type(right) is float:
            return left + right

        elif type(left) is float and type(right) is int:
            return left + right

        elif type(left) is int and type(right) is float:
            return left + right

        elif type(left) is str and type(right) is str:
            return f'{left}{right}'

        else:
            raise Exception(f'You cannot add {type(left)} and {type(right)} value types')