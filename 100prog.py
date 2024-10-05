"""
#Fahrenheit to Celsius 
F=float(input("enter temp in Fahrenheit:: "))
C=(F-32)/1.8
print(f"{C:.2f}")
"""
"""
#fact
n=int(input("enter number:: "))
a=1
for i in range(1,n+1):
    a=a*i
print(f"factorial of {n} is {a}")
"""
"""
#to calculate the sum and average of First n natural numbers by taking n as input from the user
n=int(input("Enter natural number:: "))
sum1=(n*(n+1))/2
print(f"sum of n natural numbers{int(sum1)}")
avg=sum1/n
print(f"avg of n natural numbers {avg}")
"""
"""
#will find all such numbers which are divisible by 7 but are not a multiple of 5
n=int(input("enter range:: "))
count=0
for i in range(1,n+1):
    if i%7==0 and i%5!=0:
        count+=1
        print(i,end=",")
print(f"\ntotal numbers are {count}")
"""
"""
n=int(input("enter number:: "))
sum1=0
for i in range(1,n+1):
    if i%2!=0:
        sum1+=(i*i)
        #print(i)
print(f"sum of  squares of numbers {sum1}")
"""
"""
n=input("enter data:: ")
char=0
num=0
for i in n:
    if i.isalpha():
        char+=1
    elif i.isdigit():
        num+=1
print(f"num {num}")
print(f"char {char}")
"""
"""
n=int(input("enter a num for mul table:: "))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")
"""
"""
#area of traiangle
base=float(input("enter base:: "))
height=float(input("enter height:: "))
area=1/2*base*height
print(area)
"""
"""
#largest number
a=int(input("enter a num:: "))
b=int(input("enter a num:: "))
c=int(input("enter a num:: "))
if a>b and a>c:
    print("a is largest number")
elif b>a and b>c:
    print("b is largest number")
else:
    print("c is largest number")
"""
"""
#day of the week
dict1={1:"mon",2:"tue",3:"wed",4:"thu",5:"fri",6:"sat",7:"sun"}
n=int(input("enter num of the week:: "))
print(dict1[n].upper())
"""
"""
#write a program to determine whether the character entered is a vowel or not by using logical operator
a=['a','e','i','o','u']
n=input("enter char:: ").lower()
if n in a:
    print("vowel")
else:
    print("not vowel")
"""
"""
#lower and upper count
n=input("enter string:: ")
upper=0
lower=0
for i in  n:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print(f"count of upper {upper}")
print(f"count of lower {lower}")        
"""
"""
#even or odd
n=int(input("enter num ::  "))
if n%2==0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")
"""
"""
#dict(q--- 16,17)
a = ['Codegnan','Saketh','Python'] 
b=[1,2,3]
dict1=dict(zip(b,a))
print(dict1)
n=int(input("enter data:: "))
if n in dict1:
    print(dict1[n])
else:
    print("value not found")
"""
"""
#dict update
a = {'sno':[1,2,3,4],'names':['Codegnan','Saketh','Python']}
b={'Gender':{'Male','Female'},'place':['Vijayawada','Mnglgiri']}
a.update(b)
print(a)
"""
"""
#dict with numbers as keys and there sq as value 
n=int(input("enter num:: "))
a=[]
b=[]
for i in range(1,n+1):
    a.append(i)
    b.append(i*i)
#print(a)
#print(b)
dict1=dict(zip(a,b))
print(dict1)
"""
"""
n=input("enter data sep with , :: ").split(",")
a=n
a.sort(reverse=False)
print(a)
"""
"""
#if all(int(digit) % 2 == 0 for digit in num_str):
for i in range(1000,3001):
    #count=0
    a=str(i)
    if all(int(j) % 2 == 0 for j in a):
            print(i,end=",")
"""
"""
#prime number
min1=int(input("min:: "))
max1=int(input("max:: "))

for i in range(min1,max1+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(f"it is prime number {i}")
    else:
        print(f"{i} is not a prime number")
"""
"""
#Python Program to display which letters are present in both the strings by accepting two strings from user
a=input("enter str:: ") 
b=input("enter str:: ")
for i in a:
    if i in b:
        print(i,end=",")
"""
"""
#factor of a given number
n=int(input("enter a num:: "))
for i in range(1,n+1):
    if n%i==0:
        print(i,end=",")
"""
"""
#Python program to count the even numbers in the list by accepting list as input from the user
a=list(map(int,input("enter numbers:: ").split()))
#print(a)
count=0
for i in a:
    if i%2==0:
        count+=1
print(f"even numbers count in list is {count}")
"""
"""
#a Python program which iterates the numbers from 1 to 50 (including 50).For multiples of 3 print "Codegnan" instead of number in output,and for the multiples of five print "Python". For numbers which are multiples of both three and five print "I love Codegnan". 
for i in range(1,50):
    if i%3==0:
        print("Codegnan")
    elif i%3==0 and i%5==0:
        print("I love Codegnan")
    elif i%5==0:
        print("python")
"""
"""
#Python program to convert month name to a number of days by accepting month name from the user
a=input("enter month name:: ").capitalize()
month_days = {
    "January": 31,
    "February": 28,  # Assuming non-leap year
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}
if a in month_days:
    print(f"{month_days[a]}days for {a}")
else:
    print("enter correct month")
"""
"""
#a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:14,7,5,33,22,8 Then, the output should be:['14', '7', '5', '33', '22', '8']      ('14', '7', '5', '33', '22', '8')

a=input("enter seq of comma-separated numbers::  ").split(",")
print(a)
b=set(a)
print(b)
"""
"""
#Write a Python Program to accept two numbers from user and find the sum and
product  of two numbers,your code should be in two lines only?

a,b=map(int,input("enter ::  ").split())
#print(a)
#print(b)
print(f"sum is =={a+b} and product is =={a*b}")
"""
"""
#a program that displays all leap years from 1900-2101 along with the count of leap years
a=0
b=0
for i in range(1900,2102):
    if i%400==0 and i%100==0:
        a+=1
        print(i)
    elif i%4==0 and i%100!=0:
        b+=1
        print(i)
print(f"count of leap years is {a+b}")
"""
"""
#Python Program to find the sum of values in the dictionary
a = {'Codegnan': 250,'Saketh':300,'Python':250,'Monday':200}
#b=list(a.values())
#print(sum(b))
#x=sum(a.values()) 
#print(x)
print(sum(a.values()))
"""
"""
#Python program to check a triangle is equilateral, isosceles or scalene by accepting 3 sides as input from the user
a,b,c=map(int,input("enter 3 sides:: ").split())
if a==b and b==c:
    print("An equilateral triangle ")
elif (a==b and b!=c) or (a!=b and b==c) or (a==c and c!=b):
    print("An isosceles triangle ")
elif ( a!=b and b!=c and c!=a):
    print("A scalene triangle ")
"""
"""
#Python Program to print the following pattern
n=int(input("enter number:: "))                  #1 22 333 4444 55555
for i in range(1,n+1):
    print(str(i)*i)
"""
"""
#Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the length of the given string is less than 3, leave it unchanged
a=input("enter str:: ")
if len(a)<=2:
    print(a)
elif "ing" in a:
    print(a+"ly")
elif "ing" not in a:
    print(a+"ing")
"""
"""
#Python program that takes multiple words as input from user (store in list) and return the longest word and the length of the longest one
a=input("enter multiple words with space:: ").split()
print(max(a))
print(a)
"""
"""
#Python program to remove the list values in the given dictionary
a  = {'Monday': [10, 20, 30], 'Tuesday': [20, 30, 40], 'Wednesday': [12,15,16,28],'Thursday':[52,12,36,6],
      'Friday':[15,16,28,9,25],'Saturday':[15,25,35,45]}
for i in a:
    a[i]=[]
print(a)
"""
"""
def sum_strings(num1, num2):
    # Convert the string inputs to integers
    result = int(num1) + int(num2)
    # Print the sum
    print("The sum is:", result)

# Example usage:
sum_strings("10", "20")  # Output: The sum is: 30
"""
"""
#f(x)  =  { 3x-1(x>1)    x+2(-1<=x<=1)         5x+3(x<=-1       }
x=int(input("number:: "))
if x>1:
    print(f"f(x)={3*x-1}")
elif (-1<=x<=1):
    print(f"f(x)=={x+2}")
elif x<=-1:
    print(f"f(x)=={5*x+3}")
"""
"""
#Accept Username and password as strings from user and validate username with password,such as if username and password are matching login success
d={"gopi":"1234","raj":"456","bhavana":"789"}
name=input("enter username::  ")
password=input("password:: ")
if name in d:
    if password in d[name]:
        print("login success")
    else:
        print("incorrect password")
else:
    print("enter correct credintials:: ")
"""
"""
#function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.
a=input("enter string with space:: ").split()
if len(a[0])>len(a[1]):
    print(a[0])
elif len(a[1])>len(a[0]):
    print(a[1])
else:
    print(a[0],a[1])
    
    OR
    
a, b = input("Enter two words separated by space: ").split()
if len(a) > len(b):
    print(a)
elif len(b) > len(a):
    print(b)
else:
    print(a, b)
"""
"""
#Define a function which can print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
a=7
x={i:i*i for i in range(1,a+1)}
print(x)
"""
"""
#a function which can generate a list where the values are square of numbers between 1 and 15 (both included). Then the function needs to print the first 5 and last 5 elements in the list.
y=15
x={i:i*i for i in range(1,y+1)}
for a,b in x.items():
   # print(a)
    #print(b)
    if a in range(1,5+1) or a in range(11,16):
        print(b)
        
        OR
def generate_squares():
    squares = [i**2 for i in range(1, 16)]
    print("First 5 elements:", squares[:5])
    print("Last 5 elements:", squares[-5:])

generate_squares()

"""
"""
#program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
n=int(input("enter num:: "))
x=0
for i in range(1,n+1):
    x+=i/(i+1)
print(f"{x:.2f}")
"""
"""
#Write a Function to generate all sentences where subject is in 
import random
a=["I", "You"] 
b=["Play", "Love"]
c=["Hockey","Cricket"]
A=10
while A>0:
    #print(i)
    x=random.choice(a)
    y=random.choice(b)
    z=random.choice(c)
    print(x," ",y," ",z)
    A-=1
"""
"""
#list [12,24,35,24,88,120,155,88,120,155], write a Function to print this list after removing all duplicate values with original order reserved.
a=[12,24,35,24,88,120,155,88,120,155]
a=list(set(a))
a.sort()
print(a)
"""
"""
#Function that accepts a string from user and gives the output of vowels in given string as list along with the length of the list
a=input("enter str:: ")
b=[]
for i in a:
    if i.lower() in ['a','e','i','o','u']:
        b.append(i)
        #b=list(set(b))
        #b.sort()
print(f"len of the str {len(a)}")
print(f"vowels in the str {b}")
"""
"""
#Create a Function which includes your name,age,designation and years of Experience,and assign a different name to the function and call it through the new name?
def gopi(name=1,age=1,desi=1,exp=1):
    print("yes helloo")
    print(age,name,desi,exp)
g=gopi  #assigning new name to fun()
g(2,4,6,7)
"""
"""
#a function for checking the speed of drivers
def speed_limit(n,i=10):
    if n<=70:
        print("Riding Well")
    elif n>=71:
        x=n-70
        a=x//5
        print(f"points:{a}")
        if a>10:
            print("License suspended")
n=int(input("enter a number:: "))
speed_limit(n)
"""
"""
#limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20
def num(n):
    if n<1:
        return
    elif n%3==0 or n%5==0:
        print(n,end=",")
    num(n-1)
num(5) 
"""
"""
#a Function to count the number of trailing zeros in an Integer?such as if your input is 12563000 output should be 3 as we have 3 zeros trailing

a=input("enter a num:: ")
if len(a)>3 and a[-3:]=="000":
    print("3 as we have 3 zeros trailing")
"""
"""
#fiba
n=int(input("enter a num:: "))
a=0
b=1
c=b 
print("c value:: ",c)
while n>a:
    a,b=b,c
    c=a+b
    print(a)
"""