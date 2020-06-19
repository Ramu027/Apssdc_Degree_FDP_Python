# Predefine Functions
# user define Functions
# 1. without arg and without return value
# 2. without arg and with return type
# 3. with arg and without return value
# 4 with arg and with return value

# 1. default Arg
# 2.required Arg
#3. variable length Arg
# 4. Keyword Arg

# 1.  without arg and without return value
 # Example

# def funname(arg):
    # statements
'''def additng():
    a = int(input("enter a value"))
    b= int(input("enter b value"))
    print(a+b)
'''
'''def sub():
    c= int(input("enter c value"))
    d = int(input("enter d value"))
    e = c-d
    return e

def mul(a,b):
    print(a*b)
def div(a,b):
    c = a/b
    return c



def default(a=12,b=22,c=33):
    return a+b+c
def required(a,b,c):
    return a/b/c
def var_len(*a):
    s = 0
    for i in a:
        s+=i
    #print("sum of all the values is",s)'''
'''def keyword(name= 'Ramu',companey = 'Apssdc'):
    print(name,companey)
        
def keyword(**name):
    print(name)
    

def default(a,b,c):
    add = a+b+c
    sub = a-b-c
    mul = a*b*c
    
    return add,sub,mul
    print(add)

def abc(c,*b,a=10):
    print(a,b,c)


def isprime(a):
    if a == 1:
        return False
    else:
        for i in range(2,a):
            if a%i == 0:
                return False
        return True'''



'''def abc(c,*b,a=10):
    print(a,b,c)'''




'''# Strings -  group of characters
# denotes with ' or " or  is  a string
s = 'abc'
s = "abc"

# index is the postion of data'''

s = int(input("enter strng"))
if str(s) == str(s)[::-1]:
    print('given {} is palindrome'.format(s))
else:
    print("not")
    
    



