__author__ = 'alihitawala'

import sys

try:
    filew = open("textfile", "r")
except IOError:
    print "there was an error writing to file "
    sys.exit(1)
file_text = filew.read()
print(file_text)