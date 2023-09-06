import json
import urllib.error
import urllib.parse
import urllib.request

import sys
import logging
import datetime

logging.basicConfig(level=logging.WARNING)

def wlog(obj, newline=1):
    if newline == 1: sys.stderr.write('{} -> {}\n'.format(datetime.datetime.now(), obj))
    else: sys.stderr.write('{} -> {}'.format(datetime.datetime.now(), obj))
    #if newline == 1: wlog(obj, file=sys.stderr, flush=True)
    #else: wlog(obj, file=sys.stderr, end='', flush=True)
    sys.stderr.flush()

def translate(sentence, src_lan, tgt_lan, apikey):
    url = 'http://api.niutrans.com/NiuTransServer/translation?'
    data = {"from": src_lan, "to": tgt_lan, "apikey": apikey, "src_text": sentence}
    data_en = urllib.parse.urlencode(data)
    req = url + "&" + data_en
    res = urllib.request.urlopen(req)
    res = res.read()
    res_dict = json.loads(res)
    if "tgt_text" in res_dict:
        result = res_dict['tgt_text']
    else:
        result = res
    return result

if __name__ == "__main__":
    in_src = open("macs_no_uid.txt", "r", encoding='utf-8')
    out_src = open("macs_no_uid_xiaoniu_zh.txt", "w", encoding='utf-8')
    lines = in_src.readlines()
    for line in lines:
        wlog('src: {}'.format(line.strip()))
        line = line.strip()
        trans = translate(line, 'en', 'zh', '39d906d301b6e2a3454bb0fb9a17edca')
        try:
            trans = trans.decode('utf-8')
        except:
            trans = trans
        out_src.write('{}\n'.format(trans.strip()))
        out_src.flush()
        wlog('trans: {}'.format(trans.strip()))




