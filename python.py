x=0

# first program
"""
this is comment
"""
'''
this is comment
'''
print("Welcome Hello")
print()

if x == 0:
    print("In the If block")
    print("value of x is 0")
else:
    print("In the else block")
    print("value of x is not equal to zero")
    
print()
print("This statement is out of if/else block")

#Variables
var1 = "Python"
var2 = 75
var3 = 3.5

#printing Variables
print( var1 , var2 , var3)

str1 = "alpha"
num1 = 4.5
#List/ collection of multi datatypes
first_list = [str1,"Devops",47, num1, 1.5]
print(first_list)
"""
You can edit list but not tuple
list => mutable
tuple => immutable
"""
#Tuple /collection of multidatatypes
first_tuple = (str1,"Devops",47, num1, 1.5)
print(first_tuple)

#Dictionary => {Key:value pairs}, curly braces
first_dictionary = {"Name":"Rutuja", "Weight":"62.4","Exercises":["Boxing","Dancing","Jogging","lifting"]}
print(first_dictionary)

#Boolean
x = True
y = False
print(x, y , type(x), type(y))

#print format
name = "cov_2"
dieases ="covid19"

print("The name is", name)
print("The name of virus is {}".format(name))

print("{} is the name of virus is {}".format(name, dieases))
print(f"The name of virus is {name} and it causes {dieases}")

#concat
print("The name of virus is " + name)