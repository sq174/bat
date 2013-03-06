# context_timer.py
import datetime
import sys

class Timer(object):
    def __init__(self, name=None, out=sys.stdout):
        self.name = name
        self.out = out

    def __enter__(self):
        self.tstart = datetime.datetime.now()

    def __exit__(self, exc_type, exc_value, traceback):
        self.tend = datetime.datetime.now()
        print("【開始】" + self.tstart)
        print("【終了】" + self.tend)
        print("【処理時間】" + self.tend - self.tstart)
