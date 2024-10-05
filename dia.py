n=int(input("enter a number:"))
for i in range(1,n+1):
    space1=" "*(n-i)
    stars1="*"*(i*2-1)
    print(space1+stars1)
for i in range(1,n):
    stars=("*"*(n*2-i*2-1))
    space=(" "*(i))
    
    print(space+stars)
   
