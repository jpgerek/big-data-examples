#!/usr/bin/python2.6
# -*- coding: utf-8 -*-

import sys
import re
import io

for line in sys.stdin:
        line = re.sub(r'[^a-záéíóúüñç\s]', '', line.lower()).strip()
        if line != '':
                for word in re.split(r' +', line):
                        print("{0}\t1".format(word))
