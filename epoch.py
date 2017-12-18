#/usr/bin/python

# Loglines are like this:
# [1513322531] This is line number one in the logfile
# [1513322534] This is line number two in the logfile
# [1513338238] This is line number three in the logfile

import time
inputfile = "input filename including path"
outputfile = "output file incliding path"
linesout = 0
with open(inputfile) as fin:
    lines = fin.readlines()

fout = open(outputfile,"w")
for line in lines:
    fout.writelines(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(float(line[1:11]))) + line[12:])
    linesout += 1

print("Done, %s lines written." % linesout)
