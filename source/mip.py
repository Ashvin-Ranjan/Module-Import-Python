#Imports
import types
import re
import importlib
import sys
from inspect import signature
import colorama

#Make sure that colors work on windows too
colorama.init()

#Text colors
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

#Function to call error message
def errormessage(message):
	print(bcolors.FAIL + bcolors.BOLD + "FATAL ERROR" + bcolors.ENDC + bcolors.FAIL + ": LINE " + str(line) + ", " + message + bcolors.ENDC)
	exit()

#Variables for declaring functions
funcname = ""

infunc = False

#Dictonary of functions
funcs = {}

#Imported libaries list
imps = []

#Declare vals, the list of numbers this is based off of
vals = []

#Declare variables
var = {}

#Declare commands class
class CommandsBasic:
	def __init__(self):
		pass
	
	#Call function based on name
	#args are arguments passed in
	#name is name of function
	def callfunc(self, name, args):
		try:
			#Check if function is not this function
			if(name != "callfunc"):
				if(not infunc):
					fun = getattr(self, name)
					fun(args)					
				else:
					txt = name
					for arg in args:
						txt += "," + arg 
					self.func([txt, funcname])
			else:
				errormessage("COMMAND \"" + name + "\" NOT FOUND")
		except:
			errormessage("COMMAND \"" + name + "\" NOT FOUND")
	
	#args are arguments passed in as a list
	def loop(self, args):
		try:
			for i in range(int(args[0])):
				if args[1].startswith("&"):
					for comm in funcs[args[1][1:len(args[1])]]:
						runcommand(comm)
				else:
					errormessage("LOOP FUNCTION INCORRECT")

		except:
			errormessage("LOOP ARGUMENTS INCORRECT")

	#args are arguments passed in as a list
	def runif(self, args):
		try:
			if(eval(args[0].replace('&&', 'and').replace('||', 'or').replace('!', 'not '))):
				if(args[1].startswith("&")):
					for comm in funcs[args[1][1:len(args[1])]]:
						runcommand(comm)
				else:
					errormessage("RUNIF FUNCTION INCORRECT")

		except:
			errormessage("RUNIF ARGUMENTS INCORRECT")


	#args are arguments passed in as a list
	def func(self, args):
		global infunc, funcname
		try:
			if(not infunc):
				infunc = True
				funcname = args[0]
				funcs[args[0]] = []
			else:
				if(args[0] != "fin"):
					funcs[args[1]].append(args[0])
				else:
					infunc = False
		except:
			errormessage("FUNC ARGUMENTS INCORRECT")


	#args are arguments passed in as a list
	def imp(self, args):
		try:
			#Import library
			importlib.import_module(args[0])
			imps.append(args[0])
		except:
			errormessage("IMP ARGUMENTS INCORRECT")
			
		
	
	#args are arguments passed in as a list
	def add(self, args):
		try:
			#Add value to pointer index
			pointer = int(args[0])
			val = int(args[1])
			vals[pointer] += val
		except:
			errormessage("ADD ARGUMENTS INCORRECT")
			
	
	#args are arguments passed in as a list
	def outb(self, args):
		try:
			#If first argument is -v than print out value of second arugment in binary
			if(args[0] == "-v"):
				print(bin(int(args[1])), end="")
			else:
				#Otherwise print out value of index in binary
				print(bin(vals[int(args[0])]), end="")
		except:
			errormessage("OUTB ARGUMENTS INCORRECT")
			
	
	#args are arguments passed in as a list
	def outd(self, args):
		try:
			#If first argument is -v than print out value of second arugment
			if(args[0] == "-v"):
				print(int(args[1]), end="")
			else:
				#Otherwise print out value of index
				print(vals[int(args[0])], end="")
		except:
			errormessage("OUTD ARGUMENTS INCORRECT")
			
	
	#args are arguments passed in as a list
	def outh(self, args):
		try:
			#If first argument is -v than print out value of second arugment in hex
			if(args[0] == "-v"):
				print(hex(int(args[1])), end="")
			else:
				#Otherwise print out value of index in hex
				print(hex(vals[int(args[0])]), end="")
		except:
			errormessage("OUTH ARGUMENTS INCORRECT")
			

	#args are arguments passed in as a list
	def msg(self, args):
		try:
			#Get text from arguments
			txt = ""
			for i in args:
				txt += ", " + i

			#Find text in quotes
			txt = re.findall('"([^"]*)"', txt)[0].replace('\\n', '\n').replace('\\t', '\t')

			print(txt, end = "")
		except:
			errormessage("MSG ARGUMENTS INCORRECT")
			
		
	
	#args are arguments passed in as a list
	def setv(self, args):
		try:
			#Get variable name
			txt = ""
			if len(args) > 2:
				for i in range(0, len(args)-1):
					txt += args[i]
			else:
				txt = args[0]

			#Get name in between quotes
			args[0] = re.findall('"([^"]*)"', txt)[0]

			#Set Variable
			var[args[0]] = vals[int(args[len(args)-1])]
		except:
			errormessage("SETV ARGUMENTS INCORRECT")
			

	


