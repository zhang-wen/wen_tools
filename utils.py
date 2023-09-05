import datetime
import logging
logging.basicConfig(level=logging.WARNING)

def wlog(obj, newline=1):
    if newline == 1: sys.stderr.write('{} -> {}\n'.format(datetime.datetime.now(), obj))
    else: sys.stderr.write('{} -> {}'.format(datetime.datetime.now(), obj))
    #if newline == 1: wlog(obj, file=sys.stderr, flush=True)
    #else: wlog(obj, file=sys.stderr, end='', flush=True)
    sys.stderr.flush()
