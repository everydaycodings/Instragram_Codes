from math import sqrt

num = int(input("Number: ")) # 20

for i in range(1, num + 1):
    print("i: ", i)

    for b in range(i, num+1):
        print("b: ",b)

        c_square = i**2 + b**2 # (6)^2 + (8)^2 = 100

        c = int(sqrt(c_square)) # under root 100 = 10

        if ((c_square - c**2)) == 0: # 100 - (10)^2 = 0
            print(i, b, c)

