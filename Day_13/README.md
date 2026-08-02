# 🐍 Day 13 - f-Strings and Solving Algebra Problems Using Python

Welcome back! 🎉

Today we learned two exciting new concepts.

✅ Using **f-Strings** to print variables in a cleaner way.

✅ Using Python to solve simple Algebra problems.

Python is not only used to make games and apps.

It can also help us solve Mathematics problems!

---

# 📝 Today's Topics

* Revision of `input()`
* Revision of variables
* Introduction to **f-Strings**
* Solving simple Algebra equations
* Solving Algebra addition problems

---

# 🧠 Think Like a Programmer

Before writing any program, remember our three steps.

```text
Input

↓

Processing

↓

Output
```

---

# 🎯 Program 1 - Greeting the User

First, we wrote a small program.

```python
name = input("Enter the name : ")

print(f"Hello {name}")
```

---

# Step 1 - Taking Input

We ask the user for their name.

```python
name = input("Enter the name : ")
```

Example

User enters:

```text
Charvi
```

Python stores:

```python
name = "Charvi"
```

---

# Step 2 - Printing the Name

We wrote:

```python
print(f"Hello {name}")
```

Output:

```text
Hello Charvi
```

---

# 🤔 What is an f-String?

Earlier we printed like this:

```python
print("Hello " + name)
```

Today we learned a much cleaner way.

```python
print(f"Hello {name}")
```

The letter:

```python
f
```

stands for:

👉 **Formatted String**

The curly brackets:

```python
{name}
```

tell Python:

> "Put the value stored inside the variable here."

---

# 📊 Visualisation

```text
Variable

name

↓

Contains

"Charvi"

↓

Python replaces

{name}

↓

Output

Hello Charvi
```

---

# 🎯 Program 2 - Solving an Algebra Equation

Now we used Python to solve a Maths problem.

Suppose we have:

```text
ax + b = c
```

Our goal is to find the value of:

```text
x
```

---

# 🧠 Solving on Paper

Suppose

```text
3x + 5 = 20
```

Step 1

Move 5 to the other side.

```text
3x = 20 - 5
```

Step 2

```text
3x = 15
```

Step 3

Divide both sides by 3.

```text
x = 15 / 3
```

Answer

```text
x = 5
```

Python follows the exact same steps!

---

# 📝 The Program

```python
print("Give the equation of the form ax + b = c")

a = input("Enter the value for a : ")
b = input("Enter the value for b : ")
c = input("Enter the value for c : ")

a = int(a)
b = int(b)
c = int(c)

x = (c - b) / a

print("The answer for x is :", x)
```

---

# 🧩 Understanding the Program

## Input

The user enters:

```text
a
b
c
```

Example

```text
a = 3

b = 5

c = 20
```

---

## Processing

Python calculates:

```python
x = (c - b) / a
```

Substituting the values:

```text
(20 - 5) / 3

↓

15 / 3

↓

5
```

---

## Output

```text
The answer for x is : 5
```

---

# 📊 Program Flow

```text
Input

a

b

c

↓

Convert to integers

↓

Calculate

(c-b)/a

↓

Store answer in x

↓

Print x
```

---

# 🎯 Program 3 - Algebra Addition

We then solved a bigger problem.

Suppose we have:

```text
(Ax + By + Cz)

+

(Dx + Ey + Fz)

+

(Gx + Hy + Iz)
```

Our goal is to combine all the like terms.

---

# 🧠 Understanding Like Terms

Look carefully.

```text
3x + 2x
```

Both have:

```text
x
```

So we add:

```text
3 + 2 = 5
```

Answer:

```text
5x
```

---

Similarly,

```text
4y + 6y

↓

10y
```

and

```text
8z + 1z

↓

9z
```

---

# 📝 Our Program

```python
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

print(f"{x}x + {y}y + {z}z")
```

---

# 📊 Visualisation

```text
x terms

A + D + G

↓

Store in x

----------------

y terms

B + E + H

↓

Store in y

----------------

z terms

C + F + I

↓

Store in z

----------------

Print

x + y + z
```

---

# 🏁 What We Learned Today

✅ What an f-String is.

✅ How to print variables using f-Strings.

✅ How Python can solve Algebra equations.

✅ Breaking a Maths problem into small steps.

✅ Combining like terms in Algebra.

---

# 🚀 Homework

## Question 1

Write a program that asks the user for their favourite fruit.

Use an **f-String** to print:

```text
My favourite fruit is Mango!
```

(Replace "Mango" with the user's input.)

---

## Question 2

Solve the equation:

```text
2x + 8 = 18
```

using your Algebra program.

Did Python give the same answer as solving it on paper?

---

## 🌟 Challenge

Change the values of `A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`, and `I`.

Can you predict the final expression **before** running the program?

Then check your answer using Python!

---

# 🎉 Congratulations!

Today you discovered that Python is not just a programming language—it is also a powerful tool for solving mathematical problems.

By combining variables, user input, arithmetic, and f-Strings, you created programs that can solve equations and display answers in a neat and readable way.

Keep practicing, keep experimenting, and most importantly...

**Have fun coding! 🐍🚀**
