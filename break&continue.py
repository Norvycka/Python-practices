# break statement
"""import time
for i in "Devops":
    print(i)
    time.sleep(1)
    if i == "o":
        print("found what i was looking for")
        break
print("out of loop")
"""
# continue statement
"""import time
for i in "Devops":
    print(i)
    time.sleep(1)
    if i == "o":
        print("found it")
        continue
    print(f"value of i: {i}")
print("out of loop")"""

"""import random

commands = ["ls", "pwd", "cd", "whoami", "mkdir"]
print(commands)
random.shuffle(commands)
print(commands)

LUCKY = random.choice(commands)
print(LUCKY)

for com in commands:
    print(f"testing command {com}")
    if com == LUCKY: #if this part is false, it is going down to test failed, and loops until it finds comm == LUCKY
        print("###############################")
        print(f"{LUCKY} command, test successful")
        print()
        break
    print("test failed")"""

import random

commands = ["ls", "pwd", "cd", "whoami", "mkdir"]
print(commands)
random.shuffle(commands)
print(commands)

LUCKY = random.choice(commands)
print(LUCKY)

for com in commands:
    print(f"testing command {com}")
    if com == LUCKY: #if this part is false, it is going down to test failed, and loops until it finds comm == LUCKY
        print("###############################")
        print(f"{LUCKY} command, test successful")
        print()
        continue
    print("test failed")
