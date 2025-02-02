#Keywords arguments


def vac_feedback(vac, efficacy):
    print(f"{vac} vaccine in having {efficacy} % efficacy")
    if (efficacy > 50) and (efficacy <= 75):
        print("seems not effective, more trail needed")
    elif (efficacy > 75) and (efficacy < 90):
        print("kinda alright")
    elif (efficacy >= 90) and (efficacy <= 100):
        print("sure, get shot")
    else:
        print("gay")

vac_feedback("pfizer", 49)
vac_feedback("vjayjay", 88)
vac_feedback("milf", 99)
vac_feedback("johncena", 749)

#does not work if yoi change the positions, unless you use the names
#vac_feedback(11, "john")
vac_feedback(efficacy=85, vac="pfizer")



