planet1 = "Closet of Sun"
print(planet1)
print(planet1[0])
print(planet1[1])
print(planet1[6])
print(planet1[-1])
print(planet1[-2])
print(planet1[-3])

#Slicing a string , get substring from string

print(planet1[0:4])
print(planet1[-2:-1]) 
print(planet1[4:-1])
print(planet1[:7])
print(planet1[11:])

"""
#slicing in tuple
devops=("Linux", "Vagrant", "Bash Scripting","AWS","Jenkins","Python", "Ansible")
print(devops)
print(devops[0])
print(devops[3])
print(devops[6])
print(devops[-3])
print(devops[-1])
print(devops[0:3])
print(devops[-3:-1])
print(devops[2:-1])
print(devops[2:5][0])
print(devops[2:5][0][5:11])
print(devops[2:5][0][5:11][-1])

"""
##slicing in list
devops=["Linux", "Vagrant", "Bash Scripting","AWS","Jenkins","Python", "Ansible"]
print(devops)
print(devops[0])
print(devops[3])
print(devops[6])
print(devops[-3])
print(devops[-1])
print(devops[0:3])
print(devops[-3:-1])
print(devops[2:-1])
print(devops[2:5][0])
print(devops[2:5][0][5:11])
print(devops[2:5] [0][5:11][-1])

# slicing in dictionary using key
skills = {"devops": ("Linux", "Vagrant", "Bash Scripting","AWS","Jenkins","Python", "Ansible"),"dev":["Java", "NodeJS"]}
print(skills)

print(skills["devops"])
print(skills["dev"])

print(skills["devops"][-1])
print(skills["devops"][-1][:3])