
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

print(squared)

for i in range(1, 5):
    print(i, i, sep='=>', end='\n')
