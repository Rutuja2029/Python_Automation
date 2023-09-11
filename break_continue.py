#Break

for i in "devops":
    print(i)
    if i == "o" :
        print("found data")
        break
print("out of i")

#Continue

for i in "devops":
    if i == "o" :
        #print("found data")
        continue
    print(f"value of i is {i}")
print("out of i")

#------------------------
print("===============================")
import random
vaccines = ["Moderna","pfizer","sputnik","covaxin","derma","garnier"]

random.shuffle(vaccines)
print(vaccines)

lucky = random.choice(vaccines)
print(lucky)

print("===============================")
"""
for vac in vaccines:
    print(f"************testing vaccine {vac}")
    if vac == lucky:
        print("#####")
        print(f"{lucky} vaccines, test success")
        break
print("end")
"""
print("===============================")

for vac in vaccines:
    print(f"************testing vaccine {vac}")
    if vac == lucky:
        print("#####")
        #continue
        print(f"{lucky} vaccines, test success")
        break
    print("test failed")   
print("end")
