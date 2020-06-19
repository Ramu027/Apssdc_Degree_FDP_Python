'''for i in range(10,0,-2):
    print(i,end=" ")
'''
# sum of even nums b/w 1 to 100
'''sum = 0
for i in range(2,100,2):
    print(i)
    sum+=i
print(sum)'''
'''sum = 0
for n in range(1,100):
    if n%2==0:
        sum+=n
print(sum)'''



#while condition:
 #   //Statements

'''n = 1
while n<=5:
    print(n)
    n=n+1'''

'''number = int(input("enter number")) #123
rem = 0 
while number>0:#t t t 
    m = number%10 #3 2 1
    rem = 10*rem+m #3 32 321
    number = number//10#12 1 0
print(rem)'''

# Break And Continue
'''for i in range(1,10):
    print(i)
    if i==5:
        break'''
'''for i in range(1,10):
    if i == 6:
        continue
        print(i)'''
# marks 100 to 90 A grade
# 70 to 89 B grade
# 50 to 69 c grade
# 40 to 49 D grade
# 0 to 39 Fail
# above 100 or below 0 it willshow invalid marks

'''marks  = int(input("enter marks"))
if marks<=100 and marks>=90:
    print("A grade")
elif marks<90 and marks>=70:
    print("B grade")
elif marks<70 and marks>=50:
    print("c grade")
elif marks<50 and marks>=40:
    print("d grade")
elif marks>0 and marks<40:
    print("Fail")
else:
    print('invalid marks')'''
'''n = int(input("enter number"))
for i in range(1,n):
    if i%7==0:
        if i%9==0:
            print(i)'''

# predefine
# user Define
#range(init,fin,diff)
# def
# With out Arg and Without return
#With out Arg and With return
# With  Arg and Without return
#With Arg and With return

# def functionname (arg):
  # Statements

'''def adition(a,b):
    return a+b
x= 10
y = 20
res = adition(x,y)
print(res)'''

'''def type1():
    a = int(input("enter a number"))
    b= int(input("enter b number"))
    print(a%b)'''
'''def type2():
    x = 23
    y = 57
    return y-x'''
'''def type3(a,b,c):
    print(a+b+c)'''

# Default arg
# required arg
#keyword Agr
# Var length Arg

'''def add(y,y=10,x=20):
    print(x+y)'''

def req(y,x=10,z=20):
    print(x+y+z)




    
    
    
