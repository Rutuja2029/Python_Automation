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


