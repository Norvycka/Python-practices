#for loop
"""
commands = ["ls", "pwd", "cd", "whoami", "mkdir"]

for cc in commands:
    print("")
    print("I love this command: ", cc)
    for c in cc:
        print(c)
"""
import time

x=50
while True:
    print("value of x is: ", x)
    print("looping")
    x*=2
    time.sleep(1)