# Module Import Python
This is a modular coding language made in python where you can make your own modules in python too!

Version 1.0.0

## Dependancies
- colorama
- python 3.8

## Documentation

### Base Commands
Commas(,) are used to seperate arguments.
Data is stored in variables or in a 256 length list which overflows after 255.
Variable values accessed by typing $*variable name*

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

### Creating your own module
To create your own module you need to create a python file with functions.

In the functions you can have at least 1 argument up to 3 arguments.

The First argument are the values passed in by the program in a list of strings.

The Second argument is the list of 256 values that hold ints.

The Third argument is the dictionary of variables.

If the function returns a list then the list will be put in place of the list of values

If the function returns a dictionary then the dictionary will be put in place of the variables

## Demos

In the folder "Demo" there is a simple demo program

In the folder "Modules" there is a simple module.
