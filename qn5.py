# Create a login system with the following users:
# Username: admin
# Password: admin123
# Role: Administrator
# Username: student12
# Password: study123

# Role: Student
# Ask the user for username and password.
# If the login is correct:
#  Display the user&#39;s role.
#  If the role is Administrator, display Full system access.
#  If the role is Teacher, display Teacher access.
# If the login is incorrect, display Invalid username or password.
# use nested loop
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