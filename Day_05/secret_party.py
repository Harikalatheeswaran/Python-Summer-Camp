# we need to create a program which takes in a password enterd by the user ✅
# we check if that password is correct or not ✅
# if the password is correct : we show them a message - you can enter
# if the pass word is wrong : we show them a message - you cannot enter. 

password = "superman"

print("Welcome to Eashan & Charvi's secret party 🥳")
password_entered_by_user = input("Enter the secret password : ")

print(password == password_entered_by_user)

if password == password_entered_by_user:
    print("You can enter 😄")

if password != password_entered_by_user:
    print("You cannot enter 😡")
