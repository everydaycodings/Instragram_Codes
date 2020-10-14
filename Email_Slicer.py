email = input("Please enter your email: ").strip()

username = email[:email.index("@")]
domain = email[email.index("@")+1:]

print("Your Username is {} and email domain is {}".format(username, domain))
