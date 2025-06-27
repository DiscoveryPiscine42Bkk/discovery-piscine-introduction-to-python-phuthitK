#!/usr/bin/env python3
import sys
import re
user = len(sys.argv)

if user == 2:
    print('none')
else:
    for a in range(1 , len(sys.argv)):
        if len(re.findall("ism" , sys.argv[a])) > 0:
            pass
        else:
            print(sys.argv[a] + "ism")