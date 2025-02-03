#variable length arguments *args (non keyword arguments)
def order_food(min_order, *args):
    print(f"you have ordered {min_order}")
    #print(args)
    for item in args:
        print(f"you have ordered: {item}")
    print("your food will be delivered in 30mins")
    print("enjoy da food, BOSS!")

order_food("delicious agurk", "bananana","orange")

