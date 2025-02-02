#arithmetic operators
from tabnanny import process_tokens
from time import process_time_ns

x = 2
y = 5

total = x + y
print(total)

total = x - y
print(total)

total = x*y
print(total)

total = y/x
print(total)

#modulus, liekana po dalybos
total = y%x
print(total)

#raise to the power of, kelti kvadratu
total= y**x
print(total)

#comparison operators

a = 30
b = 60

out = a < b
print(out)

out = a > b
print(out)

out = a == b
print(out)

out = a != b
print(out)

out = a >= b
print(out)

out = a <= b
print(out)


#assignment operators

c = 0
d = 1

c+=d # same as: c = c + d
print(c)

c = 0
d = 1
c -= d

print("value of c is", c)

#logical operators and or

a = 40
b = 60

x = 2
y = 3

out = (a<b) or (x>y)

print(out)

out = (a>b) or (x<y)
print(out)

out = (a<b) or (x<y)
print(out)

out = (a<b) and (x<y)
print(not(out))

#membership operators

devops=("linux", 1.5, "bash scripting", 12, "jenkins", "python")
ans = 1 in devops #adding not to make true to false
print("deez nutz ",ans)

# indentity operators

a= 12
b= 15

result = a is not b
print(result)