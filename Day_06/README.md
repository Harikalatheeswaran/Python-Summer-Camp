 # <div align="center"> *__🐍 Day 06 - Understanding How if Statements Work__* </div>

Welcome back! 🎉

Today we continued learning about one of the most important concepts in programming:

👉 **if statements**

We learned how Python decides which code to run and which code to skip.

---

# 📝 Quick Recap

Today we revised:

* Comments (`#`)
* Variables
* `input()`
* `int()`
* `type()`
* Boolean values (`True` and `False`)
* Indentation
* if statements

---

# 💬 Comments

Comments are notes written for humans.

Python ignores comments.

Comments begin with:

```python
# This is a comment
```

Example:

```python
# Ask the user for a number
number = input("Enter a number: ")
```

Comments help us understand our code later.

---

# 🧠 Boolean Values

A condition can only have two answers:

```python
True
```

or

```python
False
```

Examples:

```python
print(10 > 5)
```

Output:

```text
True
```

---

Example:

```python
print(5 > 10)
```

Output:

```text
False
```

---

# 🔢 Taking Input From User

We learned that:

```python
input()
```

always gives us text (string).

Example:

```python
a = input("Enter a number: ")
```

Even if the user enters:

```text
100
```

Python stores:

```python
"100"
```

which is text.

---

# 🔄 Converting Text Into Number

To perform calculations, we convert the text into a number.

Example:

```python
a = input("Enter a number: ")
b = int(a)
```

Now `b` contains a real number.

---

# 📏 Understanding Indentation

Look carefully:

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

Python uses indentation to know which lines belong together.

---

# 🧠 Helpful Tip

Think of indentation as putting code inside a box.

Everything indented belongs to the if statement.

Example:

```python
if True:
    print("Apple")
    print("Banana")
    print("Orange")
```

All three lines belong to the if statement.

---

# 🔹 Understanding Colon (:)

Look carefully:

```python
if c > 56:
```

The colon (`:`) tells Python:

👉 "The condition ends here."

After pressing Enter, VS Code automatically creates indentation.

This helps us write code correctly.

---

# 🎯 Program We Created Today

```python
b = input("enter the number : ")

c = int(b)

if c > 56:
    print(c, "is greater than 56")
    print("green")
    print("purple")
    print("blue")

if c < 56:
    print(c, "is less than 56")
    print("chicken biriyani")
    print("gobi")
    print("chicken 65")

print("Eashan & Charvi are learning python")
print("they are very smart!")
```

---

# 🧩 Let's Understand Step by Step

---

## Step 1

Ask the user for a number.

```python
b = input("enter the number : ")
```

Example:

User enters:

```text
80
```

---

## Step 2

Convert text into integer.

```python
c = int(b)
```

Now:

```python
c = 80
```

---

## Step 3

Check the first condition.

```python
if c > 56:
```

Python asks:

```text
Is 80 greater than 56?
```

Answer:

```text
Yes
```

So Python runs:

```python
print("green")
print("purple")
print("blue")
```

---

## Step 4

Check the second condition.

```python
if c < 56:
```

Python asks:

```text
Is 80 less than 56?
```

Answer:

```text
No
```

So Python skips everything inside this if statement.

---

# 🎯 What Happens If User Enters 30?

Python asks:

```text
Is 30 greater than 56?
```

Answer:

```text
No
```

Skip.

Then Python asks:

```text
Is 30 less than 56?
```

Answer:

```text
Yes
```

Run:

```python
print("chicken biriyani")
print("gobi")
print("chicken 65")
```

---

# 🤔 What Happens If User Enters 56?

This was the most important question today.

Python asks:

```text
Is 56 greater than 56?
```

Answer:

```text
False
```

Because 56 is equal to 56.

It is NOT greater.

---

Python asks:

```text
Is 56 less than 56?
```

Answer:

```text
False
```

Because 56 is equal to 56.

It is NOT less.

---

Therefore:

Neither if statement runs.

Only these lines run:

```python
print("Eashan & Charvi are learning python")
print("they are very smart!")
```

🎉 The students correctly predicted this!

---

# 🏁 What We Learned Today

✅ Comments

✅ Boolean values (`True` and `False`)

✅ Input and integer conversion

✅ Indentation

✅ Colon (`:`)

✅ How Python checks conditions

✅ How Python decides which code to run

✅ How Python skips code when a condition is False

---

# 🚀 Homework

Modify today's program.

Add another condition in such a way that if the user inputs `56` you should print the following
```python
print("There are 8 planets in the solar system")
print("Pluto is not a planer because : ")
print("Pluto's orbit is ir-regular & messy")
```

Make it print something fun.

Example:

```python
print("Exactly 56! 🎉")
print("There are 8 planets in the solar system")
print("Pluto is not a planer because : ")
print("Pluto's orbit is ir-regular & messy")
```

Try running the program with:

```text
30
56
80
```

Observe what gets printed each time.

---

## Great job today! 🎉

Today you learned an important programming skill:

👉 Predicting what a program will do before running it.
