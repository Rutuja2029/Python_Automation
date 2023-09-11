# IF/elif/else Condition

x = 30

if(x < 30):
    print("Inside IF block")
    print("x is less than 30")
elif(x == 30):
    print("Inside else block")
    print("x is equal to 30")   
else:
    print("Inside else block")
    print("x is not less than 30")
    
#Find out match

devops = ["Jenkins", "Ansible"]
dev = ("Nodejs","Angularjs", "java")
comp_emp1 = {"Name":"Santa","Skill":"Blockchain","Code":1024}
comp_emp2 = {"Name":"Rocky","Skill":"AI","Code":1218}

usr_skill = input("Enter your desired skill: ")
#print(usr_skill)

#Check in the db if we have this skill
if usr_skill in devops:
    print(f"we have {usr_skill} in devops team.")
elif usr_skill in dev:
    print(f"we have {usr_skill} in dev team.")
elif (usr_skill in comp_emp1.values()) or (usr_skill in comp_emp2.values()) :
    print(f"we have employees with {usr_skill} skill in company")
else:
    print(f"{usr_skill} skill not found")
    print(f"please check if you have put {usr_skill} correctly ")