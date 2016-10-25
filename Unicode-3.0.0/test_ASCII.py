#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""test_ASCII.py
This module tests the test_ASCII grammar an ASCII-only grammar.
"""

from antlr4                     import *
from test_ASCIILexer                import (    test_ASCIILexer     )
from test_ASCIIListener             import (    test_ASCIIListener  )
from test_ASCIIParser               import (    test_ASCIIParser    )

"""
from anltr4.error.ErrorListener import (    ErrorListener   )

class test_ASCIIErrorListener(ErrorListener):
    def __init__(self):
        super(test_ASCIIErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, col, msg, e):
        raise Exception(offendingSymbol)
"""

class test_ASCIIPrintListener(test_ASCIIListener):

    def enterHello(self, ctx):
        print "[PASS] original: %s" % (ctx.ID())

    # Can't work.  No codepoint
    #def enterCodepoint(self, ctx):
        #print "[FAIL] classify: %s" % (ctx.ID())


if __name__ == "__main__":

    def main():
        lexer = test_ASCIILexer(StdinStream(encoding="utf8"))
        stream = CommonTokenStream(lexer)
        parser = test_ASCIIParser(stream)
        # parser._listeners = [ test_ASCIIErrorListener() ]
        tree = parser.prog()
        printer = test_ASCIIPrintListener()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)

    try:
        main()
    except Exception as e:
        print '[FAIL] ' + str(e)
