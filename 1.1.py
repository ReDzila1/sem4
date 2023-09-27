from random import randint


n = int(input("Количество элементов в первом множестве"))
n2 = int(input("Количество элементов во втором множестве"))

a = []
b = []

for i in range(n):
    a.append(randint(1, 10))

for i in range(n2):
    b.append(randint(1, 10))

print(a, "|", b)

c = set(a).intersection(set(b))
print(sorted(c))
#n_set = set(randint(1, 20) for i in range(int(input("Введите кол-во элементов первого множества: "))))
#print(n_set)
#m_set = set(randint(1, 20) for i in range(int(input("Введите кол-во элементов второго множества: "))))
#print(m_set)
#s_set = sorted(n_set.intersection(m_set))
#print(*s_set)