# Generated from MAR.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MARParser import MARParser
else:
    from MARParser import MARParser

# This class defines a complete listener for a parse tree produced by MARParser.
class MARListener(ParseTreeListener):

    # Enter a parse tree produced by MARParser#program.
    def enterProgram(self, ctx:MARParser.ProgramContext):
        pass

    # Exit a parse tree produced by MARParser#program.
    def exitProgram(self, ctx:MARParser.ProgramContext):
        pass


    # Enter a parse tree produced by MARParser#line.
    def enterLine(self, ctx:MARParser.LineContext):
        pass

    # Exit a parse tree produced by MARParser#line.
    def exitLine(self, ctx:MARParser.LineContext):
        pass


    # Enter a parse tree produced by MARParser#ifBlock.
    def enterIfBlock(self, ctx:MARParser.IfBlockContext):
        pass

    # Exit a parse tree produced by MARParser#ifBlock.
    def exitIfBlock(self, ctx:MARParser.IfBlockContext):
        pass


    # Enter a parse tree produced by MARParser#whileBlock.
    def enterWhileBlock(self, ctx:MARParser.WhileBlockContext):
        pass

    # Exit a parse tree produced by MARParser#whileBlock.
    def exitWhileBlock(self, ctx:MARParser.WhileBlockContext):
        pass


    # Enter a parse tree produced by MARParser#statement.
    def enterStatement(self, ctx:MARParser.StatementContext):
        pass

    # Exit a parse tree produced by MARParser#statement.
    def exitStatement(self, ctx:MARParser.StatementContext):
        pass


    # Enter a parse tree produced by MARParser#assignment.
    def enterAssignment(self, ctx:MARParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MARParser#assignment.
    def exitAssignment(self, ctx:MARParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MARParser#functionCall.
    def enterFunctionCall(self, ctx:MARParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by MARParser#functionCall.
    def exitFunctionCall(self, ctx:MARParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by MARParser#compareExpression.
    def enterCompareExpression(self, ctx:MARParser.CompareExpressionContext):
        pass

    # Exit a parse tree produced by MARParser#compareExpression.
    def exitCompareExpression(self, ctx:MARParser.CompareExpressionContext):
        pass


    # Enter a parse tree produced by MARParser#parenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:MARParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by MARParser#parenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:MARParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by MARParser#constantExpression.
    def enterConstantExpression(self, ctx:MARParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by MARParser#constantExpression.
    def exitConstantExpression(self, ctx:MARParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by MARParser#addExpression.
    def enterAddExpression(self, ctx:MARParser.AddExpressionContext):
        pass

    # Exit a parse tree produced by MARParser#addExpression.
    def exitAddExpression(self, ctx:MARParser.AddExpressionContext):
        pass


    # Enter a parse tree produced by MARParser#boolExpression.
    def enterBoolExpression(self, ctx:MARParser.BoolExpressionContext):
        pass

    # Exit a parse tree produced by MARParser#boolExpression.
    def exitBoolExpression(self, ctx:MARParser.BoolExpressionContext):
        pass


    # Enter a parse tree produced by MARParser#identifierExpression.
    def enterIdentifierExpression(self, ctx:MARParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by MARParser#identifierExpression.
    def exitIdentifierExpression(self, ctx:MARParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by MARParser#functionCallExpression.
    def enterFunctionCallExpression(self, ctx:MARParser.FunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by MARParser#functionCallExpression.
    def exitFunctionCallExpression(self, ctx:MARParser.FunctionCallExpressionContext):
        pass


    # Enter a parse tree produced by MARParser#notExpression.
    def enterNotExpression(self, ctx:MARParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by MARParser#notExpression.
    def exitNotExpression(self, ctx:MARParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by MARParser#mulExpression.
    def enterMulExpression(self, ctx:MARParser.MulExpressionContext):
        pass

    # Exit a parse tree produced by MARParser#mulExpression.
    def exitMulExpression(self, ctx:MARParser.MulExpressionContext):
        pass


    # Enter a parse tree produced by MARParser#constant.
    def enterConstant(self, ctx:MARParser.ConstantContext):
        pass

    # Exit a parse tree produced by MARParser#constant.
    def exitConstant(self, ctx:MARParser.ConstantContext):
        pass


    # Enter a parse tree produced by MARParser#mulOp.
    def enterMulOp(self, ctx:MARParser.MulOpContext):
        pass

    # Exit a parse tree produced by MARParser#mulOp.
    def exitMulOp(self, ctx:MARParser.MulOpContext):
        pass


    # Enter a parse tree produced by MARParser#addOp.
    def enterAddOp(self, ctx:MARParser.AddOpContext):
        pass

    # Exit a parse tree produced by MARParser#addOp.
    def exitAddOp(self, ctx:MARParser.AddOpContext):
        pass


    # Enter a parse tree produced by MARParser#compareOp.
    def enterCompareOp(self, ctx:MARParser.CompareOpContext):
        pass

    # Exit a parse tree produced by MARParser#compareOp.
    def exitCompareOp(self, ctx:MARParser.CompareOpContext):
        pass


    # Enter a parse tree produced by MARParser#boolOp.
    def enterBoolOp(self, ctx:MARParser.BoolOpContext):
        pass

    # Exit a parse tree produced by MARParser#boolOp.
    def exitBoolOp(self, ctx:MARParser.BoolOpContext):
        pass


    # Enter a parse tree produced by MARParser#block.
    def enterBlock(self, ctx:MARParser.BlockContext):
        pass

    # Exit a parse tree produced by MARParser#block.
    def exitBlock(self, ctx:MARParser.BlockContext):
        pass



del MARParser