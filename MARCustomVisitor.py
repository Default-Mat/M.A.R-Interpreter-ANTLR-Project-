import preset_functions
from Generated_files.MARVisitor import MARVisitor
from Generated_files.MARParser import MARParser
from antlr4 import *


class MARCustomVisitor(MARVisitor):
    variables = {}

    def __init__(self):
        self.should_break = False
        self.should_continue = False
        self.is_within_block = False
        self.variables["pi"] = 3.14
        self.variables["amirreza"] = 0

    def visitFunctionCall(self, ctx: MARParser.FunctionCallExpressionContext):
        identify = ctx.ID().getText()
        argument = []
        if ctx.expression():
            argument = [self.visit(expr) for expr in ctx.expression()]

        function = getattr(preset_functions, identify)
        function(*argument)

    def visitFunctionCallExpression(self, ctx: MARParser.FunctionCallExpressionContext):
        identify = ctx.functionCall().ID().getText()
        argument = []
        if ctx.functionCall().expression():
            argument = [self.visit(expr) for expr in ctx.functionCall().expression()]

        function = getattr(preset_functions, identify)
        return function(*argument)

    def visitAssignment(self, ctx: MARParser.AssignmentContext):
        varName = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[varName] = value
        return None

    def visitConstant(self, ctx: MARParser.ConstantContext):
        if ctx.INTEGER() is not None:
            return int(ctx.INTEGER().getText())

        if ctx.FLOAT() is not None:
            return float(ctx.FLOAT().getText())

        if ctx.STRING() is not None:
            return ctx.STRING().getText()

        if ctx.BOOL() is not None:
            if ctx.BOOL().getText() == "true":
                return True
            else:
                return False

        if ctx.NULL() is not None:
            return None

        raise Exception('Unknown value type')

    def visitIdentifierExpression(self, ctx: MARParser.IdentifierExpressionContext):
        varName = ctx.ID().getText()
        if varName not in self.variables:
            raise Exception(f'Variable "{varName}" is not defined')

        return self.variables[varName]

    def visitAddExpression(self, ctx: MARParser.AddExpressionContext):
        leftExp = self.visit(ctx.expression())
        rightExpt = self.visit(ctx.term())
        return self.__add(leftExp, rightExpt)

    def visitSubExpression(self, ctx:MARParser.SubExpressionContext):
        leftExp = self.visit(ctx.expression())
        rightExpt = self.visit(ctx.term())
        return self.__subtract(leftExp, rightExpt)

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

    def visitMulExpression(self, ctx:MARParser.MulExpressionContext):
        leftExp = self.visit(ctx.term())
        rightExp = self.visit(ctx.power())
        return self.__multy(leftExp, rightExp)

    def visitDivExpression(self, ctx:MARParser.DivExpressionContext):
        leftExp = self.visit(ctx.term())
        rightExp = self.visit(ctx.power())
        return self.__divied(leftExp, rightExp)

    def visitModExpression(self, ctx:MARParser.ModExpressionContext):
        leftExp = self.visit(ctx.term())
        rightExp = self.visit(ctx.power())
        return self.__modify(leftExp, rightExp)

    def __multy(self, left, right):
        if type(left) is int and type(right) is int:
            return left * right

        elif type(left) is float and type(right) is float:
            return left * right

        elif type(left) is float and type(right) is int:
            return left * right

        elif type(left) is int and type(right) is float:
            return left * right

        elif type(left) is str and type(right) is int:
            return left * right

        elif type(left) is int and type(right) is str:
            return left * right

        else:
            raise Exception(f'You cannot multiply {type(left)} and {type(right)} value types')

    def __divied(self, left, right):
        if type(left) is int and type(right) is int:
            return left / right

        elif type(left) is float and type(right) is float:
            return left / right

        elif type(left) is float and type(right) is int:
            return left / right

        elif type(left) is int and type(right) is float:
            return left / right

        else:
            raise Exception(f'You cannot divied {type(left)} and {type(right)} value types')

    def __modify(self, left, right):
        if type(left) is int and type(right) is int:
            return left % right

        elif type(left) is float and type(right) is int:
            return left % right

        elif type(left) is float and type(right) is float:
            return left % right

        elif type(left) is int and type(right) is float:
            return left % right

        else:
            raise Exception(f'You cannot modify {type(left)} and {type(right)} value types')

    def visitPowerExpression(self, ctx:MARParser.PowerExpressionContext):
        leftExp = self.visit(ctx.not_())
        rightExp = self.visit(ctx.power())
        return self.__pow(leftExp, rightExp)

    def __pow(self, left, right):
        if type(left) is int and type(right) is int:
            return left ** right

        elif type(left) is float and type(right) is int:
            return left ** right

        elif type(left) is float and type(right) is float:
            return left ** right

        elif type(left) is int and type(right) is float:
            return left ** right

        else:
            raise Exception(f'You cannot use power op on {type(left)} and {type(right)} value types')

    def visitParanthesesExpression(self, ctx:MARParser.ParanthesesExpressionContext):
        return self.visit(ctx.expression())

    def visitBoolExpression(self, ctx: MARParser.AddExpressionContext):
        leftExp = self.visit(ctx.expression(0))
        rightExp = self.visit(ctx.expression(1))
        op = ctx.boolOp().getText()

        if op == 'and':
            return self.__and(leftExp, rightExp)
        elif op == 'or':
            return self.__or(leftExp, rightExp)
        else:
            raise Exception(f'{op} is not a boolean Operation')

    def __and(self, left, right):
        if type(left) is int and type(right) is int:
            return right
        elif type(left) is float and type(right) is float:
            return right

        elif type(left) is float and type(right) is int:
            return right

        elif type(left) is int and type(right) is float:
            return right

        elif type(left) is bool and type(right) is bool:
            return left and right
        else:
            raise Exception(f'can not in and')

    def __or(self, left, right):
        if type(left) is int and type(right) is int:
            return left
        elif type(left) is float and type(right) is float:
            return left

        elif type(left) is float and type(right) is int:
            return left

        elif type(left) is int and type(right) is float:
            return right

        elif type(left) is bool and type(right) is bool:
            return left or right
        else:
            raise Exception(f'can not in or')

    def visitCompareExpression(self, ctx: MARParser.AddExpressionContext):
        leftExp = self.visit(ctx.expression(0))
        rightExp = self.visit(ctx.expression(1))
        op = ctx.compareOp().getText()

        if op == '<':
            return self.__Smaller(leftExp, rightExp)
        elif op == '>':
            return self.__Greater(leftExp, rightExp)
        elif op == '<=':
            return self.__SmallerEquals(leftExp, rightExp)
        elif op == '>=':
            return self.__GreaterEquals(leftExp, rightExp)
        elif op == '==':
            return self.__Equals(leftExp, rightExp)
        elif op == '!=':
            return self.__NotEquals(leftExp, rightExp)
        else:
            raise Exception(f'Operation {op} not define')

    def __Smaller(self, left, right):
        if type(left) is int and type(right) is int:
            return left < right

        elif type(left) is float and type(right) is float:
            return left < right

        elif type(left) is float and type(right) is int:
            return left < right

        elif type(left) is int and type(right) is float:
            return left < right
        else:
            raise Exception(f'you can not compare {type(left)} and {type(right)} value types')

    def __Greater(self, left, right):
        if type(left) is int and type(right) is int:
            return left > right

        elif type(left) is float and type(right) is float:
            return left > right

        elif type(left) is float and type(right) is int:
            return left > right

        elif type(left) is int and type(right) is float:
            return left > right

        else:
            raise Exception(f'you can not compare {type(left)} and {type(right)} value types')

    def __SmallerEquals(self, left, right):
        if type(left) is int and type(right) is int:
            return left <= right

        elif type(left) is float and type(right) is float:
            return left <= right

        elif type(left) is float and type(right) is int:
            return left <= right

        elif type(left) is int and type(right) is float:
            return left <= right

        else:
            raise Exception(f'you can not compare {type(left)} and {type(right)} value types')

    def __GreaterEquals(self, left, right):
        if type(left) is int and type(right) is int:
            return left >= right

        elif type(left) is float and type(right) is float:
            return left >= right

        elif type(left) is float and type(right) is int:
            return left >= right

        elif type(left) is int and type(right) is float:
            return left >= right

        else:
            raise Exception(f'you can not compare {type(left)} and {type(right)} value types')

    def __Equals(self, left, right):
        if type(left) is int and type(right) is int:
            return left == right

        elif type(left) is float and type(right) is float:
            return left == right

        elif type(left) is float and type(right) is int:
            return left == right

        elif type(left) is int and type(right) is float:
            return left == right

        else:
            raise Exception(f'you can not compare {type(left)} and {type(right)} value types')

    def __NotEquals(self, left, right):
        if type(left) is int and type(right) is int:
            return left != right

        elif type(left) is float and type(right) is float:
            return left != right

        elif type(left) is float and type(right) is int:
            return left != right

        elif type(left) is int and type(right) is float:
            return left != right

        else:
            raise Exception(f'you can not compare {type(left)} and {type(right)} value types')

    def visitIfBlock(self, ctx):
        conditionResult = self.visit(ctx.expression())
        evaluatedBlock = False

        if conditionResult:
            evaluatedBlock = True
            self.visit(ctx.block())
        else:
            elseIfBlock = ctx.elseIfBlock()
            if elseIfBlock is not None:
                elseIfResult = self.visit(elseIfBlock)
                if elseIfResult:
                    evaluatedBlock = True

            if not evaluatedBlock:
                elseBlock = ctx.elseBlock()
                if elseBlock is not None:
                    self.visit(elseBlock)

        return None

    def visitElseIfBlock(self, ctx):
        conditionResult = self.visit(ctx.expression())
        evaluatedBlock = False

        if conditionResult:
            evaluatedBlock = True
            self.visit(ctx.block())
        else:
            elseIfBlock = ctx.elseIfBlock()
            if elseIfBlock is not None:
                elseIfResult = self.visit(elseIfBlock)
                if elseIfResult:
                    evaluatedBlock = True

            if not evaluatedBlock:
                elseBlock = ctx.elseBlock()
                if elseBlock is not None:
                    self.visit(elseBlock)

        return True if evaluatedBlock else False

    def visitElseBlock(self, ctx):
        self.visit(ctx.block())
        return True

    # whileBlock
    def visitWhileBlock(self, ctx: MARParser.WhileBlockContext):
        while self.visit(ctx.expression()):
            self.visit(ctx.block())

