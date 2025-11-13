Python 3.13.6 (tags/v3.13.6:4e66535, Aug  6 2025, 14:36:00) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#bASIC BOOLEAN OPERATORS
b1 = False
b2 = True
type(b1)
<class 'bool'>
type(b2)
<class 'bool'>
int("1")
1
int(1.0)
1
int(True)
1
int("0')
    
SyntaxError: unterminated string literal (detected at line 1)
int("1")
    
1
int("0")
...     
0
>>> int(0.0)
...     
0
>>> int(False)
...     
0
>>> #-----
...     
>>> # Not Operator
...     
>>> c = not b1
...     
>>> print('c',c)
...     
c True
>>> print('c:',c)
...     
c: True
>>> c = not b2
...     
>>> print('c:', c)
...     
c: False
>>> #-----0-----------------------
...     
>>> #or operator
...     
>>> c = b1 or b1
...     
>>> print('c:',c)
...     
c: False
>>> c = b1 or b2
...     
>>> print('c:',c)
...     
c: True
