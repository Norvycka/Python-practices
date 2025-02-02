#string built in methods/functions
from calendar import month

"""message = "you are a wizard harry"

#using the function once (not permanently attaching)
print(message.capitalize())

#to store that function with the value
Message = message.capitalize()
print(Message)"""

#dir() function

"""print(dir([]))
print(dir({}))
print(dir(()))
print(dir(""))"""

"""print(message.upper())
print(message.islower())
print(message.isupper())"""

#the output number means what is the index of the first character of the word
"""print(message.find("wizard"))
print(message[10:16])"""

"""seq1 = ("192","168","40","90")
print(seq1)
print(".".join(seq1))
print("/".join(seq1))
print("_".join(seq1))"""

"""mountains = ["everest", "himalaya", "bigdaddy", "longboi","alps"]

print(mountains)
mountains.append("OregonDeezNutz")
print(mountains)
mountains.extend(["BIGPP"])
print(mountains)
mountains.insert(5,"MT STEPBRO")
print(mountains)
#to delete an entry, if you dont add the number, the last entry will be popped
mountains.pop(3)
print(mountains)"""

cntr_emp = {"Name":"Sandra", "Skill":"Blockchain", "Code":1000}
print(cntr_emp.keys())
print(cntr_emp.values())
print(cntr_emp.clear())

text = "pYtHoN iS fUn"
print(text.capitalize())  # Output: "Python is fun"

