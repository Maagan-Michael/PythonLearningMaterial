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

## Counting inside string
#### Base form
`"string".count("")`
#### Examples
`"Hello World!".count("!")` => `1`  
`"This is an example".count("is")` => `2`  
`"wEIrD CAse StrING".lower().count("s")` => `2` #Function chaining to find an occurence inside mixed-case string
#### Explanation
Count occurences of substring inside another string.

## Boolean (bool) values
#### Base form
`False`\ `True`
#### Examples
`number1 >` \ `<` \ `>=` \ `<=`\ `==` \ `!=` `number2`  
`item in list`\ `string`  
`item not in list`\ `string`  
`True and False == False`  
`True and True == True`  
`True or False == True`
#### Explanation
Boolean values can have 2 states, either True or False. They can be used to create conditions.

## Conditions
#### Base form
```python
if bool:
    option1
elif bool:
    option2
else:
    default_option
```
#### Examples
```python
# condition1\condition2 are Boolean

if condition1:
    this will run only if condition1 is True
elif condition2:
    this will run only if condition1 is False AND condition2 is True
else:
    this will run if only if condition1 AND condition2 are False
```
#### Explanation
Conditions allow running certain code under certain conditions.

## Sorting a list
#### Base form 
`list.sort()`
`sorted(list)`
#### Examples
```python
ls = [4,2,5,1,3]
ls.sort()
print(ls)
```
`[5,4,3,2,1]`

```python
ls = [4,2,5,1,3]
ls2 = sorted(ls)
print(ls2)
```
`[5,4,3,2,1]`
#### Explanation
When you dont need the original list order use sort(). if you do need it, use sorted() and put the sorted list in a new variable