<div align="center">
  
# 🐍 Day 04 - Introduction to Conditional Statements <br> (if & if-else)
</div>

Welcome back! 🎉

Today we learned one of the most important concepts in programming:

👉 Making decisions!

Computers are very smart, but they only do exactly what we tell them to do.

Sometimes we want a program to do something only when a certain condition is true.

This is where **if statements** help us.

---

# 🤔 What is a Condition?

A condition is simply a question that has two possible answers:

✅ Yes (True)

❌ No (False)

Examples:

* Is 5 greater than 3? → Yes
* Is 10 smaller than 2? → No
* Is your age greater than 18? → Maybe!

Python uses conditions to make decisions.

---

# 🧠 Real Life Example

Imagine your mom tells you:

"If it is raining, take an umbrella."

You would think:

```text
Is it raining?
```

If YES ☔

Take umbrella.

If NO ☀️

Do not take umbrella.

Python works exactly the same way.

---

# 🔍 Comparison Operators in Python

When Python checks a condition, it compares two values.

To compare values, we use **comparison operators**.

Think of these operators as questions that Python asks.

The answer will always be:

✅ True

OR

❌ False

---

## Greater Than (>)

This means:

👉 "Is the value on the left bigger than the value on the right?"

Example:

```python
print(10 > 5)
```

Output:

```text
True
```

Because 10 is greater than 5.

---

## Less Than (<)

This means:

👉 "Is the value on the left smaller than the value on the right?"

Example:

```python
print(5 < 10)
```

Output:

```text
True
```

---

## Greater Than or Equal To (>=)

This means:

👉 "Is the value greater than OR equal to?"

Example 1:

```python
print(10 >= 5)
```

Output:

```text
True
```

Example 2:

```python
print(10 >= 10)
```

Output:

```text
True
```

Because 10 is equal to 10.

---

## Less Than or Equal To (<=)

This means:

👉 "Is the value smaller than OR equal to?"

Example:

```python
print(5 <= 10)
```

Output:

```text
True
```

Example:

```python
print(10 <= 10)
```

Output:

```text
True
```

---

## Equal To (==)

This means:

👉 "Are both values exactly the same?"

Example:

```python
print(5 == 5)
```

Output:

```text
True
```

Example:

```python
print("cat" == "cat")
```

Output:

```text
True
```

---

## Important!

Do NOT confuse:

```python
=
```

with

```python
==
```

---

### Single Equal (=)

Used to store a value.

Example:

```python
age = 10
```

This means:

👉 Put 10 inside the variable age.

---

### Double Equal (==)

Used to compare values.

Example:

```python
age == 10
```

This means:

👉 Is age equal to 10?

---

## Not Equal To (!=)

This means:

👉 "Are the values different?"

Example:

```python
print(5 != 10)
```

Output:

```text
True
```

Because 5 and 10 are different.

---

Example:

```python
print(5 != 5)
```

Output:

```text
False
```

Because both values are the same.

---

# 🎯 Quick Practice

Can you guess the answers before running the code?

```python
print(20 > 10)
print(5 < 2)
print(10 >= 10)
print(5 <= 4)
print("dog" == "dog")
print("cat" != "dog")
```

Answers:

```text
True
False
True
False
True
True
```

---

# 🧠 Easy Trick to Remember

| Symbol | Meaning                  |
| ------ | ------------------------ |
| >      | Greater than             |
| <      | Less than                |
| >=     | Greater than or equal to |
| <=     | Less than or equal to    |
| ==     | Equal to                 |
| !=     | Not equal to             |

These operators help Python make decisions using `if` statements.


---

# 🔹 Simple if Statement

Example:

```python
age = 12

if age > 10:
    print("You are older than 10")
```

Output:

```text
You are older than 10
```

---

## How Does This Work?

Step 1:

Python checks:

```python
age > 10
```

Step 2:

Since 12 is greater than 10

The answer is:

```text
True
```

Step 3:

Python runs the code inside the if statement.

---

# 🔹 Another Example

```python
marks = 95

if marks > 90:
    print("Excellent!")
```

Output:

```text
Excellent!
```

---

# 🔹 Multiple if Statements

Sometimes we want Python to check more than one condition.

Example:

```python
marks = 95

if marks > 90:
    print("Excellent!")

if marks > 50:
    print("Pass")
```

Output:

```text
Excellent!
Pass
```

---

## Why Did Both Print?

Because BOTH conditions are true.

Python checks each if statement separately.

---

# 🔹 Introduction to if-else

Sometimes we want Python to choose between two options.

Example:

```python
age = 8

if age >= 10:
    print("You can join the competition")
else:
    print("You are too young")
```

Output:

```text
You are too young
```

---

## How Does if-else Work?

Python asks:

```text
Is age greater than or equal to 10?
```

If YES:

Run the if block.

If NO:

Run the else block.

Only ONE block runs.

---

# 📏 Understanding Indentation

This is VERY important.

Python uses indentation (spaces) to know which lines belong together.

Example:

```python
if True:
    print("Hello")
```

Notice the space before:

```python
print("Hello")
```

This space is called:

👉 Indentation

---

# 🧠 Easy Way to Remember

Think of indentation like standing in a queue.

The indented code belongs to the if statement.

Example:

```python
if True:
    print("Line 1")
    print("Line 2")
    print("Line 3")
```

All three print statements belong to the if statement.

---

# ❌ Wrong Example

```python
if True:
print("Hello")
```

Python will show an error.

Because the print statement is not indented.

---

# 🎯 Fun Activity - Print Your Favorite Cartoon

Today we created a fun cartoon printer.

The user can choose:

* Tweety
* Sylvester
* Bugs Bunny

Python checks what the user typed.

Then it prints the correct cartoon.

---

## How It Works

Step 1:

Ask the user:

```python
cartoon = input("Type which cartoon you want to print: ")
```

Step 2:

Check the answer.

Example:

```python
if cartoon == "bugs":
    print(bugs)
```

Step 3:

If the user typed:

```text
bugs
```

Python prints Bugs Bunny.

---

# 🧠 Important Concept

Notice this:

```python
if cartoon == "bugs":
```

The double equal sign:

```python
==
```

means:

👉 "Is it equal to?"

Python is comparing values.

It is NOT assigning a value.

---

# Example

```python
animal = "cat"

if animal == "cat":
    print("Meow!")
```

Output:

```text
Meow!
```

---

# 🏁 What We Learned Today

✅ What a condition is

✅ Simple if statements

✅ Multiple if statements

✅ if-else statements

✅ Why indentation is important

✅ Using == to compare values

✅ Making programs take decisions

---

## Great job today! 🎉

You have now started learning how programmers make computers think and make decisions! 🧠🐍
