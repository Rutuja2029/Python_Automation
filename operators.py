#Arithmatic op

x = 2
y = 5

total = x + y
print(total)

total = x /  y
print(total)

total = x *  y
print(total)

total = x -  y
print(total)

total = x %  y
print(total)

total = x **  y
print(total)


# Comaparision op

a = 30
b = 60

out = (a < b)
print(out)

out = (a > b)
print(out)

out = (a == b)
print(out)

out = (a != b)
print(out)

out = (a <= b)
print(out)

out = (a >= b)
print(out)

#Assignmnegt op

c = 0
d = 1

c+=d # c = c + d
print(c)

c-=d # c = c - d
print(c)

# logical op and/or/not

a = 40
b = 60
x = 2
y = 3

out = (a < b) or (x > y)
print(out)

out = (x > y) or (a < b)
print(out)

out = (a < b) and (x > y)
print(out)

out = (a < b) and (x < y)
print(out)

out = (a < b) and (x > y)
print(out)

out = not(x < y)
print(out)

out = not(x > y)
print(out)


#Membership op : in / not in
str1 = "iot"
num1= 8
first_tuple = (str1, "Devops", 47, num1, 1.5)
ans = "Devops" in first_tuple
print(ans);

ans = "Devops" not in first_tuple
print(ans);

ans = "Dev" not in first_tuple
print(ans);

#Identity operators : is / is not

a = 12
b = 15

result = a is b
print(result)

result = a is not b
print(result)

