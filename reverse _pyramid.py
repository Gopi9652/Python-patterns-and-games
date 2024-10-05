n=int(input("enter a number:")) #index no starting with one
for i in range(1,n+1):
    stars=("*"*(n*2-i*2+1))
    space=(" "*i)
    print(space+stars)


"""
#index no starting with 0
n=int(input("enter a number:"))
for i in range(0,n):
    stars=("*"*(n*2-i*2-1))
    space=(" "*i)
    print(space+stars)

"""
