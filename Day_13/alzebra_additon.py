# this is the program to solve alzebra addition problems
# this program soves for prolems of the type : 
# Ax + By + Cz + Dx + Ey + Fz + Gx + Hy + Iz
# eg : 3x+8y+7z+6y+4z-2x+3y-4x+6z

print("THis program sloves the equations of the form : ")
print("(Ax + By + Cz) + (Dx + Ey + Fz) + (Gx + Hy + Iz)")
print()

A = int(input("Enter value of A : "))
B = int(input("Enter value of B : "))
C = int(input("Enter value of C : "))
D = int(input("Enter value of D : "))
E = int(input("Enter value of E : "))
F = int(input("Enter value of F : "))
G = int(input("Enter value of G : "))
H = int(input("Enter value of H : "))
I = int(input("Enter value of I : "))

x = A + D + G
y = B + E + H
z = C + F + I

print("The answer is :")
print(f"{x}x + {y}y + {z}z")