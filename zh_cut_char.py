from ChineseTone import ChineseHelper
from zhon.hanzi import punctuation
import sys
import re

def zhSents_to_zhChars(chinese_sentence):

    chinese_sentence = chinese_sentence.strip()
    list_chars = []
    _tmp = ''

    for c in chinese_sentence:
        if ( ChineseHelper.isChinese(c) ) or ( c in punctuation ) or ( c in string.punctuation ):
            if _tmp:
                print(_tmp.strip())
                list_chars.append(_tmp.strip())
                _tmp = ''
            print(c)
            list_chars.append(c)
        else:
            _tmp += c

    if _tmp:
        list_chars.append(_tmp.strip())

    return list_chars



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
