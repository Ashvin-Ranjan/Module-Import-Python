import colorama

#Let color work on Windows
colorama.init()

#Declare values
values = []

#Declare variables
variables = {}

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
	print(bcolors.OKBLUE + bcolors.BOLD + "basetools.py, " + bcolors.ENDC + bcolors.FAIL + bcolors.BOLD + "FATAL ERROR" + bcolors.ENDC + bcolors.FAIL + ": " + message + bcolors.ENDC)
	exit()

#Subtract value from list index
#args is the list of arguments passed in
def subtract(args):
	try:
		pointer = int(args[0])
		val = int(args[1])
		values[pointer] -= val
		#Return list that is set for values
		return values
	except:
		errormessage("SUBTRACT ARGUMENTS INCORRECT")

def set(args):
	try:
		pointer = int(args[0])
		val = int(args[1])
		values[pointer] = val
		#Return list that is set for values
		return values
	except:
		errormessage("SET ARGUMENTS INCORRECT")

def mov(args):
	try:
		pointer = int(args[0])
		pointer2 = int(args[1])
		values[pointer2] = values[pointer]
		#Return list that is set for values
		return values
	except:
		errormessage("MOV ARGUMENTS INCORRECT")

def math(args):
	try:
		pointer = int(args[0])
		txt = ""
		for i in args[1:len(args)]:
			txt += i
		m = eval(txt)
		values[pointer] = m
		#Return list that is set for values
		return values
	except:
		errormessage("MOV ARGUMENTS INCORRECT")
