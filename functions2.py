#keyword arguments
def vac_feedback(vac, efficacy):
    print(f"{vac} vaccine is having {efficacy} % efficacy")
    if(efficacy > 50 ) and (efficacy <= 75):
        print("not effective")
    elif(efficacy > 75 ) and (efficacy < 90):
        print("It's effective")
    elif(efficacy > 90 ):
        print("sure shot")
    else:
        print("need more trials")
        
vac_feedback("pfizer", 80)
vac_feedback("covax", 40)
vac_feedback("covis", 95)
vac_feedback(efficacy=100, vac="sputnik")

print("+++++++++++++++++++")

#variable length arguments - *args(non keyword arguments)
def order_food(min_order, *args):
    print(f"you have ordered :{min_order}")
    #print(args)
    for item in args:
        print(f"you have ordered: {item}")
    print("delivered")
    
order_food("Salad","Pizza","Biryani","Soup")

print("==================")
#variable length arguments - **kwargs(keyword arguments)
"""
    Input : Multilple values for minutes , key= value pair activity
    output = return sum of minutes + random minutes spend on a random activity
"""
import random
def time_activity(*args , **kwargs):
    print(args)
    print(kwargs)
    min = sum(args) + random.randint(0,60)
    print(min)
    choice = random.choice(list(kwargs.keys()))
    print(choice)
    choiceVal = random.choice(list(kwargs.values()))
    print(choiceVal)
    
    print(f"You have to spend {min} minutes for {kwargs[choice]}")
    
 

time_activity (10, 20, 30, hobby = "Dance", sports = "boxing", fun = "driving", work = "Devops")

