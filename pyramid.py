n=int(input("enter number:: "))
for i in range(1,n+1):
    space=" "*(n-i)
    stars="*"*(i*2-1)
    print(space+stars)
