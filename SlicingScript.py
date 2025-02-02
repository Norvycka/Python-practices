plant1="PEAS ASS pot"
print(plant1)

print(plant1[0])
print(plant1[1])

print(plant1[-1])

#SLICING
#from 0 to 3
print(plant1[0:3])

#print to 9th symbol, counting from 0
print(plant1[:9])
#print from 9th symbol uintil the end
print(plant1[9:])

#tuple slicing #balls deep uwu
devops=("linux", "vagrant", "bash scripting", "AWS", "jenkins", "python")
print(devops[4])
print(devops[0])
print(devops[-1])

print(devops[2:5])

"""slicing =, taking 2 to 5 th word, counting from 0, so it would be 1 to 4,
and then taking that first tuple value of that new list you made by slicing
"""
print(devops[2:5][0])

"""slicing =, taking 2 to 5 th word, counting from 0, so it would be 1 to 4,
and then taking that first tuple value of that new list you made by slicing
then slicing even deeper and taking the fifth symbol of the first value from 2 to 5th word,
dont forget it is counting from 0, so 5th value would be 4th :))
"""
print(devops[2:5][0][5])


print(devops[2:5][0][5:11])
print(devops[2:5][0][5:11][-1])

print()

#dictionary
Skills = {"devops": ("linux", "vagrant", "bash scripting", "AWS", "jenkins"), "programming":["python", "javascript", "C", "c++"]}

print(Skills["devops"], "hellyeah")

print(Skills["programming"][1][:7])





