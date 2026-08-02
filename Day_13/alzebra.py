# Solving Alzebra equations using Python

print("Give the equation of the form ax + b = c")

a = input("enter the value for a : ")
b = input("enter the value for b : ")
c = input("enter the value for c : ")

# converting the input to string
a = int(a)
b = int(b)
c = int(c)

x = (c-b)/a

print("The answre for x is : ", x)