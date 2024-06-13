# Generated from calculadora.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .calculadoraParser import calculadoraParser
else:
    from calculadoraParser import calculadoraParser

# This class defines a complete generic visitor for a parse tree produced by calculadoraParser.

class calculadoraVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by calculadoraParser#prog.
    def visitProg(self, ctx:calculadoraParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#printExpr.
    def visitPrintExpr(self, ctx:calculadoraParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#assign.
    def visitAssign(self, ctx:calculadoraParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#forStat.
    def visitForStat(self, ctx:calculadoraParser.ForStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#ifStat.
    def visitIfStat(self, ctx:calculadoraParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#whileStat.
    def visitWhileStat(self, ctx:calculadoraParser.WhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#print.
    def visitPrint(self, ctx:calculadoraParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#functionDef.
    def visitFunctionDef(self, ctx:calculadoraParser.FunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#functionCall.
    def visitFunctionCall(self, ctx:calculadoraParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#blank.
    def visitBlank(self, ctx:calculadoraParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#params.
    def visitParams(self, ctx:calculadoraParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#crearCsv.
    def visitCrearCsv(self, ctx:calculadoraParser.CrearCsvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#getDictKey.
    def visitGetDictKey(self, ctx:calculadoraParser.GetDictKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#parens.
    def visitParens(self, ctx:calculadoraParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#openFile.
    def visitOpenFile(self, ctx:calculadoraParser.OpenFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#graficaBarras.
    def visitGraficaBarras(self, ctx:calculadoraParser.GraficaBarrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#dataframeMean.
    def visitDataframeMean(self, ctx:calculadoraParser.DataframeMeanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#listIndex.
    def visitListIndex(self, ctx:calculadoraParser.ListIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#listAppend.
    def visitListAppend(self, ctx:calculadoraParser.ListAppendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#unary.
    def visitUnary(self, ctx:calculadoraParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#listPop.
    def visitListPop(self, ctx:calculadoraParser.ListPopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#float.
    def visitFloat(self, ctx:calculadoraParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#graficaPuntos.
    def visitGraficaPuntos(self, ctx:calculadoraParser.GraficaPuntosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#dataframeSeries.
    def visitDataframeSeries(self, ctx:calculadoraParser.DataframeSeriesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#id.
    def visitId(self, ctx:calculadoraParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#dictExpr.
    def visitDictExpr(self, ctx:calculadoraParser.DictExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#listExpr.
    def visitListExpr(self, ctx:calculadoraParser.ListExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#tanFunction.
    def visitTanFunction(self, ctx:calculadoraParser.TanFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#closeFile.
    def visitCloseFile(self, ctx:calculadoraParser.CloseFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#comparison.
    def visitComparison(self, ctx:calculadoraParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#Root.
    def visitRoot(self, ctx:calculadoraParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#dataframeDescribe.
    def visitDataframeDescribe(self, ctx:calculadoraParser.DataframeDescribeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#sinFunction.
    def visitSinFunction(self, ctx:calculadoraParser.SinFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#bool.
    def visitBool(self, ctx:calculadoraParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#string.
    def visitString(self, ctx:calculadoraParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#MulDiv.
    def visitMulDiv(self, ctx:calculadoraParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#factorial.
    def visitFactorial(self, ctx:calculadoraParser.FactorialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#negacion.
    def visitNegacion(self, ctx:calculadoraParser.NegacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#increment.
    def visitIncrement(self, ctx:calculadoraParser.IncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#getDictValue.
    def visitGetDictValue(self, ctx:calculadoraParser.GetDictValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#cosFunction.
    def visitCosFunction(self, ctx:calculadoraParser.CosFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#listLen.
    def visitListLen(self, ctx:calculadoraParser.ListLenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#removeDictEntry.
    def visitRemoveDictEntry(self, ctx:calculadoraParser.RemoveDictEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#writeFile.
    def visitWriteFile(self, ctx:calculadoraParser.WriteFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#graficaCaja.
    def visitGraficaCaja(self, ctx:calculadoraParser.GraficaCajaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#deleteFile.
    def visitDeleteFile(self, ctx:calculadoraParser.DeleteFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#addDictEntry.
    def visitAddDictEntry(self, ctx:calculadoraParser.AddDictEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#Mod.
    def visitMod(self, ctx:calculadoraParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#repetida.
    def visitRepetida(self, ctx:calculadoraParser.RepetidaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#AddSub.
    def visitAddSub(self, ctx:calculadoraParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#dataframeHead.
    def visitDataframeHead(self, ctx:calculadoraParser.DataframeHeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#euclidesFunction.
    def visitEuclidesFunction(self, ctx:calculadoraParser.EuclidesFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#int.
    def visitInt(self, ctx:calculadoraParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#graficaHistograma.
    def visitGraficaHistograma(self, ctx:calculadoraParser.GraficaHistogramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#dataframeExpr.
    def visitDataframeExpr(self, ctx:calculadoraParser.DataframeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#inverseExpr.
    def visitInverseExpr(self, ctx:calculadoraParser.InverseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#listRemove.
    def visitListRemove(self, ctx:calculadoraParser.ListRemoveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#readFile.
    def visitReadFile(self, ctx:calculadoraParser.ReadFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#decrement.
    def visitDecrement(self, ctx:calculadoraParser.DecrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#graficaLineas.
    def visitGraficaLineas(self, ctx:calculadoraParser.GraficaLineasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#matrixExpr.
    def visitMatrixExpr(self, ctx:calculadoraParser.MatrixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#tupleExpr.
    def visitTupleExpr(self, ctx:calculadoraParser.TupleExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#writelinesFile.
    def visitWritelinesFile(self, ctx:calculadoraParser.WritelinesFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#transposeExpr.
    def visitTransposeExpr(self, ctx:calculadoraParser.TransposeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#leerCsv.
    def visitLeerCsv(self, ctx:calculadoraParser.LeerCsvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#return.
    def visitReturn(self, ctx:calculadoraParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#Power.
    def visitPower(self, ctx:calculadoraParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#matrix.
    def visitMatrix(self, ctx:calculadoraParser.MatrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#matrix_contents.
    def visitMatrix_contents(self, ctx:calculadoraParser.Matrix_contentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#row.
    def visitRow(self, ctx:calculadoraParser.RowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#list.
    def visitList(self, ctx:calculadoraParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#tupla.
    def visitTupla(self, ctx:calculadoraParser.TuplaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#list_contents.
    def visitList_contents(self, ctx:calculadoraParser.List_contentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#dicti.
    def visitDicti(self, ctx:calculadoraParser.DictiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#dict_contents.
    def visitDict_contents(self, ctx:calculadoraParser.Dict_contentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#dict_access.
    def visitDict_access(self, ctx:calculadoraParser.Dict_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#dict_entry.
    def visitDict_entry(self, ctx:calculadoraParser.Dict_entryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#dataframe.
    def visitDataframe(self, ctx:calculadoraParser.DataframeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#args.
    def visitArgs(self, ctx:calculadoraParser.ArgsContext):
        return self.visitChildren(ctx)



del calculadoraParser