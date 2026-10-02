print("Welcome to the login system.")
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username == "admin" and password == "admin123":
        print("Login successful.")
        print("Role: Administrator")
        print("Full system access.")
        break
    elif username == "student12" and password == "study123":
        print("Login successful.")
        print("Role: Student")
        print("Student access.")
        break
    else:
        print("Invalid username or password. Please try again.")