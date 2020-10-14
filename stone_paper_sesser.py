import random

c_choicelist = ["Stone", "Paper", "Sessers"]

u_points = 0
c_points = 0
print("Choose:\n1: Stone\n2: Paper\n3: Sessers")

while True:
    c_choice = random.choice(["stone", "paper", "sessers"])
    user = input("What Do You Want To Choose: ")

    if user == "q":
        break
        
    elif user == "stone" and c_choice == "stone":
        print("You Got A tie")
    elif user == "stone" and c_choice == "paper":
        print("You Loose!, Computer Choose",c_choice)
        c_points += 1
    elif user == "stone" and c_choice == "sessers":
        print("You Won!, Computer Choose",c_choice)
        u_points += 1

    elif user == "paper" and c_choice == "stone":
        print("You Won!, Computer Choose",c_choice)
        u_points += 1
    elif user == "paper" and c_choice == "paper":
        print("You Got A tie")

    elif user == "paper" and c_choice == "sessers":
        print("You Loose!, Computer Choose",c_choice)
        c_points += 1
    
    elif user == "sessers" and c_choice == "stone":
        print("You Loose!, Computer Choose",c_choice)
        c_points += 1
        
    elif user == "sessers" and c_choice == "paper":
        print("You Won!, Computer Choose",c_choice)
        u_points += 1

    elif user == "sessers" and c_choice == "sessers":
        print("You Got A tie")


print()
print("Your Point: {}\nComputer Point: {}".format(u_points, c_points))      

if u_points > c_points:         
    print("You Won The Match.")
elif u_points < c_points:
    print("You Lose The Match.")
elif u_points == c_points:
    print("You Got A Tie!")

print()
print("Thanku For Playing This Game.")
