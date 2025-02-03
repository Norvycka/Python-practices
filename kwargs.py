#variable length arguments *args (keyword arguments)

import random

def time_activity(*args, **kwargs):
    """
    Input: multiple values for minutes, key=value pair activity
    Output: return sum of minutes + random minute aspect on a random activity
    """
    #print(args)
    #print(kwargs)
    min = sum(args) + random.randint(0,60)
    #print(min)
    choice = random.choice(list(kwargs.keys()))
    #print(choice)
    print(f"you have to spend {min} minutes for {kwargs[choice]}")

    
time_activity(10,20,10, sport="Kickboxing", hobby="Plants", fun="Driving", work="DevOps")