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
            return self.__add(leftExp, rightExpt)

        if op == '-':
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

    def visitMulExpression(self, ctx:MARParser.AddExpressionContext):
        leftExp = self.visit(ctx.expression(0))
        rightExp = self.visit(ctx.expression(1))
        op = ctx.mulOp().getText()

        if op == '*':
            return self.__multy(leftExp, rightExp)
        elif op == '/':
            return self.__divied(leftExp, rightExp)
        elif op == '%':
            return self.__modify(leftExp, rightExp)
        else:
            raise Exception(f'Operation {op} not define')
        
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

        
    def visitCompareOp(self, ctx: MARParser.AddExpressionContext):
        leftExp = self.visit(ctx.expression(0))
        rightExp = self.visit(ctx.expression(1))
        op = ctx.compareOp().getText()

        if op == '<':
            return self.__Smaller(leftExp, rightExp)
        elif op == '>':
            return self.__Bigger(leftExp, rightExp)
        elif op == '<=':
            return self.__SmallerEquals(leftExp, rightExp) 
        elif op == '>=':
            return self.__GreaterEquals(leftExp, rightExp)
        elif op == '==':
            return self.__Equals(leftExp, rightExp)
        elif op == '!=':
            return self.__NotEquals(rightExp, rightExp)
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
    
    def __Bigger(self, left, right):
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