# ========================================== Detect Vowels in a Sentence =========================================================

Vowels = ("a", "e", "i", "0", "u")

user_message = input("Please Enter Your Message: ")

filltered_message = ""

for i in user_message:
    if i not in Vowels:
        filltered_message = filltered_message + i

print(filltered_message)



# =========================================== Detact Space Between Two Words ======================================================

space = " "
user_message = input("Please Enter Your Message: ")

if space in user_message:
    print("There is a space")
else:
     print("There is no space")




# ============================================= Delete Message between words ========================================================
user_message = input("Please Enter Your Message: ")

final_result = user_message.replace(" ", "")
print(final_result)



# ============================================= Delete the ending Space of the sentence ==============================================
user_message = input("Please Enter Your Message: ")

final_result = user_message.strip()
print(final_result)