
numb = input("Vvedite chislo: ")
if int(numb) > 0:
    print("Polozhitelnoe chislo")
else:
    print("Otricatelnoe chislo")


age = int(input('age'))
if age >= 18:
    print('sovershennoletniy')
elif age <= 4:
    print("rebenok")
else:
    print("nesovershennoletniy")

a =  45
b = 6
if a % b == 0:
    print('delitsya')
else:
    print("ne delitsya")

god = 2000
etot_god = 2024
if god == etot_god:
    print("tekushiy god")
elif god < etot_god:
    print("god eshe ne nastupil")
else:
    print("god proshel")


