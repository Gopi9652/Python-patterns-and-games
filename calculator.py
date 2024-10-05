import math as m

while True:
    a = int(input("a="))
    b = int(input("b="))
    print("****choose which operation you perform****")
    print("1.add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    print("5.mod(%)")
    print("6.square root")
    print("7.power")
    print("8.factorial")
    print("9.exponential")
    print("10.trigonometry")
    x = int(input("enter your choice: "))
    
    if x == 1:
        print("Result:", a + b)
    elif x == 2:
        print("Result:", a - b)
    elif x == 3:
        print("Result:", a * b)
    elif x == 4:
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Division by zero")
    elif x == 5:
        if b != 0:
            print("Result:", a % b)
        else:
            print("Error: Modulus by zero")
    elif x == 6:
        print("Result:", m.sqrt(a))
    elif x == 7:
        print("Result:", m.pow(a, b))
    elif x == 8:
        print("Result:", m.factorial(a))
    elif x == 9:
        print("Result:", m.exp(a))
    elif x == 10:
        print("Sine:", m.sin(m.radians(a)))
        print("Cosine:", m.cos(m.radians(a)))
        print("Tangent:", m.tan(m.radians(a)))
    else:
        print("Enter correct choice")
        break
