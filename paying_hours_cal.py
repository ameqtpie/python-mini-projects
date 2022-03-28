def computepay(hours, rate):
    if hours > 40 :
    # print('overtime')
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else :
        # print('regular')
        pay = hours * rate
    return pay

sh = float(input('Enter hours:'))
sr = float(input('Enter rate:'))

xp = computepay(sh, sr)

print('Pay:', xp)
