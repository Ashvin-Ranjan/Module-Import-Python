# Module Import Python
This is a modular coding language made in python where you can make your own modules in python too!

Version 1.2.0

## Dependancies
- colorama
- python 3.8

## How to use it

Run the python file with an argument that holds the name of the .mip file that is going to be run, here is an example:

```
py mip.py test.mip
```

If no file if given then it will automatically run run.mip.

## Documentation

### Base Commands
Commas(,) are used to seperate arguments.

Data is stored in variables or in a 256 length list which overflows after 255.

Variable values accessed by typing $*variable name*

Functions values are passed or run by typing &*function name*

- imp: 

usage: imp, [*libaray name*]

Imports the fellow python file and you are able to use the commands in it by using *library name*.*command*, [*arguments*]


- add:

usage: add, [*list location*], [*value to add*]

Adds the value to the list location, if adding 255 this will end up subtracting 1 from the pointer value


- outb:

usage: outb, [*list location*]

Prints out value in pointer as binary

usage: outb, -v, [*number*]

Prints out value in number as binary


- outd:

usage: outb, [*list location*]

Prints out value in pointer as decimal

usage: outb, -v, [*number*]

Prints out value in number as decimal

- outh:

usage: outb, [*list location*]

Prints out value in pointer as hex

usage: outb, -v, [*number*]

Prints out value in number as hex

- msg:

usage: msg, [*message in quotes*]

Prints out message text

- setv:

usage: setv, [*variable name in quotes*], [*list location*]

Puts number in list value into the variable

- func:

usage: func, [*function name*]

After this you are able to put in any functions afterwards and the decloration finishes when you type fin as a command

- runif:

usage: runif, [*condition*], [*function value (& then function name)*]

Runs the function if the condition evaluates to true, uses && || and !

- loop:

usage: loop, [*times*], [*function value (& then function name)*]

Run the function the amount of times specified

### Creating your own module
To create your own module you need to create a python file with functions.

The non private functions all require one arguement which is a list of the arguments passed in from the .mip program.

You also require variable called values and one called variables, which are updated and store the list of values and the dictionary of variables.

If the function returns a list then the list will be put in place of the list of values.

If the function returns a dictionary then the dictionary will be put in place of the variables.

If the function return as tuple then the list in the tuple and the dictionary will be assigned to their respective values as seen above.

Use and underscore(\_) at the beginging of the function if you do not want it to be callable from a program.

## Demos

In the folder "Demo" there is a simple demo program.

In the folder "Modules" there is a simple module.

## What changed?

- Added functions, if statements, and for loops.
