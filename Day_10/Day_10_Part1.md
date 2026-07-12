# 🐍 Day 10 - Understanding `for` Loops & the `range()` Function (Part 1)

Welcome back! 🎉

Today we explored one of the most powerful features in Python:

# 🔄 Loops

Until now, whenever we wanted to print something many times, we had to write many `print()` statements.

For example:

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

This works...

But imagine printing your name **100 times**!

That would be a lot of typing.

There must be an easier way.

Python gives us something called a **loop**.

A loop allows us to repeat the same set of instructions many times.

---

# 🧠 Think Like a Programmer

Whenever programmers solve a problem, they think in three simple steps.

```
Input
↓

Processing

↓

Output
```

Today's problem was:

```
Print your name many times.
```

### Input

```
Your name
```

### Processing

```
Repeat printing the name many times.
```

### Output

```
Your name printed again and again.
```

---

# 🔄 Our First `for` Loop

We wrote:

```python
name = "Charvi & Eashan"

for i in range(5):
    print(name)
```

Output:

```
Charvi & Eashan
Charvi & Eashan
Charvi & Eashan
Charvi & Eashan
Charvi & Eashan
```

Python repeated the print statement **5 times**.

---

# 🧩 Understanding the Syntax

Let's understand every part.

```python
for i in range(5):
```

It may look confusing at first, but it is actually very simple.

```
for
 │
 │
 └── Repeat something

i
 │
 │
 └── A variable that changes every time the loop runs

range(5)
 │
 │
 └── Repeat 5 times

:
 │
 │
 └── The loop starts here

Indentation
 │
 │
 └── Everything inside the loop repeats
```

---

# 📏 Why Do We Use Indentation?

Look carefully.

```python
for i in range(5):
    print(name)
```

Notice the spaces before:

```python
print(name)
```

This is called **indentation**.

Python uses indentation to know:

> "This statement belongs to the loop."

Every statement with the same indentation will execute repeatedly.

Example:

```python
for i in range(3):
    print("Apple")
    print("Banana")
    print("Orange")
```

Output:

```
Apple
Banana
Orange
Apple
Banana
Orange
Apple
Banana
Orange
```

Python repeats **all three print statements** because they are inside the loop.

---

# 🎯 Understanding `range()`

The `range()` function tells Python:

> "How many times should I repeat?"

The simplest form is:

```python
range(stop)
```

Example:

```python
range(5)
```

Python starts counting from **0**.

It stops **before** 5.

Numbers produced:

```
0
1
2
3
4
```

---

# 📊 Visualising `range(5)`

```
Start

0 → 1 → 2 → 3 → 4
                │
                ▼
              Stop
```

Notice:

Python does **NOT** include **5**.

---

# 🤔 What is the Variable `i`?

We wrote:

```python
for i in range(5):
```

What is `i`?

It is simply a variable.

Just like:

```python
name = "Charvi"
```

We can print it.

Example:

```python
for i in range(5):
    print(i)
```

Output:

```
0
1
2
3
4
```

Every time the loop runs,

Python changes the value of `i`.

---

# 🧠 Think Like Python

Iteration 1

```
i = 0

↓

print(i)
```

Output

```
0
```

---

Iteration 2

```
i = 1

↓

print(i)
```

Output

```
1
```

---

Iteration 3

```
i = 2

↓

print(i)
```

Output

```
2
```

Python continues until `range()` finishes.

---

# 🎯 Using `range(start, stop)`

Sometimes we don't want to start from zero.

We can write:

```python
range(1,5)
```

Python starts from **1**.

Stops before **5**.

Output:

```
1
2
3
4
```

---

# 📊 Visualising `range(1,5)`

```
Start

1 → 2 → 3 → 4
              │
              ▼
            Stop
```

Notice:

Python still does **NOT** include **5**.

---

# 🎯 Using `range(start, stop, step)`

Sometimes we want to jump by more than one number.

Example:

```python
range(1,10,2)
```

Output:

```
1
3
5
7
9
```

Python jumps by **2** every time.

---

# 📊 Visualising `range(1,10,2)`

```
1 -----> 3 -----> 5 -----> 7 -----> 9

Jump by 2 every time
```

---

Great job! 🎉

In the next part, we'll learn:

* Reverse loops
* Negative step values
* Looping through strings
* A surprise program that made everyone excited!
