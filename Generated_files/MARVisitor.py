# Generated from MAR.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MARParser import MARParser
else:
    from MARParser import MARParser

# This class defines a complete generic visitor for a parse tree produced by MARParser.

class MARVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MARParser#program.
    def visitProgram(self, ctx:MARParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#line.
    def visitLine(self, ctx:MARParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#ifBlock.
    def visitIfBlock(self, ctx:MARParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#whileBlock.
    def visitWhileBlock(self, ctx:MARParser.WhileBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#statement.
    def visitStatement(self, ctx:MARParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#assignment.
    def visitAssignment(self, ctx:MARParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#functionCall.
    def visitFunctionCall(self, ctx:MARParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#compareExpression.
    def visitCompareExpression(self, ctx:MARParser.CompareExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#parenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:MARParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#constantExpression.
    def visitConstantExpression(self, ctx:MARParser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#addExpression.
    def visitAddExpression(self, ctx:MARParser.AddExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#boolExpression.
    def visitBoolExpression(self, ctx:MARParser.BoolExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:MARParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx:MARParser.FunctionCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#notExpression.
    def visitNotExpression(self, ctx:MARParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#mulExpression.
    def visitMulExpression(self, ctx:MARParser.MulExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#constant.
    def visitConstant(self, ctx:MARParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#mulOp.
    def visitMulOp(self, ctx:MARParser.MulOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#addOp.
    def visitAddOp(self, ctx:MARParser.AddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#compareOp.
    def visitCompareOp(self, ctx:MARParser.CompareOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#boolOp.
    def visitBoolOp(self, ctx:MARParser.BoolOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MARParser#block.
    def visitBlock(self, ctx:MARParser.BlockContext):
        return self.visitChildren(ctx)



del MARParser