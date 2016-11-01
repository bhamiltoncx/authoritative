#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""hello.py
This module tests the test_Codepoint grammar which imports the "classify" grammar.
"""

from antlr4                     import *
from test_CodepointLexer                import (    test_CodepointLexer     )
from test_CodepointListener             import (    test_CodepointListener  )
from test_CodepointParser               import (    test_CodepointParser    )

"""
from anltr4.error.ErrorListener import (    ErrorListener   )

class test_CodepointErrorListener(ErrorListener):
    def __init__(self):
        super(test_CodepointErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, col, msg, e):
        raise Exception(offendingSymbol)
"""

class test_CodepointPrintListener(test_CodepointListener):

    def enterHello(self, ctx):
        print "[PASS] classify: %s" % (ctx.ID())

    def enterCodepoint(self, ctx):
        print "[FAIL] classify: %s" % (ctx.ID())

if __name__ == "__main__":

    def main():
        lexer = test_CodepointLexer(StdinStream(encoding="utf8"))
        stream = CommonTokenStream(lexer)
        parser = test_CodepointParser(stream)
        # parser._listeners = [ test_CodepointErrorListener() ]
        tree = parser.prog()
        printer = test_CodepointPrintListener()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)

    try:
        main()
    except Exception as e:
        print '[FAIL] ' + str(e)
