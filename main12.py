data = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

name = input("Введите имя")
x = len(data)
i = 0
while i < x:
    if name in data[i]:
        print(name + ' is ' + str(data[i][1]))
        break
    i += 1
if i == len(data):
    print('Not found')
