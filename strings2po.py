#!/usr/bin/env python

import re
import sys

print('msgid ""')
print('msgstr ""')
print('"Project-Id-Version: \\n"')
print('"PO-Revision-Date: \\n"')
print('"Last-Translator: \\n"')
print('"Language-Team: \\n"')
print('"MIME-Version: 1.0\\n"')
print('"Content-Type: text/plain; charset=UTF-8\\n"')
print('"Content-Transfer-Encoding: 8bit\\n"')
print('"Plural-Forms: nplurals=2; plural=(n != 1);\\n"')
print('\n')

for strings_line in sys.stdin.readlines():
    popartition = None
    if strings_line.startswith('\"'):
        string = strings_line.replace(';', '').rstrip()
        popartition = string.partition("=")
        if popartition and popartition != "\"\"":
            print('msgid %s\nmsgstr %s\n' % (popartition[0].strip(), popartition[2].strip()))
