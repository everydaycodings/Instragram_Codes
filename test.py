x = int(input("How many candies you want:"))

ac = 1000
i = 1

while i <= x:  
    if x > ac:
        continue
        print("no")
    print("candies", i)
    i+=1