num = int(input("Number: ")) # 5
favt = 1

if num < 0:
    print("Number below 0")

elif num == 0:
    print("Number = 0")

else:
    for i in range(1, num +2): # ((1,5) it also includes num which is 5
        favt = favt * i
        # it basically does is form fav (1) * i (1) = 1
        # it basically does is form fav (2) * i (1) = 2
        # it basically does is form fav (2) * i (3) = 6
        # it basically does is form fav (6) * i (4) = 24
        # it basically does is form fav (24) * i (5) = 1
print(favt)