import random

increption_dict = {"A":"1", "B":"2", "C":"T", "D":"W", "E":"D", "F":"G", "G":"0",
                       "H":"A", "I":"Q", "J":"P", "K":"5", "L":"O", "M":"7", "N":"8",
                       "O":"U", "P":"3", "Q":"M", "R":"B", "S":"6", "T":"", "U":"9",
                       "V":"C", "W":"X", "X":"4", "Y":"Z", "Z":"V", " ":" "}

increption_dict1 = {"A":"Q", "B":"W", "C":"E", "D":"R", "E":"T", "F":"Y", "G":"U",
                       "H":"I", "I":"O", "J":"P", "K":"L", "L":"K", "M":"J", "N":"H",
                       "O":"G", "P":"F", "Q":"D", "R":"S", "S":"A", "T":"Z", "U":"X",
                       "V":"C", "W":"V", "X":"B", "Y":"N", "Z":"M", " ": " "}
encreapted_message = ""

listt = [increption_dict, increption_dict1]

choice = random.choice(listt)

user = input("Please Enter Your Message: ").upper()

for i in user:
    if i in choice:
        encreapted_message += choice[i]
print("Your Encreapted Message: ", encreapted_message.lower())