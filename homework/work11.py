pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
index_loop = pythonList.index("loop")
pythonList.pop(index_loop)
print(pythonList)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
null = a[0] * a[1] * a[2] * a[3] * a[4] * a[5] * a[6] * a[7] * a[8] * a[9] * a[10]
print(null)

a = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
numbers = []
b = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
letters = []
for i in a:
    if str(i).isdigit():
        numbers.append(int(i))
print(numbers)
for y in b:
    if str(y).isalpha():
        letters.append(y)
print(letters)

b = (1, 2, 3)
print(b [1:4])
