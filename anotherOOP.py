credentials = {}
print("Hii")
class Login_user:

    def signup(self, first_name, last_name, age, password):
        print("Wellcome to our Page")
        username = first_name + "_" + last_name
        credentials["username"] = username
        credentials["age"] = age
        credentials["passs"] = password
        print("thanku", username, "for login")

    def increment_login_attempt(self):
        attempt = 0
        fattement = attempt + 1
        return fattement

    def login(self, username1, password1):
            if username1 == credentials["username"] and password1 == credentials["passs"]:
                print("Wellcome Back ",username1)
            else:
                increment_login_attempt()

                print("Try Again")


login1 = Login_user()

while True:
    user = input("Login/Sign_up: ")
    if user == "login":
        first_name  = input("Enter The first name: ")
        last_name = input("Enter the last name: ")
        password = input("Enter your password: ")
        login1.login(username1 = first_name + last_name, password1 = password)

    elif user == "sign_up":
        first_name  = input("Enter The first name: ")
        last_name = input("Enter the last name: ")
        age = int(input("Enter your age: "))
        password = input("Enter your password: ")
        login1.signup(first_name, last_name, age, password)

    elif user == "q":
        break
