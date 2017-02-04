import time

class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print 'elapsed time: %f ms' % self.msecs


def factorial(x):
  result=1
  while x>=1:
    result=x*result
    x=x-1


def factorial2(x):
  if x==1:
    return x
  else:
    return x*factorial2(x-1)

with Timer() as t:
#  factorial(5000)
   factorial2(500)
print "=> elasped time: %s s" % t.secs

