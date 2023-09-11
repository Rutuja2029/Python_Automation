
vaccines = ("Moderna","pfizer","sputnik")
for vac in vaccines:
    print(f"{vac} vaccine sprovides immuniazation")
    for i in vac:
        print(i)
        
    print("end of i loop")
print("end of vac loop")

#####
import time
x = 2
while True:
    print("value of x is: ", x)
    x *= 2
    time.sleep(2)
    
print("end of the code")