def convert_1(miles):
    return miles * 1.6
def convert_2(kilometers):
    return kilometers * 0.6

try:
    f_miles = float(input('Enter km to convert into miles: '))
    f_kilometers = float(input('Enter miles to convert into km: '))
except:
    print('Invalid Input')

print('km to miles: ', convert_1(f_miles))
print('miles to km: ', convert_2(f_kilometers))
