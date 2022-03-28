def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    print('BMI: ', bmi)
    if bmi < 16:
        return 'Severe Underweight'
    elif bmi >= 16 and bmi < 18.5:
        return 'Underweight'
    elif bmi >= 18.5 and bmi < 25:
        return 'Healthy'
    elif bmi >= 25 and bmi < 30:
        return 'Overweight'
    elif bmi >= 30:
        return 'Obese'

weight = input('Enter your weight(kg): ')
height = input('Enter your height(m): ')

try:
    f_weight = float(weight)
    f_height = float(height)
except:
    print('Invalid input')
    quit()

print(bmi_calculator(f_weight, f_height))
