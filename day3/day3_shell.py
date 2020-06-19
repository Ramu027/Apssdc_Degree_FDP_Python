Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> additng()
enter a value3355534
enter b value4354354354
4357709888
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> sub()
enter c value49003849045809
enter d value8943454
49003840102355
>>> s= sub()
enter c value458745
enter d value4435
>>> s
454310
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> mul()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    mul()
TypeError: mul() missing 2 required positional arguments: 'a' and 'b'
>>> mul(24,27)
648
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> div(123,2)
61
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> div(123,2)
61.5
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> default()
67
>>> default(10)
65
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> default(c=20)
54
>>> default(10,20)
63
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> required()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    required()
TypeError: required() missing 3 required positional arguments: 'a', 'b', and 'c'
>>> required(12,34,34)
0.010380622837370243
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> required(10,5,2)
1.0
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> var_len(3,4,5,6)
18
>>> var_len(3,4,5,6,7)
25
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> var_len(3,4,5,6,7)
25
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> var_len(3,4,5,6,7)
sum of all the values is 25
>>> var_len()
sum of all the values is 0
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> var_len(3,4,5,6,7)
>>> var_len()
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> keyword()
Ramu Apssdc
>>> name = 'ravi'
>>> keyword()
Ramu Apssdc
>>> keyword(name= 'ravi')
ravi Apssdc
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> keyword(name= 'ravi')
{'name': 'ravi'}
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> keyword(name= 'ravi',companey = 'apssdc')
{'name': 'ravi', 'companey': 'apssdc'}
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========: 'apssdc'
>>> default(23,24,25)
(72, -26, 13800)
>>> a = default(23,24,25)
>>> a
(72, -26, 13800)
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> default(23,24,25)
(72, -26, 13800)
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> default(23,24,25)
72
(72, -26, 13800)
>>> a = default(23,24,25)
72
>>> a
(72, -26, 13800)
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> a = default(23,24,25)
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> abc()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    abc()
TypeError: abc() missing 2 required positional arguments: 'b' and 'c'
>>> abc(23,45)
10 23 45
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> abc(23,45)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    abc(23,45)
TypeError: abc() missing 1 required keyword-only argument: 'c'
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> abc(23,45)
10 (45,) 23
>>> abc(23,45,55)
10 (45, 55) 23
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> isprime(10)
False
>>> isprime(7)
True
>>> isprime(1)
True
>>> isprime(2)
True
>>> isprime(3)
True
>>> isprime(4)
False
>>> isprime(6)
False
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> isprime(1)
False
>>> isprime(3)
True
>>> isprime(4)
False
>>> isprime(6)
False
>>> for i in range(1,100):
	if isprime():
		print(i)

		
Traceback (most recent call last):
  File "<pyshell#55>", line 2, in <module>
    if isprime():
TypeError: isprime() missing 1 required positional argument: 'a'
>>> for i in range(1,100):
	if isprime(i):
		print(i)

		
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
>>> for i in range(1,100):
	if isprime(i):
		print(i,end=' ')

		
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
>>> sum = 0
>>> for i in range(1,100):
	if isprime(i):
		sum+=i

>>> sum
1060
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> abc(a= 20,4,34,56)
SyntaxError: positional argument follows keyword argument
>>> abc(20,4,34,56,a= 20)
20 (4, 34, 56) 20
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
>>> reg(10)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    reg(10)
  File "C:/Users/Ramu/Desktop/Python_FDP/day3_file.py", line 81, in reg
    return reg(a-1)
  File "C:/Users/Ramu/Desktop/Python_FDP/day3_file.py", line 81, in reg
    return reg(a-1)
  File "C:/Users/Ramu/Desktop/Python_FDP/day3_file.py", line 81, in reg
    return reg(a-1)
  [Previous line repeated 991 more times]
