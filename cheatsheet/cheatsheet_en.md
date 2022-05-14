# MM Python cheat sheet

# **Base**
## Output
**Base Form**  
`print()`
**Example**  
`print("Hello World!")` => `Hello World!`
**Explanation**  
Send the desired output to the console.

## Input
**Base Form** 
`input()`
**Example**  
`input("Enter your name: ")` => `Enter your name: _` (Waiting for interactive input)
**Explanation**  
Allows receiving input from the console user for all sorts of operations.

## Casting
**Base Form**  
`int()` / `str()` / `float()`
**Example**  
`int("1")` => `1`  
`str(1)` => `"1"`  
`float(1)` => `1.0`
**Explanation**  
Conversion from string to integer, integer/float to string or integer to float.

# **Strings**
## Slicing
**Base Form**  
`"string"[START:END:STEP]`
**Example**  s
`"ABCD"[1:3]` => `BC`  
`"ABCDEFG"[1:-3]` => `BCD`  
`"ABCDEFGHIJKLM"[:4:-1]` => `MLKJIHGF`
**Explanation**  
Some string slicing techniques. works for lists, tuples and sets aswell  
[START::] Represents the pointer location to begin with, negative numbers are counted from the end.  
[:END:] Represents the pointer location to end with, negative numbers are counted from the end.  
[::STEP] Represents the number of places for a step, negative numbers are reversing the order.  

## String casing manipulation
**Base Form**  
`"string".upper()` / `"string".lower()`
**Example**  s
`"Python Course".upper()` => `PYTHON COURSE`  
`"Python Course".lower()` => `python course`  
`"wEIRD Case"[0].upper() + "wEIRD Case"[1:].lower()` => `Weird case`  
**Explanation**  
Changing the entire string into either UPPERCASE or lowercase depending on the respective function.

## Counting inside string
**Base Form**  
`"string".count("")`
**Example**  s
`"Hello World!".count("!")` => `1`  
`"This is an example".count("is")` => `2`  
`"wEIrD CAse StrING".lower().count("s")` => `2` #Function chaining to find an occurence inside mixed-case string
**Explanation**  
Count occurences of substring inside another string.

## other methods for strings
[Medthods for strings](https://www.programiz.com/python-programming/methods/string)


# **Conditions (if statements)**
## Boolean (bool) values
**Base Form**  
`False`\ `True`
**Example**  s
`number1 >` \ `<` \ `>=` \ `<=`\ `==` \ `!=` `number2`  
`item in list`\ `string`  
`item not in list`\ `string`  
`True and False == False`  
`True and True == True`  
`True or False == True`
**Explanation**  
Boolean values can have 2 states, either True or False. They can be used to create conditions.

## Conditions
**Base Form**  
```python
if bool:
    option1
elif bool:
    option2
else:
    default_option
```
**Example**  s
```python
# condition1\condition2 are Boolean

if condition1:
    this will run only if condition1 is True
elif condition2:
    this will run only if condition1 is False AND condition2 is True
else:
    this will run if only if condition1 AND condition2 are False
```
**Explanation**  
Conditions allow running certain code under certain conditions.

# **Lists**
## Adding\Removing an object from a list
**Base Form**   
`list.append()`
`list.pop()`
**Example**  s
```python
ls = ["Tony", "Ana", "Dan", "Dvora"]
ls.append("Hanna")
print(ls)
```
`["Tony", "Ana", "Dan", "Dvora", "Hanna"]`

```python
ls = ["Tony", "Ana", "Dan", "Dvora"]
index = ls.index("Ana")
ls.pop(index)
print(ls)
```
`["Tony", "Dan", "Dvora"]`
**Explanation**  
.append(object) adds the object you put in it to the end of the list as is shown.  
.pop(int) pops the item at the specified index, can be used with .index() to remove a specific item from the list

## Sorting a list
**Base Form**   
`list.sort()`
`sorted(list)`
**Example**  s
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
print(ls)
```
`[5,4,3,2,1]`  
`[4,2,5,1,3]`
**Explanation**  
When you dont need the original list order use sort(). if you do need it, use sorted() and put the sorted list in a new variable

## SUM/MIN/MAX values from a list
**Base Form**   
`sum(list)`
`min(list)`
`max(list)`

**Example**  s
```python
ls = [13,4,2,51,-1,3]
max_number = max(ls)
min_number = min(ls)
sum_of_list = sum(ls)
print(max_number)
print(min_number)
print(sum_of_list)
```
51  
-1  
72
**Explanation**  
these are 3 useful functions you can use on a list

## other methods for lists
[Medthods for lists](https://www.programiz.com/python-programming/methods/list)
