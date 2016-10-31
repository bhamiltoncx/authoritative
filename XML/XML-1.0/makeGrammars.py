#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""authoritativeXML.py

Usage:
    authoritativeXML.py [-v]
    authoritativeXML.py (-h | --help)
    authoritativeXML.py (--version)

Options:
    -v --verbose                    Show verbose output
    -h --help                       Show this Usage message
    --version                       Show version

Concepts:
    Read authoritative specification, parse, and convert to grammar.

Author  : Jonathan D. Lettvin (jlettvin@gmail.com)
Date    : 20161023 
Legal   : Copyright(c) Jonathan D. Lettvin, All Rights Reserved
License : GPL 3.0
"""

__module__     = "authoritativeXML.py"
__author__     = "Jonathan D. Lettvin"
__copyright__  = "\
Copyright(C) 2016 Jonathan D. Lettvin, All Rights Reserved"
__credits__    = [ "Jonathan D. Lettvin" ]
__license__    = "GPLv3"
__version__    = "0.0.1"
__maintainer__ = "Jonathan D. Lettvin"
__email__      = "jlettvin@gmail.com"
__contact__    = "jlettvin@gmail.com"
__status__     = "Demonstration"
__date__       = "20161024"

from re     import (sub)
from bs4    import (BeautifulSoup)
from urllib import (urlopen)
from pprint import (pprint)
from docopt import (docopt)

class XML(dict):

    URI = {
        'authority': "https://www.w3.org/TR/xml/REC-xml-20081126.xml",
        'local': "REC-xml-20081126.xml"
    }

    def __init__(self, **kw):
        self.__dict__ = self
        self.update(**kw)
        #self.soup = BeautifulSoup(open(XML.URI["authority"]).read())
        self.soup = BeautifulSoup(open(XML.URI["local"]).read())
        scraps = self.soup.find_all('table', attrs={'class':"Scrap"});
        pprint(scraps)

if __name__ == "__main__":

    def main():
        "main is the traditional module entrypoint"

        # Convert command-line arguments to a dictionary suitable for members.
        kwargs = {
            k.strip('-'): w
            for k, w in docopt(__doc__, version="0.0.1").iteritems()
        }
        if kwargs["verbose"]:
            pprint(kwargs)

        xml = XML(**kwargs)

    main()
