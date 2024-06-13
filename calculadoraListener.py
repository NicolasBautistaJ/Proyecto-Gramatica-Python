# Generated from calculadora.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .calculadoraParser import calculadoraParser
else:
    from calculadoraParser import calculadoraParser

# This class defines a complete listener for a parse tree produced by calculadoraParser.
class calculadoraListener(ParseTreeListener):

    # Enter a parse tree produced by calculadoraParser#prog.
    def enterProg(self, ctx:calculadoraParser.ProgContext):
        pass

    # Exit a parse tree produced by calculadoraParser#prog.
    def exitProg(self, ctx:calculadoraParser.ProgContext):
        pass


    # Enter a parse tree produced by calculadoraParser#printExpr.
    def enterPrintExpr(self, ctx:calculadoraParser.PrintExprContext):
        pass

    # Exit a parse tree produced by calculadoraParser#printExpr.
    def exitPrintExpr(self, ctx:calculadoraParser.PrintExprContext):
        pass


    # Enter a parse tree produced by calculadoraParser#assign.
    def enterAssign(self, ctx:calculadoraParser.AssignContext):
        pass

    # Exit a parse tree produced by calculadoraParser#assign.
    def exitAssign(self, ctx:calculadoraParser.AssignContext):
        pass


    # Enter a parse tree produced by calculadoraParser#forStat.
    def enterForStat(self, ctx:calculadoraParser.ForStatContext):
        pass

    # Exit a parse tree produced by calculadoraParser#forStat.
    def exitForStat(self, ctx:calculadoraParser.ForStatContext):
        pass


    # Enter a parse tree produced by calculadoraParser#ifStat.
    def enterIfStat(self, ctx:calculadoraParser.IfStatContext):
        pass

    # Exit a parse tree produced by calculadoraParser#ifStat.
    def exitIfStat(self, ctx:calculadoraParser.IfStatContext):
        pass


    # Enter a parse tree produced by calculadoraParser#whileStat.
    def enterWhileStat(self, ctx:calculadoraParser.WhileStatContext):
        pass

    # Exit a parse tree produced by calculadoraParser#whileStat.
    def exitWhileStat(self, ctx:calculadoraParser.WhileStatContext):
        pass


    # Enter a parse tree produced by calculadoraParser#print.
    def enterPrint(self, ctx:calculadoraParser.PrintContext):
        pass

    # Exit a parse tree produced by calculadoraParser#print.
    def exitPrint(self, ctx:calculadoraParser.PrintContext):
        pass


    # Enter a parse tree produced by calculadoraParser#functionDef.
    def enterFunctionDef(self, ctx:calculadoraParser.FunctionDefContext):
        pass

    # Exit a parse tree produced by calculadoraParser#functionDef.
    def exitFunctionDef(self, ctx:calculadoraParser.FunctionDefContext):
        pass


    # Enter a parse tree produced by calculadoraParser#functionCall.
    def enterFunctionCall(self, ctx:calculadoraParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by calculadoraParser#functionCall.
    def exitFunctionCall(self, ctx:calculadoraParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by calculadoraParser#blank.
    def enterBlank(self, ctx:calculadoraParser.BlankContext):
        pass

    # Exit a parse tree produced by calculadoraParser#blank.
    def exitBlank(self, ctx:calculadoraParser.BlankContext):
        pass


    # Enter a parse tree produced by calculadoraParser#params.
    def enterParams(self, ctx:calculadoraParser.ParamsContext):
        pass

    # Exit a parse tree produced by calculadoraParser#params.
    def exitParams(self, ctx:calculadoraParser.ParamsContext):
        pass


    # Enter a parse tree produced by calculadoraParser#crearCsv.
    def enterCrearCsv(self, ctx:calculadoraParser.CrearCsvContext):
        pass

    # Exit a parse tree produced by calculadoraParser#crearCsv.
    def exitCrearCsv(self, ctx:calculadoraParser.CrearCsvContext):
        pass


    # Enter a parse tree produced by calculadoraParser#getDictKey.
    def enterGetDictKey(self, ctx:calculadoraParser.GetDictKeyContext):
        pass

    # Exit a parse tree produced by calculadoraParser#getDictKey.
    def exitGetDictKey(self, ctx:calculadoraParser.GetDictKeyContext):
        pass


    # Enter a parse tree produced by calculadoraParser#parens.
    def enterParens(self, ctx:calculadoraParser.ParensContext):
        pass

    # Exit a parse tree produced by calculadoraParser#parens.
    def exitParens(self, ctx:calculadoraParser.ParensContext):
        pass


    # Enter a parse tree produced by calculadoraParser#openFile.
    def enterOpenFile(self, ctx:calculadoraParser.OpenFileContext):
        pass

    # Exit a parse tree produced by calculadoraParser#openFile.
    def exitOpenFile(self, ctx:calculadoraParser.OpenFileContext):
        pass


    # Enter a parse tree produced by calculadoraParser#graficaBarras.
    def enterGraficaBarras(self, ctx:calculadoraParser.GraficaBarrasContext):
        pass

    # Exit a parse tree produced by calculadoraParser#graficaBarras.
    def exitGraficaBarras(self, ctx:calculadoraParser.GraficaBarrasContext):
        pass


    # Enter a parse tree produced by calculadoraParser#dataframeMean.
    def enterDataframeMean(self, ctx:calculadoraParser.DataframeMeanContext):
        pass

    # Exit a parse tree produced by calculadoraParser#dataframeMean.
    def exitDataframeMean(self, ctx:calculadoraParser.DataframeMeanContext):
        pass


    # Enter a parse tree produced by calculadoraParser#listIndex.
    def enterListIndex(self, ctx:calculadoraParser.ListIndexContext):
        pass

    # Exit a parse tree produced by calculadoraParser#listIndex.
    def exitListIndex(self, ctx:calculadoraParser.ListIndexContext):
        pass


    # Enter a parse tree produced by calculadoraParser#listAppend.
    def enterListAppend(self, ctx:calculadoraParser.ListAppendContext):
        pass

    # Exit a parse tree produced by calculadoraParser#listAppend.
    def exitListAppend(self, ctx:calculadoraParser.ListAppendContext):
        pass


    # Enter a parse tree produced by calculadoraParser#unary.
    def enterUnary(self, ctx:calculadoraParser.UnaryContext):
        pass

    # Exit a parse tree produced by calculadoraParser#unary.
    def exitUnary(self, ctx:calculadoraParser.UnaryContext):
        pass


    # Enter a parse tree produced by calculadoraParser#listPop.
    def enterListPop(self, ctx:calculadoraParser.ListPopContext):
        pass

    # Exit a parse tree produced by calculadoraParser#listPop.
    def exitListPop(self, ctx:calculadoraParser.ListPopContext):
        pass


    # Enter a parse tree produced by calculadoraParser#float.
    def enterFloat(self, ctx:calculadoraParser.FloatContext):
        pass

    # Exit a parse tree produced by calculadoraParser#float.
    def exitFloat(self, ctx:calculadoraParser.FloatContext):
        pass


    # Enter a parse tree produced by calculadoraParser#graficaPuntos.
    def enterGraficaPuntos(self, ctx:calculadoraParser.GraficaPuntosContext):
        pass

    # Exit a parse tree produced by calculadoraParser#graficaPuntos.
    def exitGraficaPuntos(self, ctx:calculadoraParser.GraficaPuntosContext):
        pass


    # Enter a parse tree produced by calculadoraParser#dataframeSeries.
    def enterDataframeSeries(self, ctx:calculadoraParser.DataframeSeriesContext):
        pass

    # Exit a parse tree produced by calculadoraParser#dataframeSeries.
    def exitDataframeSeries(self, ctx:calculadoraParser.DataframeSeriesContext):
        pass


    # Enter a parse tree produced by calculadoraParser#id.
    def enterId(self, ctx:calculadoraParser.IdContext):
        pass

    # Exit a parse tree produced by calculadoraParser#id.
    def exitId(self, ctx:calculadoraParser.IdContext):
        pass


    # Enter a parse tree produced by calculadoraParser#dictExpr.
    def enterDictExpr(self, ctx:calculadoraParser.DictExprContext):
        pass

    # Exit a parse tree produced by calculadoraParser#dictExpr.
    def exitDictExpr(self, ctx:calculadoraParser.DictExprContext):
        pass


    # Enter a parse tree produced by calculadoraParser#listExpr.
    def enterListExpr(self, ctx:calculadoraParser.ListExprContext):
        pass

    # Exit a parse tree produced by calculadoraParser#listExpr.
    def exitListExpr(self, ctx:calculadoraParser.ListExprContext):
        pass


    # Enter a parse tree produced by calculadoraParser#tanFunction.
    def enterTanFunction(self, ctx:calculadoraParser.TanFunctionContext):
        pass

    # Exit a parse tree produced by calculadoraParser#tanFunction.
    def exitTanFunction(self, ctx:calculadoraParser.TanFunctionContext):
        pass


    # Enter a parse tree produced by calculadoraParser#closeFile.
    def enterCloseFile(self, ctx:calculadoraParser.CloseFileContext):
        pass

    # Exit a parse tree produced by calculadoraParser#closeFile.
    def exitCloseFile(self, ctx:calculadoraParser.CloseFileContext):
        pass


    # Enter a parse tree produced by calculadoraParser#comparison.
    def enterComparison(self, ctx:calculadoraParser.ComparisonContext):
        pass

    # Exit a parse tree produced by calculadoraParser#comparison.
    def exitComparison(self, ctx:calculadoraParser.ComparisonContext):
        pass


    # Enter a parse tree produced by calculadoraParser#Root.
    def enterRoot(self, ctx:calculadoraParser.RootContext):
        pass

    # Exit a parse tree produced by calculadoraParser#Root.
    def exitRoot(self, ctx:calculadoraParser.RootContext):
        pass


    # Enter a parse tree produced by calculadoraParser#dataframeDescribe.
    def enterDataframeDescribe(self, ctx:calculadoraParser.DataframeDescribeContext):
        pass

    # Exit a parse tree produced by calculadoraParser#dataframeDescribe.
    def exitDataframeDescribe(self, ctx:calculadoraParser.DataframeDescribeContext):
        pass


    # Enter a parse tree produced by calculadoraParser#sinFunction.
    def enterSinFunction(self, ctx:calculadoraParser.SinFunctionContext):
        pass

    # Exit a parse tree produced by calculadoraParser#sinFunction.
    def exitSinFunction(self, ctx:calculadoraParser.SinFunctionContext):
        pass


    # Enter a parse tree produced by calculadoraParser#bool.
    def enterBool(self, ctx:calculadoraParser.BoolContext):
        pass

    # Exit a parse tree produced by calculadoraParser#bool.
    def exitBool(self, ctx:calculadoraParser.BoolContext):
        pass


    # Enter a parse tree produced by calculadoraParser#string.
    def enterString(self, ctx:calculadoraParser.StringContext):
        pass

    # Exit a parse tree produced by calculadoraParser#string.
    def exitString(self, ctx:calculadoraParser.StringContext):
        pass


    # Enter a parse tree produced by calculadoraParser#MulDiv.
    def enterMulDiv(self, ctx:calculadoraParser.MulDivContext):
        pass

    # Exit a parse tree produced by calculadoraParser#MulDiv.
    def exitMulDiv(self, ctx:calculadoraParser.MulDivContext):
        pass


    # Enter a parse tree produced by calculadoraParser#factorial.
    def enterFactorial(self, ctx:calculadoraParser.FactorialContext):
        pass

    # Exit a parse tree produced by calculadoraParser#factorial.
    def exitFactorial(self, ctx:calculadoraParser.FactorialContext):
        pass


    # Enter a parse tree produced by calculadoraParser#negacion.
    def enterNegacion(self, ctx:calculadoraParser.NegacionContext):
        pass

    # Exit a parse tree produced by calculadoraParser#negacion.
    def exitNegacion(self, ctx:calculadoraParser.NegacionContext):
        pass


    # Enter a parse tree produced by calculadoraParser#increment.
    def enterIncrement(self, ctx:calculadoraParser.IncrementContext):
        pass

    # Exit a parse tree produced by calculadoraParser#increment.
    def exitIncrement(self, ctx:calculadoraParser.IncrementContext):
        pass


    # Enter a parse tree produced by calculadoraParser#getDictValue.
    def enterGetDictValue(self, ctx:calculadoraParser.GetDictValueContext):
        pass

    # Exit a parse tree produced by calculadoraParser#getDictValue.
    def exitGetDictValue(self, ctx:calculadoraParser.GetDictValueContext):
        pass


    # Enter a parse tree produced by calculadoraParser#cosFunction.
    def enterCosFunction(self, ctx:calculadoraParser.CosFunctionContext):
        pass

    # Exit a parse tree produced by calculadoraParser#cosFunction.
    def exitCosFunction(self, ctx:calculadoraParser.CosFunctionContext):
        pass


    # Enter a parse tree produced by calculadoraParser#listLen.
    def enterListLen(self, ctx:calculadoraParser.ListLenContext):
        pass

    # Exit a parse tree produced by calculadoraParser#listLen.
    def exitListLen(self, ctx:calculadoraParser.ListLenContext):
        pass


    # Enter a parse tree produced by calculadoraParser#removeDictEntry.
    def enterRemoveDictEntry(self, ctx:calculadoraParser.RemoveDictEntryContext):
        pass

    # Exit a parse tree produced by calculadoraParser#removeDictEntry.
    def exitRemoveDictEntry(self, ctx:calculadoraParser.RemoveDictEntryContext):
        pass


    # Enter a parse tree produced by calculadoraParser#writeFile.
    def enterWriteFile(self, ctx:calculadoraParser.WriteFileContext):
        pass

    # Exit a parse tree produced by calculadoraParser#writeFile.
    def exitWriteFile(self, ctx:calculadoraParser.WriteFileContext):
        pass


    # Enter a parse tree produced by calculadoraParser#graficaCaja.
    def enterGraficaCaja(self, ctx:calculadoraParser.GraficaCajaContext):
        pass

    # Exit a parse tree produced by calculadoraParser#graficaCaja.
    def exitGraficaCaja(self, ctx:calculadoraParser.GraficaCajaContext):
        pass


    # Enter a parse tree produced by calculadoraParser#deleteFile.
    def enterDeleteFile(self, ctx:calculadoraParser.DeleteFileContext):
        pass

    # Exit a parse tree produced by calculadoraParser#deleteFile.
    def exitDeleteFile(self, ctx:calculadoraParser.DeleteFileContext):
        pass


    # Enter a parse tree produced by calculadoraParser#addDictEntry.
    def enterAddDictEntry(self, ctx:calculadoraParser.AddDictEntryContext):
        pass

    # Exit a parse tree produced by calculadoraParser#addDictEntry.
    def exitAddDictEntry(self, ctx:calculadoraParser.AddDictEntryContext):
        pass


    # Enter a parse tree produced by calculadoraParser#Mod.
    def enterMod(self, ctx:calculadoraParser.ModContext):
        pass

    # Exit a parse tree produced by calculadoraParser#Mod.
    def exitMod(self, ctx:calculadoraParser.ModContext):
        pass


    # Enter a parse tree produced by calculadoraParser#repetida.
    def enterRepetida(self, ctx:calculadoraParser.RepetidaContext):
        pass

    # Exit a parse tree produced by calculadoraParser#repetida.
    def exitRepetida(self, ctx:calculadoraParser.RepetidaContext):
        pass


    # Enter a parse tree produced by calculadoraParser#AddSub.
    def enterAddSub(self, ctx:calculadoraParser.AddSubContext):
        pass

    # Exit a parse tree produced by calculadoraParser#AddSub.
    def exitAddSub(self, ctx:calculadoraParser.AddSubContext):
        pass


    # Enter a parse tree produced by calculadoraParser#dataframeHead.
    def enterDataframeHead(self, ctx:calculadoraParser.DataframeHeadContext):
        pass

    # Exit a parse tree produced by calculadoraParser#dataframeHead.
    def exitDataframeHead(self, ctx:calculadoraParser.DataframeHeadContext):
        pass


    # Enter a parse tree produced by calculadoraParser#euclidesFunction.
    def enterEuclidesFunction(self, ctx:calculadoraParser.EuclidesFunctionContext):
        pass

    # Exit a parse tree produced by calculadoraParser#euclidesFunction.
    def exitEuclidesFunction(self, ctx:calculadoraParser.EuclidesFunctionContext):
        pass


    # Enter a parse tree produced by calculadoraParser#int.
    def enterInt(self, ctx:calculadoraParser.IntContext):
        pass

    # Exit a parse tree produced by calculadoraParser#int.
    def exitInt(self, ctx:calculadoraParser.IntContext):
        pass


    # Enter a parse tree produced by calculadoraParser#graficaHistograma.
    def enterGraficaHistograma(self, ctx:calculadoraParser.GraficaHistogramaContext):
        pass

    # Exit a parse tree produced by calculadoraParser#graficaHistograma.
    def exitGraficaHistograma(self, ctx:calculadoraParser.GraficaHistogramaContext):
        pass


    # Enter a parse tree produced by calculadoraParser#dataframeExpr.
    def enterDataframeExpr(self, ctx:calculadoraParser.DataframeExprContext):
        pass

    # Exit a parse tree produced by calculadoraParser#dataframeExpr.
    def exitDataframeExpr(self, ctx:calculadoraParser.DataframeExprContext):
        pass


    # Enter a parse tree produced by calculadoraParser#inverseExpr.
    def enterInverseExpr(self, ctx:calculadoraParser.InverseExprContext):
        pass

    # Exit a parse tree produced by calculadoraParser#inverseExpr.
    def exitInverseExpr(self, ctx:calculadoraParser.InverseExprContext):
        pass


    # Enter a parse tree produced by calculadoraParser#listRemove.
    def enterListRemove(self, ctx:calculadoraParser.ListRemoveContext):
        pass

    # Exit a parse tree produced by calculadoraParser#listRemove.
    def exitListRemove(self, ctx:calculadoraParser.ListRemoveContext):
        pass


    # Enter a parse tree produced by calculadoraParser#readFile.
    def enterReadFile(self, ctx:calculadoraParser.ReadFileContext):
        pass

    # Exit a parse tree produced by calculadoraParser#readFile.
    def exitReadFile(self, ctx:calculadoraParser.ReadFileContext):
        pass


    # Enter a parse tree produced by calculadoraParser#decrement.
    def enterDecrement(self, ctx:calculadoraParser.DecrementContext):
        pass

    # Exit a parse tree produced by calculadoraParser#decrement.
    def exitDecrement(self, ctx:calculadoraParser.DecrementContext):
        pass


    # Enter a parse tree produced by calculadoraParser#graficaLineas.
    def enterGraficaLineas(self, ctx:calculadoraParser.GraficaLineasContext):
        pass

    # Exit a parse tree produced by calculadoraParser#graficaLineas.
    def exitGraficaLineas(self, ctx:calculadoraParser.GraficaLineasContext):
        pass


    # Enter a parse tree produced by calculadoraParser#matrixExpr.
    def enterMatrixExpr(self, ctx:calculadoraParser.MatrixExprContext):
        pass

    # Exit a parse tree produced by calculadoraParser#matrixExpr.
    def exitMatrixExpr(self, ctx:calculadoraParser.MatrixExprContext):
        pass


    # Enter a parse tree produced by calculadoraParser#tupleExpr.
    def enterTupleExpr(self, ctx:calculadoraParser.TupleExprContext):
        pass

    # Exit a parse tree produced by calculadoraParser#tupleExpr.
    def exitTupleExpr(self, ctx:calculadoraParser.TupleExprContext):
        pass


    # Enter a parse tree produced by calculadoraParser#writelinesFile.
    def enterWritelinesFile(self, ctx:calculadoraParser.WritelinesFileContext):
        pass

    # Exit a parse tree produced by calculadoraParser#writelinesFile.
    def exitWritelinesFile(self, ctx:calculadoraParser.WritelinesFileContext):
        pass


    # Enter a parse tree produced by calculadoraParser#transposeExpr.
    def enterTransposeExpr(self, ctx:calculadoraParser.TransposeExprContext):
        pass

    # Exit a parse tree produced by calculadoraParser#transposeExpr.
    def exitTransposeExpr(self, ctx:calculadoraParser.TransposeExprContext):
        pass


    # Enter a parse tree produced by calculadoraParser#leerCsv.
    def enterLeerCsv(self, ctx:calculadoraParser.LeerCsvContext):
        pass

    # Exit a parse tree produced by calculadoraParser#leerCsv.
    def exitLeerCsv(self, ctx:calculadoraParser.LeerCsvContext):
        pass


    # Enter a parse tree produced by calculadoraParser#return.
    def enterReturn(self, ctx:calculadoraParser.ReturnContext):
        pass

    # Exit a parse tree produced by calculadoraParser#return.
    def exitReturn(self, ctx:calculadoraParser.ReturnContext):
        pass


    # Enter a parse tree produced by calculadoraParser#Power.
    def enterPower(self, ctx:calculadoraParser.PowerContext):
        pass

    # Exit a parse tree produced by calculadoraParser#Power.
    def exitPower(self, ctx:calculadoraParser.PowerContext):
        pass


    # Enter a parse tree produced by calculadoraParser#matrix.
    def enterMatrix(self, ctx:calculadoraParser.MatrixContext):
        pass

    # Exit a parse tree produced by calculadoraParser#matrix.
    def exitMatrix(self, ctx:calculadoraParser.MatrixContext):
        pass


    # Enter a parse tree produced by calculadoraParser#matrix_contents.
    def enterMatrix_contents(self, ctx:calculadoraParser.Matrix_contentsContext):
        pass

    # Exit a parse tree produced by calculadoraParser#matrix_contents.
    def exitMatrix_contents(self, ctx:calculadoraParser.Matrix_contentsContext):
        pass


    # Enter a parse tree produced by calculadoraParser#row.
    def enterRow(self, ctx:calculadoraParser.RowContext):
        pass

    # Exit a parse tree produced by calculadoraParser#row.
    def exitRow(self, ctx:calculadoraParser.RowContext):
        pass


    # Enter a parse tree produced by calculadoraParser#list.
    def enterList(self, ctx:calculadoraParser.ListContext):
        pass

    # Exit a parse tree produced by calculadoraParser#list.
    def exitList(self, ctx:calculadoraParser.ListContext):
        pass


    # Enter a parse tree produced by calculadoraParser#tupla.
    def enterTupla(self, ctx:calculadoraParser.TuplaContext):
        pass

    # Exit a parse tree produced by calculadoraParser#tupla.
    def exitTupla(self, ctx:calculadoraParser.TuplaContext):
        pass


    # Enter a parse tree produced by calculadoraParser#list_contents.
    def enterList_contents(self, ctx:calculadoraParser.List_contentsContext):
        pass

    # Exit a parse tree produced by calculadoraParser#list_contents.
    def exitList_contents(self, ctx:calculadoraParser.List_contentsContext):
        pass


    # Enter a parse tree produced by calculadoraParser#dicti.
    def enterDicti(self, ctx:calculadoraParser.DictiContext):
        pass

    # Exit a parse tree produced by calculadoraParser#dicti.
    def exitDicti(self, ctx:calculadoraParser.DictiContext):
        pass


    # Enter a parse tree produced by calculadoraParser#dict_contents.
    def enterDict_contents(self, ctx:calculadoraParser.Dict_contentsContext):
        pass

    # Exit a parse tree produced by calculadoraParser#dict_contents.
    def exitDict_contents(self, ctx:calculadoraParser.Dict_contentsContext):
        pass


    # Enter a parse tree produced by calculadoraParser#dict_access.
    def enterDict_access(self, ctx:calculadoraParser.Dict_accessContext):
        pass

    # Exit a parse tree produced by calculadoraParser#dict_access.
    def exitDict_access(self, ctx:calculadoraParser.Dict_accessContext):
        pass


    # Enter a parse tree produced by calculadoraParser#dict_entry.
    def enterDict_entry(self, ctx:calculadoraParser.Dict_entryContext):
        pass

    # Exit a parse tree produced by calculadoraParser#dict_entry.
    def exitDict_entry(self, ctx:calculadoraParser.Dict_entryContext):
        pass


    # Enter a parse tree produced by calculadoraParser#dataframe.
    def enterDataframe(self, ctx:calculadoraParser.DataframeContext):
        pass

    # Exit a parse tree produced by calculadoraParser#dataframe.
    def exitDataframe(self, ctx:calculadoraParser.DataframeContext):
        pass


    # Enter a parse tree produced by calculadoraParser#args.
    def enterArgs(self, ctx:calculadoraParser.ArgsContext):
        pass

    # Exit a parse tree produced by calculadoraParser#args.
    def exitArgs(self, ctx:calculadoraParser.ArgsContext):
        pass



del calculadoraParser