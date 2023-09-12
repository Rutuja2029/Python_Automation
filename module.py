import random

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


#========================================

#variable length arguments - *args(non keyword arguments)
def order_food(min_order, *args):
    print(f"you have ordered :{min_order}")
    #print(args)
    for item in args:
        print(f"you have ordered: {item}")
    print("delivered")
    




#========================================

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
    
 




#=======================================================
