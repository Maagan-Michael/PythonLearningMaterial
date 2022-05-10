# שליף קורס פיית׳ון מעגן מיכאל

## פלט
#### צורת הבסיס
`print()`
#### דוגמה
`print("Hello World!")` => `Hello World!`
#### הסבר
שליחת הפלט הרצוי למסוף.

## קלט
#### צורת הבסיס
`input()`
#### דוגמה
`input("Enter your name: ")` => `Enter your name: _` (בהמתנה לקלט מהמשתמש)
#### הסבר
מאפשר קבלת קלט מהמסוף לשלל פעולות.

## המרה
#### צורת הבסיס
`int()` / `str()` / `float()`
#### דוגמה
`int("1")` => `1`  
`str(1)` => `"1"`  
`float(1)` => `1.0`
#### הסבר
המרה ממחרוזת למספר שלם, מספר שלם/שבר עשרוני למחרוזת או מספר שלם לשבר עשרוני.

## חיתוך
#### צורת הבסיס
`"string"[START:END:STEP]`
#### דוגמאות
`"ABCD"[1:3]` => `BC`  
`"ABCDEFG"[1:-3]` => `BCD`  
`"ABCDEFGHIJKLM"[:4:-1]` => `MLKJIHGF`
#### הסבר
מגוון טכניקות לחיתוך מחרוזות.  

&rlm;&lrm;[START::]&rlm; מציינת את מיקום ההתחלה למצביע, ערכים שליליים נספרים מהסוף.  
&rlm;&lrm;[:END:]&rlm; מציינת את מיקום הסוף למצביע, ערכים שליליים נספרים מהסוף.  
&rlm;&lrm;[::STEP]&rlm; מייצגת את מספר המקומות לצעד, מספרים שליליים הופכים את הסדר.

## שינוי אותיות קטנות/גדולות
#### צורת הבסיס
`"string".upper()` / `"string".lower()`
#### דוגמאות
`"Python Course".upper()` => `PYTHON COURSE`  
`"Python Course".lower()` => `python course`  
`"wEIRD Case"[0].upper() + "wEIRD Case"[1:].lower()` => `Weird case`  
#### הסבר
החלפת המחרוזת כולה באותיות גדולות או קטנות בהתאם לפונקציה הרצויה.

## ספירה בתוך מחרוזת
#### צורת הבסיס
`"string".count("")`
#### דוגמאות
`"Hello World!".count("!")` => `1`  
`"This is an example".count("is")` => `2`  
`"wEIrD CAse StrING".lower().count("s")` => `2` #שרשור של פונקציות לחיפוש תת־מחרוזת בתוך מחרוזת עם אותיות גדולות וקטנות
#### הסבר
ספירת תת־מחרוזות בתוך מחרוזת נוספת.

## ערך בוליאני
#### צורת הבסיס
`False`\ `True`
#### דוגמאות
`number1 >` \ `<` \ `>=` \ `<=`\ `==` \ `!=` `number2`  
`item in list`\ `string`  
`item not in list`\ `string`  
`True and False == False`  
`True and True == True`  
`True or False == True`
#### הסבר
לערך בוליאני יש 2 מצבים, אמת או שקר. בעזרתם אפשר ליצור תנאים.

## תנאים
#### צורת הבסיס
```python
if bool:
    option1
elif bool:
    option2
else:
    default_option
```
#### דוגמה
```python
# condition1\condition2 are Boolean

if condition1:
    this will run only if condition1 is True
elif condition2:
    this will run only if condition1 is False AND condition2 is True
else:
    this will run if only if condition1 AND condition2 are False
```
#### הסבר
תנאים מאפשרים לבחור אילו קטעי קוד יופעלו בתנאים מסוימים.

## סידור רשימה
#### צורת הבסיס
`list.sort()`
`sorted(list)`
#### דוגמאות
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
#### הסבר
 סידור הרשימה. השתמשו ב-sort כאשר אין לכם צורך בסדר המקורי שהיה לרשימה
