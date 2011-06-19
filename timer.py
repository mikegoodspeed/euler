import sys
import datetime
import os

start = datetime.datetime.now()
os.system('python ' + sys.argv[1])
print datetime.datetime.now() - start
