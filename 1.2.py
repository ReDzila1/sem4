from random import randint

n = int(input("Количество кустов"))
m = 2
maximum = 0

if n < 3:
    print("Количество кустов должно быть больше 2")
else:
    list = [[i for i in range(1)] for j in range(n)]

    for i in range(len(list)):
        for j in range(len(list[i])):
            list[i][j] = randint(10,40)
            
    print(list)

    for i in range(1, len(list) - 1):
        for j in range(len(list[i])):
            if (list[i - 1][j] + list[i][j] + list[i + 1][j]) > maximum:
                maximum = list[i - 1][j] + list[i][j] + list[i + 1][j]

    print(maximum)