
# 🐍 Day 02 - Printing, Variables, Conditions & Functions

Welcome back! 🎉

Today we will learn:
- Different ways to print lines 🖨️
- Variables 📦
- If conditions 🤔
- Taking input from user ⌨️
- Functions 🧠

Take it slow. Try every example yourself 💡

---

# 🖨️ Printing in Python

We already used `print()` to show output.

👉 Think of `print()` like talking to the computer screen.

---

## 🔹 Method 1: Using multiple print statements

print("Hello")
print("How are you?")

👉 Each `print()` goes to a new line automatically.

---

## 🔹 Method 2: Using \n (New Line)

`\n` means **"go to next line"**.

print("Hello\nHow are you?")

👉 Output:
Hello
How are you?

---

## 🧠 When to use \n?

- When you want **one print statement**
- When you are building long text

---

## 🎯 Activity

Print this using ONE print statement:

I like Python
It is fun
I am learning coding

---

# 📦 Variables

A variable is like a **box that stores information**.

👉 We give the box a name so we can use it later.

---

## 🔹 Example

name = "Rahul"
age = 12

print(name)
print(age)

---

## 🧠 Understand clearly

- `name` → label of the box
- `"Rahul"` → value inside the box

👉 You can change the value anytime.

---

## 📏 Rules for naming variables

✅ Allowed:
- letters (a-z, A-Z)
- numbers (0-9)
- underscore (_)

❌ Not allowed:
- spaces → my name ❌
- starting with number → 1name ❌

---

## ✅ Good examples

name = "Arjun"
age = 13
my_pet = "Cat"

---

## ❌ Bad examples (will give error)

1name = "Arjun"
my name = "Arjun"

---

## 🎯 Activity

Create 3 variables:
- your name
- your favorite food
- your age

Print all of them.

---

# 🤔 If Conditions

Python can **make decisions** just like humans.

👉 Example:
If it is raining → take umbrella ☔

---

## 🔹 Basic if

age = 15

if age > 10:
    print("You are older than 10")

👉 If condition is TRUE → code runs
👉 If FALSE → nothing happens

---

## 🔹 if - else

age = 8

if age > 10:
    print("You are older than 10")
else:
    print("You are 10 or younger")

👉 Only ONE block will run

---

## 🔹 if - elif - else

marks = 75

if marks > 90:
    print("Excellent")
elif marks > 50:
    print("Good")
else:
    print("Try again")

👉 Python checks from top to bottom
👉 First TRUE condition runs

---

## 🎯 Activity

Write a program:

- If number > 0 → print "Positive"
- Else → print "Negative"

---

# ⌨️ Taking Input from User

Now we can **ask the user for input**.

---

## 🔹 Example

name = input("Enter your name: ")

print("Hello", name)

👉 User types something → Python stores it

---

## 🧠 Important Concept

input() always gives **text (string)**

Even if user types number, it is still text.

---

## 🔹 Example with number

age = int(input("Enter your age: "))

print(age + 1)

👉 `int()` converts text → number

---

## 🎯 Activity

Ask user:
- name
- favorite game

Print:
Hello <name>
You like <game>

---

# 🧠 Functions

Functions help us **reuse code**.

👉 Instead of writing same code again and again, we use functions.

---

## 🔹 Example

def say_hello():
    print("Hello!")

say_hello()

👉 We define once → use many times

---

## 🔹 Function with input

def greet(name):
    print("Hello", name)

greet("Arjun")

👉 "Arjun" is passed into function

---

## 🔹 Function with return

def add(a, b):
    return a + b

result = add(5, 3)
print(result)

👉 `return` sends value back

---

## 🎯 Activity

Create a function:

Name: introduce

It should print:
- your name
- your age

---

# 🏁 What You Learned Today

- Printing with \n
- Variables and rules
- If conditions
- Taking input
- Functions

---

# 🚀 Homework

1. Ask user name and age
2. If age > 18 → print "Adult"
3. Else → print "Kid"

4. Create a function that prints:

I am learning Python!

---

Great job today! 🎉
