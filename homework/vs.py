"""
my_list = ['a', 2, 3, 2, 'b', 'a']
my_set = set(my_list)
my_set.add(True)
print(all(my_set))


numbers = []
for i in range(5):
    user_input = int(input("Vvedi: "))
    numbers.append(user_input)
    
print(min(numbers))


user = ()
user_input = str(input("Vvedi func: "))
if user_input == 'print':
    print('func print')
elif user_input == 'len':
    print('func len')
elif user_input == 'input':
    print('func input')
else:
    print('net takoy func')    

user_input = float(input('Vvedi summu: '))
if user_input >= 50000:
    print(round((user_input * (3.47 / 100)), 2))
else:
    print('Summa mala')

a = '5' + 10
print(a)
my_list = [1, 4, 6,]
print(my_list[10])
print(b)

try:
    user_input = float(input('Vvedi summu: '))
    if user_input >= 50000:
        print(round((user_input * (3.47 / 100)), 2))
except:
    print('veli str, a ne int')

try:
    user_input = str(input('Vvedi name: '))
    print(Hello, user_input)
except:
    print('vveli int, a ne str')

dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}

try:
    for key in dict_.keys():
        print(key + ' opa')
except:
    print('est int v str')
"""