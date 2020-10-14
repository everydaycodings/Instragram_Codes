import random
i = 0

while True:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    if a == 3 and b == 3 and c == 3:
        i += 1
        print(a, b, c, "in", i, "Times")
        break
    else:
        i += 1
        print(a, b, c)
        continue
