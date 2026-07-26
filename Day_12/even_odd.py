# Ask the user if they want to print even numbers or odd numbers from 1-12
# If the user selects even - print even numbers from 1-12
# If the usser selects odd - print odd numbers from 1-12

# ---------------------------------------------------------------------------------------------------------------

# Solution : 

# Input : ask the user for even or odd between 1 to 12
# process : code
# Output : even or odd numbers between 1 to 12

choice = input("You want to print even or odd numbers between 1 to 12: ")

if choice == "even":
    print(2)
    print(4)
    print(6)
    print(8)
    print(10)
    print(12)

# elif
elif choice == "odd":
    print(1)
    print(3)
    print(5)
    print(7)
    print(9)
    print(11)

else:
    print("Invalid Choice.")
    

print("charvi & eashan are learning loops")

# ------------------------------------------------------------------------------------------------------------------

# same program done using for