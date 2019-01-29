#!/usr/bin/env python
import sys

layer = "15"


if str(sys.argv[1])[-4:] == '.mod':
	print "Succes!"
	#opening source file
	f = open(str(sys.argv[1]),'r')
	#opening destination file
	f1 = open(str(sys.argv[2]), 'wb')


	for line in f.readlines():
		if line[0:2] == "DP":
			line = line.replace("21",layer)
			f1.write(line)
		else:
			f1.write(line)
	f.close()
	f1.close()
	print "Have a nice day!"
else:
	print "#Err!! Wrong source file format. Should be .drl. \nFunction format is \ndrl2gcode.py source_file.drl destination_file.ngc"
	