RecursionError: maximum recursion depth exceeded
>>> s = '''a'''
>>> s
'a'
>>> type(s)
<class 'str'>
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> s = 'Apssdc"
SyntaxError: EOL while scanning string literal
>>> s = 'Apssdc'
>>> s[0]
'A'
>>> s[1]
'p'
>>> s[4]
'd'
>>> s[-1=
      
SyntaxError: invalid syntax
>>> s[-1]
      
'c'
>>> s[-6]
      
'A'
>>> s[0:4]
      
'Apss'
>>> s[0:3]
      
'Aps'
>>> s[3:6]
      
'sdc'
>>> s[3:]
      
'sdc'
>>> s[:3]
      
'Aps'
>>> s[:]
      
'Apssdc'
>>> s[0:6:1]
      
'Apssdc'
>>> s[0:6:2]
      
'Asd'
>>> s[::2]
      
'Asd'
>>> s[0:6:-1]
      
''
>>> s[6:0:-1]
      
'cdssp'
>>> s[6:1:-1]
      
'cdss'
>>> s[6:-1:-1]
      
''
>>> s[6::-1]
      
'cdsspA'
>>> s[::-1]
      
'cdsspA'
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
enter strngramu
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
enter strngapssdc
not
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
enter strngaba
given string is palindrome
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
enter strngmam
given mam is palindrome
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
enter strng121
given 121 is palindrome
>>> f = 1.09
      
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
enter strng121
Traceback (most recent call last):
  File "C:/Users/Ramu/Desktop/Python_FDP/day3_file.py", line 90, in <module>
    if s == s[::-1]:
TypeError: 'int' object is not subscriptable
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
enter strng121
not
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
enter strng121
given 121 is palindrome
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
enter strng121
given 121 is palindrome
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
enter strng123
not
>>> 
=========== RESTART: C:/Users/Ramu/Desktop/Python_FDP/day3_file.py ===========
enter strng123
not
>>> s
      
123
>>> s[::-1]
      
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    s[::-1]
TypeError: 'int' object is not subscriptable
>>> str(s)[::-1]
      
'321'
>>> dir(str)
      
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> s = 'ApssDc'
      
>>> s.capitalize()
      
'Apssdc'
>>> s.casefold()
      
'apssdc'
>>> s
      
'ApssDc'
>>> s.upper()
      
'APSSDC'
>>> s
      
'ApssDc'
>>> s[0]
      
'A'
>>> s[0]='b'
      
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    s[0]='b'
TypeError: 'str' object does not support item assignment
>>> s.lower()
      
'apssdc'
>>> s = 'appsdc_fdp'
      
>>> s
      
'appsdc_fdp'
>>> s.center(20)
      
'     appsdc_fdp     '
>>> len(s)
      
10
>>> s.center(20,'*')
      
'*****appsdc_fdp*****'
>>> s.count('p')
      
3
>>> s.count('a')
      
1
>>> s.count('ap')
      
1
>>> s.startswith('a')
      
True
>>> s.endswith('a')
      
False
>>> s.find('a')
      
0
>>> s.find('p')
      
1
>>> s.find(z)
      
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    s.find(z)
NameError: name 'z' is not defined
>>> s.find('z')
      
-1
>>> s.find()
      
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    s.find()
TypeError: find() takes at least 1 argument (0 given)
>>> s.replace('a','A')
      
'Appsdc_fdp'
>>> s
      
'appsdc_fdp'
>>> s.replace('p','P')
      
'aPPsdc_fdP'
>>> s.index('p')
      
1
>>> s.index('z')
      
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    s.index('z')
ValueError: substring not found
>>> s.isupper()
      
False
>>> s
      
'appsdc_fdp'
>>> s.islower()
      
True
>>> s1 = '12abcd'
      
>>> s1.isdigit()
      
False
>>> s2='1234'
      
>>> s2.isdigit()
      
True
>>> s1 = '12abcd'
      
>>> s1.capitalize()
      
'12abcd'
>>> s1[2].capitalize()
      
'A'
>>> s[0:2]+s[2].capitalize()+s[3:]
      
'apPsdc_fdp'
>>> s1[0:2]+s1[2].capitalize()+s1[3:]
      
'12Abcd'
>>> s1[0:2]+s1[2].capitalize()+s1[3:]
      
'12Abcd'
>>> s
      
'appsdc_fdp'
>>> s1
      
'12abcd'
>>> s1.replace('a','A')
      
'12Abcd'
>>> 
