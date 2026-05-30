# 🐍 Day 03 - Using VS Code & Understanding User Input

Welcome back! 🎉

Today we learned:

* How to create a Python file in VS Code
* How to take input from the user
* What the `input()` function does
* Why `input()` always gives us text (string)
* Why we need `int()` for calculations
* How to check data types using `type()`

---

# 💻 Creating a New Python File in VS Code

VS Code is a tool that programmers use to write code.

Let's learn how to create a new Python file.

---

## Step 1: Open VS Code

Click on:

* VS Code Desktop Icon

OR

* Windows Search → Type "VS Code"

---

## Step 2: Open Your Python Folder

Click:

```
File → Open Folder
```

Choose the folder where you want to save your Python programs.

Example:

```
Desktop/Python
```

---

## Step 3: Create a New File

Click:

```
File → New File
```

OR

Click the ➕ (New File) button.

---

## Step 4: Save the File

Save the file as:

```python
demo.py
```

👉 `.py` tells the computer that this is a Python file.

---

## Step 5: Write Code

Now you can start writing Python programs inside the file.

---

# ⌨️ Understanding the input() Function

Sometimes we want the user to tell the program something.

For example:

* Their name
* Their age
* Their favorite animal
* A number

To do this, we use:

```python
input()
```

---

## Example

```python
name = input("Enter your name: ")

print("Hello " + name)
```

---

## What Happens Here?

Step 1:

Python shows:

```text
Enter your name:
```

Step 2:

The user types:

```text
Rahul
```

Step 3:

Python stores the answer inside the variable:

```python
name
```

Step 4:

Python prints:

```text
Hello Rahul
```

---

# 🧠 Important Concept

Whatever the user enters using:

```python
input()
```

Python automatically converts it into a string.

A string means:

👉 Text

Even if the user enters:

```text
5
```

Python treats it as:

```python
"5"
```

Notice the quotes.

That means Python sees it as text, not a number.

---

# 🔍 Let's Check Using type()

We can ask Python:

"What type of data is this?"

Using:

```python
type()
```

Example:

```python
a = input("Enter a number: ")

print(type(a))
```

If the user enters:

```text
5
```

Output:

```python
<class 'str'>
```

👉 `str` means string (text)

---

# 🤔 What Happens If We Don't Convert?

Let's try this program:

```python
a = input("Enter a number: ")

print(a * 2)
```

Suppose the user enters:

```text
5
```

Many students expect:

```text
10
```

But Python prints:

```text
55
```

Why?

Because Python thinks:

```python
a = "5"
```

This is text.

Python repeats the text two times:

```text
55
```

Just like:

```python
print("cat" * 2)
```

Output:

```text
catcat
```

Python is repeating text.

It is NOT doing math.

---

# 🔢 Converting Text into a Number

To do calculations, we must convert the text into a number.

We use:

```python
int()
```

The word `int` means:

👉 Integer (whole number)

---

## Example

```python
a = input("Please enter a number: ")

b = int(a)

print(type(b))
```

If user enters:

```text
5
```

Output:

```python
<class 'int'>
```

Now Python knows that 5 is a number.

---

# 🎯 Final Program

```python
a = input("Please enter a number: ")

b = int(a) * 2

print(type(b))
print("The answer is :", b)
```

---

## Example Run

Input:

```text
5
```

Output:

```text
<class 'int'>
The answer is : 10
```

🎉 Now Python performs real mathematical calculations!

---

# 🏁 What We Learned Today

✅ How to create a Python file in VS Code

✅ How to use `input()`

✅ How Python stores user input

✅ What a string (`str`) is

✅ How to use `type()`

✅ Why calculations may not work with strings

✅ How to convert text into numbers using `int()`

---

# 🚀 Homework

Create a file called:

```python
adding_number.py
```

Write a program that:

1. Asks the user for a number
2. Add 100 to the number
3. Prints the answer

Example:

Input:

```text
7
```

Output:

```text
The answer is : 107
```
---

### *__Great job today! 🎉🐍__*
