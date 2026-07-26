# Ask the user if they want to print even numbers or odd numbers from 1-50
# If the user selects even - print even numbers from 1-50
# If the usser selects odd - print odd numbers from 1-50

# ---------------------------------------------------------------------------------------------------------------

# Solution : 

# Input : ask the user for even or odd between 1 to 50
# process : code
# Output : even or odd numbers between 1 to 50

choice = input("You want to print even or odd numbers between 1 to 50: ")

if choice == "even":
    # to print even numbers : 
    print("even numbers from 1-50")
    for i in range(2, 51, 2):
        print(i)

# elif
elif choice == "odd":
    # to print odd numbers : 
    print("odd numbers from 1-50")
    for i in range(1, 50, 2):
        print(i) 

else:
    print("Invalid Choice.")
    

print("charvi & eashan are learning loops")

# ------------------------------------------------------------------------------------------------------------------
