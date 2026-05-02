# 🐍 Day 02 - Built-in Functions, Variables, Input & Terminal Basics

Welcome back! 🎉

Today we learned some very important basics that real programmers use every day.

---

## 🧠 1. Built-in Functions (type, help, exit)

Python gives us some **ready-made functions**. We can use them directly.

### 🔹 `type()`

This tells us **what kind of data** something is.

```python
print(type("Hello"))
print(type(10))
```

👉 Output will show things like `str` (text) and `int` (number)

---

### 🔹 `help()`

This shows **information about Python commands**.

```python
help(print)
```

👉 Think of it like asking Python:
👉 "Explain this to me"

---

### 🔹 `exit()`

This stops Python.

```python
exit()
```

👉 Imagine this like:
Tom holding a hammer 🔨
When you call `exit()`, Python goes to sleep 😴

---

## 💻 Where did we run these?

We used the **Command Prompt (CMD)** and typed `python` to enter Python mode.

---

## 📦 2. Variables

A variable is like a **box 📦 that stores data**.

We give the box a name, and we can use it later.

---

### 🔹 Example

```python
name = "Arjun"
age = 12

print(name)
print(age)
```

👉 `name` stores text
👉 `age` stores number

---

## 🧠 Easy Understanding

- Variable name = label on the box
- Value = what is inside the box

---

## 📏 Rules for Naming Variables

✅ Allowed:
- letters (a-z, A-Z)
- numbers (0-9)
- underscore (_)

❌ Not allowed:
- spaces → `my name`
- starting with number → `1name`

---

### ✅ Good Examples

```python
my_name = "Rahul"
age = 13
pet_name = "Dog"
```

---

### ❌ Bad Examples

```python
1name = "Rahul"
my name = "Rahul"
```

---

## 🎯 Activity

Create variables:
- your name
- your favorite color
- your age

Print them.

---

## ⌨️ 3. Taking Input from User

We can ask the user to type something.

---

### 🔹 Example

```python
name = input("Enter your name: ")
print("Hello " + name)
```

👉 Python waits for user input
👉 Stores it in `name`
👉 Then prints greeting

---

## 📁 Program: greetings.py

We created a file called `greetings.py`

```python
name = input("Enter your name: ")
print("Hello " + name)
```

---

## 🧠 Important Note

`input()` always gives **text (string)**

---

## 💻 4. Terminal Command - Clear Screen

Sometimes the screen gets messy.

We can clear it using:

```
cls
```

👉 This works in **Command Prompt (CMD)**
👉 It clears everything on the screen

---

## 🏁 What You Learned Today

- Built-in functions: `type()`, `help()`, `exit()`
- Variables and how they store data
- Rules for naming variables
- Taking input using `input()`
- Writing a small program (greetings.py)
- Clearing screen using `cls`

---

## 🚀 Homework

1. Create a file:

```
calculator.py
```

2. Ask user:
- number 1
- number 2

3. Print:
    - the sum of numbers : use `+` to add two numbers
    - the difference of numbers : use `-` to subtract two numbers
    - the product of numbers : use `*` to multiply two numbers
    - the division of numbers : use `/` to divide two numbers


---

Great job today! 🎉 Keep practicing!