line = 0

#Instansiate the class
com = CommandsBasic()

#Get values into the list
for i in range(256):
	vals.append(0)

#Declare commands
commands = []

#Fill commands list
if(len(sys.argv) == 1):
	with open("run.mip", "r", encoding="utf-8") as f:
		commands = f.readlines()
else:
	with open(sys.argv[1], "r", encoding="utf-8") as f:
		commands = f.readlines()

def runcommand(command):
	global infunc, funcs, imps, vals, var

	for j in range(256):
		if(vals[j] > 255):
			vals[j] -= 256
		if(vals[j] < 0):
			vals[j] += 256

	#Split all commands
	args_unclean = command.strip().split(",")
	args = []
	comment = False

	#Clean args
	for arg in args_unclean:
		cleanarg = arg.replace("\t", "")
		if(not "\"" in cleanarg):
			cleanarg = cleanarg.strip().replace(" ", "")
		#Check if arg is a comment
		if(";" in arg):
			if(not comment and cleanarg.split(";")[0] != ""):
				args.append(cleanarg.split(";")[0])
			comment = True

		#Put cleaned args in list
		if cleanarg != "" and not comment:
			args.append(cleanarg)
	
	for arg in args:
		if "⁒" in arg:
			errormessage("⁒ IS NOT ALLOWED")
			exit()

	for n,arg in enumerate(args):
		args[n] = arg.replace("\\$", "⁒")

	
	#Turns all invocations of variable values to actual values
	for n,arg in enumerate(args):

		for i in var.keys():
			args[n] = args[n].replace("$" + i, str(var[i]))
			

	for n,arg in enumerate(args):
		args[n] = arg.replace("⁒", "\\$")

	#Set modules variables
	for j in imps:
		try:
			sys.modules[j].variables = var
		except:
			pass

		try:
			sys.modules[j].values = vals
		except:
			pass

		try:
			sys.modules[j].imports = imps
		except:
			pass

		try:
			sys.modules[j].functions = funcs
		except:
			pass

		try:
			sys.modules[j].line = line
		except:
			pass

	#Go through all commands
	if args != []:
		if(args[0].startswith("&")):
			for comm in funcs[args[0][1:len(args[0])]]:
				runcommand(comm)

		#If this does not call on a libaray then call the base function
		elif(not "." in args[0] or infunc):
			com.callfunc(args[0], args[1:len(args)])
		#If this calls a library than go through and call the function
		else:
			#Get libary and command
			mod = args[0].split(".")
			found = False
			for j in imps:
				#If libaray is found than go though and call the function
				if mod[0] == j:
					#If function does not start with and underscore call it
					if(not mod[1].startswith("_")):
						found = True
						try:
							#Get command function
							command = getattr(sys.modules[j], mod[1])
							
							#Run Command
							command(args[1:len(args)])

							try:
								#Do a check then if it passes set values in the library to program values
								if(type(sys.modules[j].values) == list and len(vals) == 256 and all(isinstance(x, int) for x in vals)):
									sys.modules[j].values
							except:
								pass

							try:
								#Do a check then if it passes set variables in the library to program variables
								if(type(sys.modules[j].variables) == dict):
									var = sys.modules[j].variables
							except:
								pass

							try:
								#Do a check then if it passes set imports in the library to program imports
								if(type(sys.modules[j].imports) == dict):
									imps = sys.modules[j].imports
							except:
								pass

							try:
								#Do a check then if it passes set functions in the library to program functions
								if(type(sys.modules[j].functions) == dict):
									funcs = sys.modules[j].functions
							except:
								pass


						except:
							errormessage("LIBRARY COMMAND \"" + mod[1] + "\" NOT FOUND")
					else:
						errormessage("LIBRARY COMMAND \"" + mod[1] + "\" IS PRIVATE")
			#If the libary is not found then throw error.
			if(not found):
				errormessage("LIBRARY \"" + mod[0] + "\" NOT FOUND")


#Go through all commands
for i,command in enumerate(commands):
	line = i + 1
	runcommand(command)
	
