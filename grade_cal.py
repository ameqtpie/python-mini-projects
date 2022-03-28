def computeGrade(grade):
    if score < 0 or score > 1.0 :
        return "Out of range"
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"

scr = input('Enter grade (1.0 - 0.1): ')
try:
    score = float(scr)
except:
    print('Invalid input')
    quit()

print(computeGrade(score))
