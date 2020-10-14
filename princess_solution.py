import random

prince_name = random.choice(["John", "Hendry", "Gali_Ka_Launda"])
discarted_list = []
selected_list = []
i = 0

while i != 99 :
    i = i + 1
    point = random.randint(0, 100)

    if point <= 50:
        discarted_list.append(point)
        continue

    elif point == 100:
        selected_list.append(point)
        break

    elif point > 50:
        selected_list.append(point)       
        continue

selected_prince = max(selected_list)

print("Your Prince Name is {} And He Got {} Points".format(prince_name, selected_prince))