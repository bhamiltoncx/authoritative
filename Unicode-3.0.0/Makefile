#!/usr/bin/env make
# Makefile for "classify" grammar generator and tests
# Version 0.0.2
#
# Author    : Jonathan D. Lettvin (jlettvin@gmail.com)
# Date      : 20161023
# Legal     : Copyright(c) Jonathan D. Lettvin, All Rights Reserved
# License   : GPL 3.0
#
# Usage:
#     make [all]        Download resources, Generate grammar, Test
#     make test         Run simple generator internal tests
#     make clean        Remove temporary and unnecessary files
#     make help         Display this text
#     make version      Display version of this Makefile
#
# Description: See README.md

MANIFEST=                       \
	MANIFEST Makefile README.md \
	makeGrammars.py             \
	classify16.g4 classify21.g4 \
	test_Codepoint.py test_Codepoint.g4 test_ASCII.py test_ASCII.g4

FTP=ftp://ftp.unicode.org/Public/

SOURCES=                        \
	UnicodeData.txt             \
	Blocks.txt                  \
	PropertyValueAliases.txt    \
	UnicodeData-3.0.0.html

GRAMMARS=                              \
	classify16.g4    test_Codepoint.g4 \
	classify21.g4    test_ASCII.g4

TARGETS=                                                    \
	test_ASCII.tokens           test_Codepoint.tokens       \
	test_ASCIILexer.py          test_CodepointLexer.py      \
	test_ASCIILexer.tokens      test_CodepointLexer.tokens  \
	test_ASCIIListener.py       test_CodepointListener.py   \
	test_ASCIIParser.py         test_CodepointParser.py     \
	test_ASCIIVisitor.py        test_CodepointVisitor.py

antlr4=java -jar /usr/local/lib/antlr-4.5.3-complete.jar

all: test_ASCII.tokens test_ASCII.tokens test_Codepoint.tokens
	@echo "make finished.  Creating MANIFEST"

.PHONY:
help:
	@cat Makefile|grep "^#"|cut -c3-|grep -v "/usr/bin/env"

.PHONY:
version:
	@echo "Makefile `cat Makefile|grep '^#'|cut -c3-|grep 'Version'`"
	@echo "classify Version \
`grep 'docopt.*vers' makeGrammars.py |cut -d'\"' -f 2`"

.PHONY:
test: $(GRAMMARS)
	./makeGrammars.py -u

.PHONY:
clean:
	@echo $@
	@rm -f MANIFEST
	@$(foreach item, $(MANIFEST), echo $(item) >> MANIFEST;)
	@echo "Try: @ls -1 | sort MANIFEST MANIFEST - | uniq -u | xargs rm -f"
	@rm -f $(SOURCES) $(TARGETS) *.pyc local/*

.PHONY:
UnicodeData.txt:
	@echo $@
	@wget -q -c -N -Plocal $(FTP)UCD/latest/ucd/$@

.PHONY:
Blocks.txt:
	@echo $@
	@wget -q -c -N -Plocal $(FTP)UCD/latest/ucd/$@

.PHONY:
PropertyValueAliases.txt:
	@echo $@
	@wget -q -c -N -Plocal $(FTP)UCD/latest/ucd/$@

.PHONY:
UnicodeData-3.0.0.html:
	@echo $@
	@wget -q -c -N -Plocal $(FTP)3.0-Update/$@

test_ASCII.tokens: $(GRAMMARS) test_ASCII.py Makefile
	@echo $@
	@$(antlr4) -Dlanguage=Python2 -visitor test_ASCII.g4
	@echo "Test ordinary lexer"
	@echo "hello original\nhello 愚公移山"   | ./test_ASCII.py

test_Codepoint.tokens: $(GRAMMARS) test_Codepoint.py Makefile
	@echo $@
	@$(antlr4) -Dlanguage=Python2 -visitor test_Codepoint.g4
	@echo "Test classify lexer"
	@echo "hello classify\nhello 愚公移山"   | ./test_Codepoint.py

test_Codepoint.g4: makeGrammars.py $(SOURCES) Makefile
	@echo "$@"
	@echo "produce both 16 bit (ANTLR) and 21 bit (full21bit) grammars"
	@./makeGrammars.py --zeroerror --enhance
	@./makeGrammars.py --zeroerror --enhance --full21bit
