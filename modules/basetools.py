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
  print(bcolors.OKBLUE + bcolors.BOLD + "basetools.py, " + bcolors.ENDC + bcolors.FAIL + bcolors.BOLD + "FATAL ERROR" + bcolors.ENDC + bcolors.FAIL + ": " + message + bcolors.ENDC)
  exit()

def subtract(args, vals):
  try:
    pointer = int(args[0])
    val = int(args[1])
    vals[pointer] -= val
    return vals
  except:
    errormessage("ARGUMENTS INCORRECT")
