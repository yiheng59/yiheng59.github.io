import random
from pprint import *

shape = (18, 6)
m = shape[0]
n = shape[1]

num = []
index = 1

for i in range(n * m):
    num.append(index)
    index += 1

random.shuffle(num)

pos = []  # 上左下右

for index, number in enumerate(num):
    x, y = index % m, index // m
    a, b, c, d = (x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y)
    a, b, c, d = [num[i[0] + i[1] * m] if 0 <= i[0] < m and 0 <= i[1] < n else -2 for i in (a, b, c, d)]
    pos.append((a, b, c, d))

new_pos = pos.copy()
new_num = num.copy()
experienced_index = []
for _ in range(n * m):
    index = 0
    while index in experienced_index:
        index = random.randint(0, n * m - 1)

    experienced_index.append(index)
    x, y = index % m, index // m
    p = pos[index]
    tips_count = 0
    for a, j in enumerate(p):
        if j == -2:
            tips_count += 1
            continue
        if j == -1:
            continue
        b = (a + 2) % 4  # 上<->下 左<->右
        if pos[num.index(j)][b] != -1:
            tips_count += 1

    while (tips_count == 4 or (tips_count == 3 and random.random() > 0.3)
           or (tips_count == 2 and random.random() > 0.8)):
        l = z = 0
        while True:
            l = random.randint(0, 3)
            z = p[l]
            if z == -1 or z == -2:
                continue
            break

        q = list(pos[num.index(z)])
        q[(l + 2) % 4] = -1
        new_pos[num.index(z)] = tuple(q)
        tips_count -= 1
    if tips_count > 2 and random.random() > 0.5:
        new_num[index] = -1


index = 0


print("Sorted:")
for i in range(n * m):
    print([new_num[i], pos[i]], end=" ")
    if (i + 1) % m == 0:
        print()

print("\nKey:")
for i in range(n * m):
    print(num[i], end=" ")
    if (i + 1) % m == 0:
        print()

random.shuffle(new_num)
print("\nCards:")
for i in range(n * m):
    print([new_num[i], pos[i]])
