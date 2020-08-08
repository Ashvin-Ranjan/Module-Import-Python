import colorama

#Let color work on Windows
colorama.init()

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
#vals is the values that are storing numbers in the base code
def subtract(args, vals):
	try:
		pointer = int(args[0])
		val = int(args[1])
		vals[pointer] -= val
		#Return list that is set for values
		return vals
	except:
		errormessage("ARGUMENTS INCORRECT")
