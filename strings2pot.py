#!/usr/bin/env python

import re
import sys
import datetime

print('msgid ""')
print('msgstr ""')
print('"Project-Id-Version: \\n"')
print('"Report-Msgid-Bugs-To: \\n"')
print('"POT-Creation-Date: %s \\n"' % datetime.datetime.utcnow())
print('"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n"')
print('"Last-Translator: \\n"')
print('"Language-Team: \\n"')
print('"MIME-Version: 1.0\\n"')
print('"Content-Type: text/plain; charset=UTF-8\\n"')
print('"Content-Transfer-Encoding: 8bit\\n"')
print('\n')

for strings_line in sys.stdin.readlines():
    popartition = None
    if strings_line.startswith('\"'):
        string = strings_line.replace(';', '').rstrip()
        popartition = string.partition("=")
        if popartition and popartition != "\"\"":
            print('msgid %s\nmsgstr ""\n' % popartition[0].strip())
