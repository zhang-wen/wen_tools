from ChineseTone import ChineseHelper
from zhon.hanzi import punctuation
import sys
import re

for line in sys.stdin:
    _tmp = ''
    for c in line.strip():
        if ChineseHelper.isChinese(c):
            _tmp += ' ' +  c + ' '
        elif c in punctuation:
            _tmp += ' ' +  c + ' '
        else:
            _tmp += c
    _tmp = re.sub('  ', ' ', _tmp) 
    sys.stdout.write('{}\n'.format(_tmp.strip()))
