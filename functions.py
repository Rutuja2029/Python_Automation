
def add(arg1, arg2):
    total = arg1 + arg2
    return total

num1 = input("Enter num1:")
num2 = input("Enter num1:")
out = add(num1, num2)
print(out)
print(add(num1,num2))


"""
def adder(arg1, arg2):
    total = arg1 + arg2
    print(total)
    #return NONE
    
print(adder(10,50))

"""
"""
##DOUBT --------------
def sum(arg):
    x = 0
    for i in arg:
        x = x + 1
    return x
#out = sum([10, 20, 30])
#print(out)

print(sum([10,20]))

"""   

#Default Argument

def greetings(MSG = "Morning"):
    print(f"Good {MSG}")
    print("Welcome")
    
greetings()

def greetings(MSG,TIME):
    print(f"Good {MSG}. It's {TIME}")
    print("Welcome")
  
str = "Morning" 
clock = "9:30"
greetings(str, clock)
