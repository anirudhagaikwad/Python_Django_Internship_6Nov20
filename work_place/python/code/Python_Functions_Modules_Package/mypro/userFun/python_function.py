# Userdefine function


def addition():
    x=10
    y=20
    print("Function without arg & return type :: \n 10+20 = ",(x+y))

addition()   # call function

def subtraction(x,y):
    print("Function with arg & no return type :: \n X-Y = ",(x-y))


subtraction(10,3) # call function  


def multiplication(x,y):
    result=x*y
    print("Function with arg & with return type :: \n X*Y = ",result)
    return result

z=multiplication(3,3)    

print("return value -> result = ",z)


def devid():
    return (10/2)

d=devid()
print("devid() return value is = ",d)    







