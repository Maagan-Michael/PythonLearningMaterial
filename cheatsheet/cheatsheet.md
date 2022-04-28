# MM Python cheat sheet

## Output
#### Base form
`print()`
#### Example
`print("Hello World!")` => `Hello World!`
#### Explanation
Send the desired output to the console.

## Input
#### Base form
`input()`
#### Example
`input("Enter your name: ")` => `Enter your name: _` (Waiting for interactive input)
#### Explanation
Allows receiving input from the console user for all sorts of operations.

## Casting
#### Base form
`int()` / `str()` / `float()`
#### Example
`int("1")` => `1`  
`str(1)` => `"1"`  
`float(1)` => `1.0`
#### Explanation
Conversion from string to integer, integer/float to string or integer to float.

## Slicing
#### Base form
`"string"[START:END:STEP]`
#### Examples
`"ABCD"[1:3]` => `BC`  
`"ABCDEFG"[1:-3]` => `BCD`  
`"ABCDEFGHIJKLM"[:4:-1]` => `MLKJIHGF`
#### Explanation
Some string slicing techniques.  
[START::] Represents the pointer location to begin with, negative numbers are counted from the end.  
[:END:] Represents the pointer location to end with, negative numbers are counted from the end.  
[::STEP] Represents the number of places for a step, negative numbers are reversing the order.  

## String casing manipulation
#### Base form
`"string".upper()` / `"string".lower()`
#### Examples
`"Python Course".upper()` => `PYTHON COURSE`  
`"Python Course".lower()` => `python course`  
`"wEIRD Case"[0].upper() + "wEIRD Case"[1:].lower()` => `Weird case`  
#### Explanation
Changing the entire string into either UPPERCASE or lowercase depending on the respective function.
