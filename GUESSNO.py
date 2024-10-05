import random
print("****====> Welcome to guessing number challenge <====****")
no_of_times_attempt=0
a=random.randrange(1,50)
#print("print A: ",a)
while no_of_times_attempt<=7:
     print("It is your", no_of_times_attempt,"time")
     x=int(input("enter number: "))
     if a>x:
         print("you entered small number\n")
         print("the Difference is: ",(a-x))
     elif a<x:
         print("you entered big number\n")
         print("the Difference is: ",(x-a))
     else:
         print("You won\n")
         break
     no_of_times_attempt=no_of_times_attempt+1
print("====> '''***GAME OVER***''' <====")
