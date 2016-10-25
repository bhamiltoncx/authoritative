Unicode-3.0.0
=============

0: Highlights
=============
ANTLR4:
```
| ----------------- | --------------------------------------------------- |
| FILE              | CONTENTS                                            |
| ----------------- | --------------------------------------------------- |
| classify16.g4     | ANTLR4 import grammar for codepoint classification  |
| classify21.g4     | 21 bit import grammar for codepoint classification  |
| makeGrammars.py   | Code to generate classify*.g4                       |
| ----------------- | --------------------------------------------------- |
| test_ASCII.g4     | Simple original g4 grammar for comparison test      |
| test_ASCII.py     | Simple original g4 grammar test script              |
| ----------------- | --------------------------------------------------- |
| test_Codepoint.g4 | Simple classify g4 grammar for import testing       |
| test_Codepoint.py | Simple classify g4 grammar test script              |
| ----------------- | --------------------------------------------------- |
| Makefile          | Script to download Unicode files, generate g4, test |
| README.md         | This file                                           |
| ----------------- | --------------------------------------------------- |
```

1: Codepoint classification grammar
===================================
2016 Automated Unicode codepoint classification ANTLR4 grammar writer.

Python code to convert authoritative unicode.org resource files into
a complete and commented grammar suitable for import into other grammars.
Similar tables are built within the python code for local testing.

TODO: Finish Python generation of classification table.
This compiled table (in .c or .js JIT) may outperform
other implementations including ANTLR4 grammar
possibly by an order of magnitude.


1.1: Makefile help
==================
```
$ make help
Makefile for "classify" grammar generator and tests
Version 0.0.2

Author    : Jonathan D. Lettvin (jlettvin@gmail.com)
Date      : 20161023
Legal     : Copyright(c) Jonathan D. Lettvin, All Rights Reserved
License   : GPL 3.0

Usage:
    make [all]        Download resources, Generate grammar, Test
    make test         Run simple generator internal tests
    make clean        Remove temporary and unnecessary files
    make help         Display this text
    make version      Display version of this Makefile

Description: See README.md
```

1.2: makeGrammars.py --help
===========================
```
$ ./makeGrammars.py --help
makeGrammars.py

Usage:
    makeGrammars.py [-acefktuz] [-v]
    makeGrammars.py (-h | --help)
    makeGrammars.py (--version)

Options:
    -a --showascii                  Show ASCII class/name
    -c --showcount                  Show key counts
    -e --enhance                    Add WS and ID rules
    -f --full21bit                  Express full 21 bit range 0 to 10FFFF
    -k --showkeys                   Show key names
    -t --showtables                 Show tables
    -u --unittest                   Run tests
    -z --zeroerror                  Use zero, not len as ERROR table index
    -v --verbose                    Show verbose output
    -h --help                       Show this Usage message
    --version                       Show version

Concepts:
    The authority for codepoint classification is unicode.org.
    One file (UnicodeData.txt) is the absolute authority.
    Each legal codepoint (Unicode character) is defined in its own line.
    Each line is semicolon separated and its columns are not labelled.
    A second file (UnicodeData-3.0.0) provides the correct column labels.
    It also provides Abbreviation Descriptions for each codepoint.

    Enhance (-e) causes additional rules to be moved
    from the file hello.g4 to the file classify.g4 where
    they can be imported into other grammars.

Author  : Jonathan D. Lettvin (jlettvin@gmail.com)
Date    : 20161023 
Legal   : Copyright(c) Jonathan D. Lettvin, All Rights Reserved
License : GPL 3.0
```

1.3: Instructions
=================
Quick:
* $ make clean
* $ make

Expect output of make to be:
```
UnicodeData.txt
Blocks.txt
PropertyValueAliases.txt
UnicodeData-3.0.0.html
classify16.g4
produce both 16 bit (ANTLR) and 21 bit (full21bit) grammars
test_ASCII.tokens
Test ordinary lexer
line 2:6 token recognition error at: '愚'
line 2:7 token recognition error at: '公'
line 2:8 token recognition error at: '移'
line 2:9 token recognition error at: '山'
line 3:0 missing ID at '<EOF>'
[PASS] original: original
[PASS] original: &lt;missing ID&gt;
test_Codepoint.tokens
Test classify lexer
[PASS] classify: classify
[PASS] classify: 愚公移山
make finished.  Creating MANIFEST
```

Observe:
* The four unicode.org files are downoaded.
* The grammars are produced
* test_ASCII (the ASCII grammar) is executed with one PASS and one FAIL.
* test_Codepoint (the class grammar) is executed with two PASSes
* A manifest of working files is produced

TODO: The [PASS] with &lt;missing ID&gt; is in error and needs correction.

Requirements:

command-line tools:
* antlr4
* wget

Python libraries:
* BeautifulSoup
* docopt

The Makefile performs several important functions.

Fetch/refresh local copies of unicode.org resource files:
* UnicodeData.txt (primary data for legal codepoint values)
* UnicodeData-3.0.0.html (column names for UnicodeData.txt)
* Blocks.txt (classification abbreviations for blocks of codepoints)
* PropertyValueAliases.txt (classification names for blocks)

Process:
* Extract data from resource files and construct grammars
* Test grammars by submission to ANTLR4

The resulting grammars include:
* classify*.g4 (grammars identifying all legal codepoint classifications)
* test_Codepoint.g4 (grammar which imports classify.g4)

In particular:
* classify16.g4 (16 bit unicode) is a limitation of ANTLR for java.
* classify21.g4 (21 bit unicode) is fully compliant with the unicode standard.

TODO: Finish generating a new independent classification table:
Once this internally constructed Table in makeGrammars.py is finished,
submitting a Unicode codepoint "u" to this lookup
yields the codepoint (character) class suitable for a lexer to use.
```
classification = Table[Table[Table[Base][(u>>14)&0x7f]][(u>>7)&0x7f]][u&0x7f]
```
This is approximately 11 Intel instructions in machine code:
* 2 shifts
* 3 masks
* 6 dereferences

The existing table performs well for all legal 21 bit unicode codepoints
but only classifies ASCII correctly.
When finished, operations and performance will be compared with
code generated by ANTLR4 and reported here.
