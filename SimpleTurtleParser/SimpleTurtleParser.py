import fileinput
import sys
import os.path
from turtle import *

'''			SIMPLE TURTLE PARSER
# == Parses files of the following format ==

 P 2 	# select pen 2
 D		# pen down
 W 2 	# draw went 2cm
 N 1 	# then north 1
 E 2	# then east 2
 S 1	# then back south
 U		# pen up

# ===========================================
'''

multiplier = 100
colours = ["red", "blue", "yellow", "green"]

def parseFile(file):
	if not(os.path.isfile(file)):
		print("No such file: "+file)
		return

	numOfLines = 0
	for line in fileinput.input(file):
		numOfLines += 1

		# Parse comments
		if len(line) < 1: 
			continue
		elif line[0] == '#':
			continue
		tokens = line.split()
		cmd = tokens[0]

		# Parse commands without arguments
		if cmd == 'D':
			down()
			continue
		elif cmd == 'U':
			up()
			continue
		elif len(tokens) < 2:
			print("Not enough arguments on line "+str(numOfLines))
			return
		if not(tokens[2].startswith("#")):
			print("Syntax error on line "+str(numOfLines))
			return

		# Parse commands with arguments
		arg = int(tokens[1])
		if cmd == 'P':
			color(colours[arg-1])
		elif cmd == 'N':
			setheading(90)
			forward(arg*multiplier)
		elif cmd == "S":
			setheading(270)
			forward(arg*multiplier)
		elif cmd == "E":
			setheading(0)
			forward(arg*multiplier)
		elif cmd == "W":
			setheading(180)
			forward(arg*multiplier)
	done()

# Main method
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Invalid number of arguments')		
		print('Syntax: ' + sys.argv[0]  + ' [FILENAME]')		
	else:
		degrees()
		parseFile(sys.argv[1])
		