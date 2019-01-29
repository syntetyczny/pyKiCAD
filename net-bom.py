#!/usr/bin/env python
import sys

if str(sys.argv[1])[-4:] == '.net':
	print "Succes!"
	#opening source file
	f = open(str(sys.argv[1]),'r')
	#opening destination file
	f1 = open(str(sys.argv[2]), 'wb')

	
	f1.write('(PJD - Automatyka 1.09.2013) \n(net to BOM)\n\n')
	f1.write('Symbol\t-\tValue\t-\tlibrary\n')

	temp = []
	new_line = ''
	for line in f.readlines():
		
		if line[0:15] == '    (comp (ref ':
		#	f1.write(line[15:line.find(')')] + '\t-\t')
			new_line = line[15:line.find(')')] + '\t-\t'
		if line[0:13] == '      (value ':
		#	f1.write(line[13:line.find(')')] + '\t-\t')
			new_line += line[13:line.find(')')] + '\t-\t'
		if line[0:16] == '      (libsource':
		#	f1.write(line[line.find('(part ')+6:line.find('))')] + '\n')
			new_line += line[line.find('(part ')+6:line.find('))')] + '\n'
			temp.append(new_line)
			new_line = ''
	

	temp.sort()
	f.close()
	for line in temp:
		f1.write(line)
	f1.close()
	print "Have a nice day!"
	
	#print temp
else:
	print "#Err!! Wrong source file format. Should be .drl. \nFunction format is \ndrl2gcode.py source_file.drl destination_file.ngc"
	
