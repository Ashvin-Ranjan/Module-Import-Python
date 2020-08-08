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
	print(bcolors.FAIL + bcolors.BOLD + "FATAL ERROR" + bcolors.ENDC + bcolors.FAIL + ": " + message + bcolors.ENDC)
	exit()

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
				func = getattr(self, name)
			else:
				errormessage("COMMAND NOT FOUND")
		except:
			errormessage("COMMAND NOT FOUND")
			
		func(args)

	#args are arguments passed in as a list
	def imp(self, args):
		try:
			#Import library
			importlib.import_module(args[0])
		except:
			errormessage("ARGUMENTS INCORRECT")
			
		
	
	#args are arguments passed in as a list
	def add(self, args):
		try:
			#Add value to pointer index
			pointer = int(args[0])
			val = int(args[1])
			vals[pointer] += val
		except:
			errormessage("ARGUMENTS INCORRECT")
			
	
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
			errormessage("ARGUMENTS INCORRECT")
			
	
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
			errormessage("ARGUMENTS INCORRECT")
			
	
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
			errormessage("ARGUMENTS INCORRECT")
			

	#args are arguments passed in as a list
	def msg(self, args):
		try:
			#Get text from arguments
			txt = ""
			for i in args:
				txt += i

			#Find text in quotes
			txt = re.findall('"([^"]*)"', txt)[0].replace('\\n', '\n').replace('\\t', '\t')

			print(txt, end = "")
		except:
			errormessage("ARGUMENTS INCORRECT")
			
		
	
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
			errormessage("ARGUMENTS INCORRECT")
			

	




#Instansiate the class
com = CommandsBasic()

#Get values into the list
for i in range(256):
	vals.append(0)

#Declare commands
commands = []

#Fill commands list
if(len(sys.argv) == 1):
	with open("run.mip", "r") as f:
		commands = f.readlines()
else:
	with open(argv[1], "r") as f:
		commands = f.readlines()

#Go through all commands
for i in commands:

	for j in range(256):
		if(vals[j] > 255):
			vals[j] -= 256
		if(vals[j] < 0):
			vals[j] += 256

	#Split all commands
	args_unclean = i.strip().split(",")
	args = []
	comment = False

	#Clean args
	for arg in args_unclean:
		#Check if arg is a comment
		if(";" in arg):
			if(not comment and arg.strip().replace(" ", "").replace("\t", "").split(";")[0] != ""):
				args.append(arg.strip().replace(" ", "").replace("\t", "").split(";")[0])
			comment = True

		#Put cleaned args in list
		if arg.strip().replace(" ", "").replace("\t", "") != "" and not comment:
			args.append(arg.strip().replace(" ", "").replace("\t", ""))
		
	#Turns all invocations of variable values to actual values
	for n,arg in enumerate(args):
		for i in var.keys():
			args[n] = arg.replace("$" + i, str(var[i]))

	#Go through all commands
	if args != []:
		#If this does not call on a libaray then call the base function
		if(not "." in args[0]):
			com.callfunc(args[0], args[1:len(args)])
		#If this calls a library than go through and call the function
		else:
			#Get libary and command
			mod = args[0].split(".")
			found = False
			for j in sys.modules.keys():
				#If libaray is found than go though and call the function
				if mod[0] == j:
					#If function does not start with and underscore call it
					if(not mod[1].startswith("_")):
						found = True
						#Get command function
						command = getattr(sys.modules[j], mod[1])
						#Get the peramaters
						sig = signature(command).parameters

						if len(sig) == 1:
							#If the command takes in one argument then passes the args that that were passed in
							command(args[1:len(args)])

						elif len(sig) == 2:
							#If they request 2 args then pass in args and list of vals
							old = vals
							vals = command(args[1:len(args)], vals)

							#If the return value of the function is a list and is 256 values long then set that as the list of values
							if(vals == None or len(vals) != 256 or type(vals) != list):
								vals = old

						elif len(sig) == 3:
							oldval = vals
							vals = command(args[1:len(args)], vals, var)

							#If return value of function is a list and is 256 values long then set that as the list of values
							if(type(vals) == list and len(vals) == 256):
								pass

							#If the return value of function is a dictionary then set is as the list of variables
							elif(type(vals) == dict):
								var = vals
								vals = oldval

							#If the return value of the function is a tuple then run the for loop
							elif(type(vals) == tuple):
								tup = vals
								vals = oldval

								for n in tup:
									#If return value of n is a list and is 256 values long then set that as the list of values
									if(type(n) == list and len(vals) == 256):
										vals = n

									#If the return value of n is a dictionary then set is as the list of variables
									elif(type(n) == dict):
										var = n

							#Otherwise set nothing
							else:
								vals = oldval
					else:
						errormessage("COMMAND IS PRIVATE")
			#If the libary is not found then throw error.
			if(not found):
				errormessage("LIBRARY NOT FOUND")
