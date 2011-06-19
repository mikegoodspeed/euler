d = map(int, ''.join([repr(x) for x in xrange(1, 185186)]))
print d[9] * d[99] * d[999] * d[9999] * d[99999] * d[999999]
