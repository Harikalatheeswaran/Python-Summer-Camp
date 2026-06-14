# 🐍 Day 05 - Solving Problems with Python

Welcome back! 🎉

Today we learned:

* What comments are
* How programmers solve problems step by step
* How to break a big problem into smaller problems
* How to compare values using `==`
* How to check if values are different using `!=`
* How to use `if` statements to make decisions
* How to see the result of a condition using `print()`

---

# 🧠 How Programmers Think

When programmers are given a problem, they do not start writing code immediately.

Instead, they ask:

👉 "How can I break this big problem into smaller pieces?"

Solving many small problems is easier than solving one big problem.

---

# 🎯 Today's Problem

We wanted to create a secret party.

Only people who know the password can enter.

If they know the password:

```text
You can enter 😄
```

If they do not know the password:

```text
You cannot enter 😡
```

---

# ✏️ Step 1 - Write the Plan

Before writing code, we wrote comments.

Comments help us plan our program.

---

# 📝 What Are Comments?

Comments are notes for humans.

Python ignores comments.

Comments start with:

```python
#
```

Example:

```python
# This is a comment

print("Hello")
```

Python runs:

```python
print("Hello")
```

But ignores:

```python
# This is a comment
```

---

# 🤔 Why Use Comments?

Comments help us:

* Remember our ideas
* Explain code
* Plan programs
* Make code easier to understand

---

# Our Plan

Before writing code, we wrote:

```python
# we need to create a program which takes in a password entered by the user

# we check if that password is correct or not

# if the password is correct : we show them a message - you can enter

# if the password is wrong : we show them a message - you cannot enter
```

Notice something?

We solved the problem on paper first.

Only then did we write code.

This is exactly how real programmers work.

---

# 🧩 Breaking the Problem into Small Pieces

Let's divide our problem.

---

## Small Problem 1

What is the correct password?

Answer:

```python
password = "superman"
```

We stored the password inside a variable.

---

## Small Problem 2

Show a welcome message.

```python
print("Welcome to Eashan & Charvi's secret party 🥳")
```

Output:

```text
Welcome to Eashan & Charvi's secret party 🥳
```

---

## Small Problem 3

Ask the user for a password.

```python
password_entered_by_user = input("Enter the secret password : ")
```

Example:

User enters:

```text
superman
```

Python stores it inside:

```python
password_entered_by_user
```

---

## Small Problem 4

Check if the passwords are the same.

```python
password == password_entered_by_user
```

Python asks:

```text
Are these two values equal?
```

---

# 🔍 Understanding ==

The symbol:

```python
==
```

means:

👉 Is it equal to?

Example:

```python
print(10 == 10)
```

Output:

```text
True
```

Because both values are equal.

---

Example:

```python
print(10 == 5)
```

Output:

```text
False
```

Because the values are different.

---

# 🎯 Why Did We Print the Comparison?

We wrote:

```python
print(password == password_entered_by_user)
```

Why?

Because we wanted to SEE what Python was thinking.

---

Example

Correct password entered:

```text
superman
```

Output:

```text
True
```

---

Wrong password entered:

```text
batman
```

Output:

```text
False
```

This helped us understand how conditions work.

---

# 🧠 Understanding True and False

A condition can only have two answers.

```text
True
```

OR

```text
False
```

Think of it like:

```text
Yes
```

OR

```text
No
```

---

# 🚪 Letting the User Enter

Now we use an if statement.

```python
if password == password_entered_by_user:
    print("You can enter 😄")
```

If the password is correct:

Output:

```text
You can enter 😄
```

---

# 🚫 Blocking the User

Now we check if the password is different.

```python
if password != password_entered_by_user:
    print("You cannot enter 😡")
```

---

# 🔍 Understanding !=

The symbol:

```python
!=
```

means:

👉 Not Equal To

Python asks:

```text
Are these values different?
```

---

Example:

```python
print(10 != 5)
```

Output:

```text
True
```

Because 10 and 5 are different.

---

Example:

```python
print(10 != 10)
```

Output:

```text
False
```

Because they are the same.

---

# 🧩 The Complete Program

```python
# we need to create a program which takes in a password entered by the user

# we check if that password is correct or not

# if the password is correct : we show them a message - you can enter

# if the password is wrong : we show them a message - you cannot enter

password = "superman"

print("Welcome to Eashan & Charvi's secret party 🥳")

password_entered_by_user = input("Enter the secret password : ")

print(password == password_entered_by_user)

if password == password_entered_by_user:
    print("You can enter 😄")

if password != password_entered_by_user:
    print("You cannot enter 😡")
```

---

# 🏁 What We Learned Today

✅ Comments using `#`

✅ Planning before coding

✅ Breaking problems into smaller parts

✅ Using variables

✅ Taking user input

✅ Comparing values using `==`

✅ Checking if values are different using `!=`

✅ Understanding `True` and `False`

✅ Using `if` statements

✅ Understanding how programmers solve real problems

---

# 🚀 Homework

Create a program called:

```python
secret_club.py
```

Use:

```python
password = "python"
```

Ask the user for a password.

If the password is correct:

```text
Welcome to the Secret Club! 🎉
```

If the password is wrong:

```text
Access Denied! 🚫
```

---

## Great job today! 🎉

Today you learned one of the most important skills in programming:

👉 Breaking a big problem into small pieces and solving them one step at a time.
