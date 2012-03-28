#!/usr/bin/env python

import re
import sys

for po_line in sys.stdin.readlines():
    msgstr = None
    if po_line.startswith('msgid '):
        msgid = po_line.replace('msgid ', '').rstrip()
    if po_line.startswith('msgstr '):
        msgstr = po_line.replace('msgstr ', '').rstrip()
    if msgstr and msgstr != "\"\"":
        print('%s = %s;' % (msgid, msgstr))
