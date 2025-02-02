#defining functions

"""def add(arg1, arg2):
    total = arg1 + arg2
    return total

var1 = int(input("Irasyk pirma sk: "))
var2 = int(input("Irasyk antra sk: "))

out = add(var1,var2)
print(out)"""

"""def adder(arg1, arg2):
    total = arg1 + arg2
    print(total)

#adder(10,50)
print(adder(20,30))"""

"""def summ(arg):
    x = 0
    for i in arg:
        x = x + i
    return x

#out = summ([10,20,30])
#print(out)

print(summ([10,20,10,30]))"""

#you can declare the string in the MSG, and then overwrite it when call to the function greeting("Evening")
def greeting(MSG="Morning"):
    print(f"Good {MSG}")
    print("Welcome to the function")

greeting("Evening")
