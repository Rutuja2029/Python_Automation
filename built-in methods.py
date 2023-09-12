#built-in methods/functions

message = "corona vaccine is ready."
print(message)
print(message.capitalize())


#to print all built in functions for dataype
print(dir(""))
print(dir([]))
print(dir(()))
print(dir({}))

#======
print(message.upper())
Message = message.upper()
print(message.lower())
print(Message.islower())
 #-----------------
print(message.find("ready"))
print(message[18:22])
print(message.find("not"))

#===================
sequence = ("192","168","40","90")
print(".".join(sequence))
print("/".join(sequence))
print("***/&".join(sequence))

#===================
print("==============")

moutains = ["Eve", "him","sah","Alps","K2","Mt Hood"]
print(moutains)

moutains.append("nilgiri")
print(moutains)

moutains.extend(["aravali","sat"])
print(moutains)

moutains.insert(2, "Mt Abu")
print(moutains)

moutains.pop()
print(moutains)
moutains.pop()
print(moutains)
moutains.pop()
print(moutains)
moutains.pop(2)
print(moutains)


#===================
print("==============")

comp_emp1 = {"Name":"Santa","Skill":"Blockchain","Code":1024}
print(comp_emp1.keys())
print(comp_emp1.values())
comp_emp1.clear()
print(comp_emp1)
