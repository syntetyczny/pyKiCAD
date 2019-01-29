#!/usr/bin/env python
import sys

drilling_speed = " F1200"
loose_speed = "F4000"
safe_Z = "15.000"
drilling_depth = "-3.000"


if str(sys.argv[1])[-4:] == '.drl':
	print "Succes!"
	#opening source file
	f = open(str(sys.argv[1]),'r')
	#opening destination file
	f1 = open(str(sys.argv[2]), 'wb')

	
	f1.write('(PJD - Automatyka 25.02.2013) \n(drl to gcode)')
	f1.write('G90 (set absolute distance mode) \n')
	f1.write('S25000 M3 (set 25000rpm speed of spindle) \n')
	f1.write('G64 P0.01 (set 0.01 accurance for arcs) \n')

	for line in f.readlines():
		if line.find("G85") != -1:
			line_1 = line[:line.find("G85")]
			line_2 = line[line.find("G85"):]
			if line[0] == "T":
				#line = line[:-1]
				f1.write('('+line[:-1] + ')' + line[-1])
			if line_1[0] == 'X':
				f1.write('G0 ' + 'Z ' + safe_Z + ' ' + loose_speed + line[-1])
				f1.write('G0 ' + line_1[:-1] + ' ' + loose_speed + line[-1])
				f1.write('G1 ' + 'Z ' + drilling_depth + ' ' + drilling_speed + line[-1])
			if line_2[0] == 'X':
				f1.write('G0 ' + 'Z ' + safe_Z + ' ' + loose_speed + line[-1])
				f1.write('G0 ' + line_2[:-1] + ' ' + loose_speed + line[-1])
				f1.write('G1 ' + 'Z ' + drilling_depth + ' ' + drilling_speed + line[-1])
		else:
			if line[0] == "T":
				#line = line[:-1]
				f1.write('('+line[:-1] + ')' + line[-1])
			if line[0] == 'X':
				f1.write('G0 ' + 'Z ' + safe_Z + ' ' + loose_speed + line[-1])
				f1.write('G0 ' + line[:-1] + ' ' + loose_speed + line[-1])
				f1.write('G1 ' + 'Z ' + drilling_depth + ' ' + drilling_speed + line[-1])
			
	
	f1.write('G0 ' + 'Z ' + safe_Z + ' ' + loose_speed + '\n')
	f1.write(' M5 ' + '\n')
	f1.write(' M2 ' + '\n')

	f.close()
	f1.close()
	print "Have a nice day!"
else:
	print "#Err!! Wrong source file format. Should be .drl. \nFunction format is \ndrl2gcode.py source_file.drl destination_file.ngc"
	
