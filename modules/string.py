import colorama
import re

#Let color work on Windows
colorama.init()

#Declare variables
variables = {}

#Declare line
line = 0

#Declare all of the colors
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def _errormessage(message):
	print(bcolors.OKBLUE + bcolors.BOLD + "string.py, " + bcolors.ENDC + bcolors.FAIL + bcolors.BOLD + "FATAL ERROR: " + bcolors.ENDC + bcolors.FAIL + ": LINE " + str(line) + ", " + message + bcolors.ENDC)
	exit()

def length(args):
	try:
		var1 = re.findall('"([^"]*)"', args[0])[0].replace('\\n', '\n').replace('\\t', '\t')
		var2 = re.findall('"([^"]*)"', args[1])[0].replace('\\n', '\n').replace('\\t', '\t')
		variables[var1] = len(var2)
		return variables
	except:
		_errormessage("LENGTH ARGUMENTS INCORRECT")


def substring(args):
	try:
		if len(args) == 3:
			var1 = re.findall('"([^"]*)"', args[0])[0].replace('\\n', '\n').replace('\\t', '\t')
			var2 = re.findall('"([^"]*)"', args[1])[0].replace('\\n', '\n').replace('\\t', '\t')
			variables[var1] = var2[int(args[2])]
		else:
			var1 = re.findall('"([^"]*)"', args[0])[0].replace('\\n', '\n').replace('\\t', '\t')
			var2 = re.findall('"([^"]*)"', args[1])[0].replace('\\n', '\n').replace('\\t', '\t')
			variables[var1] = var2[int(args[2]):int(args[3])]
		return variables
	except:
		_errormessage("SUBSTRING ARGUMENTS INCORRECT")

def combine(args):
	try:
		var1 = re.findall('"([^"]*)"', args[0])[0].replace('\\n', '\n').replace('\\t', '\t')
		var2 = re.findall('"([^"]*)"', args[1])[0].replace('\\n', '\n').replace('\\t', '\t')
		var3 = re.findall('"([^"]*)"', args[2])[0].replace('\\n', '\n').replace('\\t', '\t')
		variables[var3] = var1 + var2
		return variables
	except:
		_errormessage("COMBINE ARGUMENTS INCORRECT") 

def setstring(args):
	try:
		var = re.findall('"([^"]*)"', args[0])[0].replace('\\n', '\n').replace('\\t', '\t')
		txt = ""
		for i in args[1:len(args)]:
			txt += i
		question = re.findall('"([^"]*)"', txt)[0].replace('\\n', '\n').replace('\\t', '\t')
		variables[var] = question
		return variables
	except:
		_errormessage("SETSTRING ARGUMENTS INCORRECT")
