from Generated_files.MARVisitor import MARVisitor
from Generated_files.MARParser import MARParser
from antlr4 import *


class MARCustomVisitor(MARVisitor):
    variables = {}

    def visitLine(self, ctx: MARParser.LineContext):
        if ctx.marStatement() is not None:
            self.visitMarStatement(ctx.marStatement())

        elif ctx.statement() is not None:
            self.visitStatement(ctx.statement())

        elif ctx.ifBlock() is not None:
            self.visitIfBlock(ctx.ifBlock())

        elif ctx.whileBlock() is not None:
            self.visitWhileBlock(ctx.whileBlock())

    def visitMarStatement(self, ctx: MARParser.MarStatementContext):
        print("MAR: Matin Meskinnavaz, Amirreza Mehrabani, Reza Tahmasbi")

    def visitAssignment(self, ctx: MARParser.AssignmentContext):
        varName = ctx.ID().getText()
        value = self.visit(ctx.expression())
        print(value)
        self.variables[varName] = value

    def visitConstant(self, ctx: MARParser.ConstantContext):
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

    def visitIdentifierExpression(self, ctx: MARParser.IdentifierExpressionContext):
        varName = ctx.ID().getText()
        if varName not in self.variables:
            raise Exception(f'Variable "{varName}" is not defined')

        return self.variables[varName]

    def visitAddExpression(self, ctx: MARParser.AddExpressionContext):
        leftExp = self.visit(ctx.expression(0))
        rightExp = self.visit(ctx.expression(1))
        op = ctx.addOp().getText()
        if op == '+':
            return self.__add(leftExp, rightExp)

        if op == '-':
            return self.__subtract(leftExp, rightExp)

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

    def __subtract(self, left, right):
        if type(left) is int and type(right) is int:
            return left - right

        elif type(left) is float and type(right) is float:
            return left - right

        elif type(left) is float and type(right) is int:
            return left - right

        elif type(left) is int and type(right) is float:
            return left - right

        else:
            raise Exception(f'You cannot subtract {type(left)} and {type(right)} value types')

    # ifBlock
    def visitIfBlock(self, ctx: MARParser.IfBlockContext):
        if self.visit(ctx.expression()):
            self.visit(ctx.block())
            return
        elif ctx.elseIfBlock() is not None:
            for i in range(len(ctx.elseIfBlock())):
                if self.visit(ctx.elseIfBlock(i).expression()):
                    self.visit(ctx.elseIfBlock(i).block())
                    return
            if ctx.elseBlock() is not None:
                self.visit(ctx.elseBlock().block())

    # whileBlock
    def visitWhileBlock(self, ctx: MARParser.WhileBlockContext):
        while True:
            if not self.visit(ctx.expression()):
                break
            try:
                self.visit(ctx.block())
            except ContinueException:
                continue
            except BreakException:
                break

    # while block breaker
    def visitBreakStatement(self, ctx: MARParser.BreakStatementContext):
        return 'break'

    def visitContinueStatement(self, ctx: MARParser.ContinueStatementContext):
        return 'continue'

    # check if we are visiting an statement or an if-block
#     def visitLine(self, ctx:MARParser.LineContext):
#         if ctx.statement() is not None:
#             return self.visit(ctx.statement())
#         elif ctx.ifBlock() is not None:
#             return self.visit(ctx.ifBlock())
#         elif ctx.whileBlock() is not None:
#             self.visit(ctx.whileBlock())
