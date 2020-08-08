import types
import re
import importlib
import sys
from inspect import signature
import colorama

colorama.init()

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def errormessage(message):
	print(bcolors.FAIL + bcolors.BOLD + "FATAL ERROR" + bcolors.ENDC + bcolors.FAIL + ": " + message + bcolors.ENDC)
	exit()

def imports():
	out = []
	for name, val in globals().items():
		if isinstance(val, types.ModuleType):
			out.append(val)

	return out

#Delcare imps and class

#Declare vals, the list of numbers this is based off of
vals = []

#Declare variables
var = {}

#Declare commands class
class CommandsBasic:
	def __init__(self):
		pass
	
	def callfunc(self, name, args):
		try:
			func = getattr(self, name)
		except:
			errormessage("COMMAND NOT FOUND")
			
		func(args)

	def imp(self, args):
		try:
			importlib.import_module(args[0])
		except:
			errormessage("ARGUMENTS INCORRECT")
			
		
	
	def add(self, args):
		try:
			pointer = int(args[0])
			val = int(args[1])
			vals[pointer] += val
		except:
			errormessage("ARGUMENTS INCORRECT")
			
	
	def outb(self, args):
		try:
			if(args[0] == "-v"):
				print(bin(int(args[1])), end="")
			else:
				print(bin(vals[int(args[0])]), end="")
		except:
			errormessage("ARGUMENTS INCORRECT")
			
	
	def outd(self, args):
		try:
			if(args[0] == "-v"):
				print(int(args[1]), end="")
			else:
				print(vals[int(args[0])], end="")
		except:
			errormessage("ARGUMENTS INCORRECT")
			
		
	def outh(self, args):
		try:
			if(args[0] == "-v"):
				print(hex(int(args[1])), end="")
			else:
				print(hex(vals[int(args[0])]), end="")
		except:
			errormessage("ARGUMENTS INCORRECT")
			

	def msg(self, args):
		try:
			txt = ""
			for i in args:
				txt += i
			
			txt = re.findall('"([^"]*)"', txt)[0].replace('\\n', '\n').replace('\\t', '\t')
			print(txt, end = "")
		except:
			errormessage("ARGUMENTS INCORRECT")
			
		
	
	def setv(self, args):
		try:
			txt = ""
			if len(args) > 2:
				for i in range(0, len(args)-1):
					txt += args[i]
			else:
				txt = args[0]
			args[0] = re.findall('"([^"]*)"', txt)[0]
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

#Go through all
for i in commands:

	for j in range(256):
		if(vals[j] > 255):
			vals[j] -= 256
		if(vals[j] < 0):
			vals[j] += 256

	#split all commands
	args_unclean = i.strip().split(",")
	args = []
	comment = False

	#clean args
	for arg in args_unclean:
		if(";" in arg):
			if(not comment and arg.strip().replace(" ", "").replace("\t", "").split(";")[0] != ""):
				args.append(arg.strip().replace(" ", "").replace("\t", "").split(";")[0])
				
			comment = True

		if arg.strip().replace(" ", "").replace("\t", "") != "" and not comment:
			args.append(arg.strip().replace(" ", "").replace("\t", ""))
		
	#changesvars
	for n,arg in enumerate(args):
		for i in var.keys():
			args[n] = arg.replace("$" + i, str(var[i]))

	#Go through all commands
	if args != []:
		if(not "." in args[0]):
			com.callfunc(args[0], args[1:len(args)])
		else:
			mod = args[0].split(".")
			found = False
			for j in sys.modules.keys():
				if mod[0] == j:
					found = True
					command = getattr(sys.modules[j], mod[1])
					sig = signature(command).parameters
					if len(sig) == 1:
						command(args[1:len(args)])
					elif len(sig) == 2:
						old = vals
						vals = command(args[1:len(args)], vals)
						if(vals == None or len(vals) != 256 or type(vals) != list):
							vals = old
					elif len(sig) == 3:
						oldval = vals
						vals = command(args[1:len(args)], vals, var)
						if(type(vals) == list and len(vals) == 256):
							pass
						elif(type(vals) == dict):
							var = vals
							vals = oldval
						else:
							vals = oldval
			
			if(not found):
				errormessage("LIBRARY NOT FOUND")
