# 🐍 Day 12 - Combining `if` Statements and `for` Loops (Part 1)

Welcome back! 🎉

Today we learned something very exciting!

Until now, we learned two important concepts separately:

✅ `if`, `elif` and `else`

✅ `for` loops

Today we learned that **real programmers combine different concepts together** to solve bigger problems.

---

# 📝 Quick Recap

Before starting today's lesson, we revised the different ways to use the `range()` function.

---

## Example 1

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

---

### 📊 Visualisation

```text
Start

0 → 1 → 2 → 3 → 4
                │
                ▼
              Stop
```

Python starts from **0** and stops **before** **5**.

---

## Example 2

```python
for i in range(1, 6):
    print(i)
```

Output

```text
1
2
3
4
5
```

---

### 📊 Visualisation

```text
Start

1 → 2 → 3 → 4 → 5
                │
                ▼
              Stop
```

Python starts from **1** and stops before **6**.

---

## Example 3

```python
for i in range(1, 10, 2):
    print(i)
```

Output

```text
1
3
5
7
9
```

---

### 📊 Visualisation

```text
1 -----> 3 -----> 5 -----> 7 -----> 9

Jump by 2 every time
```

The third number inside `range()` is called the **step**.

The step tells Python how many numbers to jump each time.

---

# 🧠 Understanding `range(start, stop, step)`

The `range()` function has three parts.

```python
range(start, stop, step)
```

Let's understand each one.

---

## 🟢 Start

The first number tells Python where to begin.

Example

```python
range(5, 10)
```

Python starts from:

```text
5
```

---

## 🔵 Stop

The second number tells Python where to stop.

**Important Rule**

Python **never prints the stop number**.

Example

```python
range(5,10)
```

Prints

```text
5
6
7
8
9
```

Notice that **10 is not printed.**

---

## 🟣 Step

The third number tells Python how much to jump.

Example

```python
range(2,11,2)
```

Output

```text
2
4
6
8
10
```

Python jumps by **2** every time.

---

# 🎯 Today's Problem

Today we wanted to build a slightly bigger program.

The program should ask the user:

```text
Do you want to print EVEN numbers or ODD numbers?
```

If the user types:

```text
even
```

Print

```text
2
4
6
8
10
12
```

If the user types

```text
odd
```

Print

```text
1
3
5
7
9
11
```

If the user types anything else,

Print

```text
Invalid Choice.
```

---

# 🧠 Think Like a Programmer

Before writing code, we first think about the problem.

```text
Input

↓

Processing

↓

Output
```

---

## Input

```text
even

or

odd
```

---

## Processing

Python checks what the user typed.

Then decides which numbers to print.

---

## Output

Either

```text
2
4
6
8
10
12
```

OR

```text
1
3
5
7
9
11
```

---

# ✍️ Our First Solution

We first solved the problem without using loops.

```python
choice = input("You want to print even or odd numbers between 1 to 12: ")

if choice == "even":
    print(2)
    print(4)
    print(6)
    print(8)
    print(10)
    print(12)

elif choice == "odd":
    print(1)
    print(3)
    print(5)
    print(7)
    print(9)
    print(11)

else:
    print("Invalid Choice.")

print("Charvi & Eashan are learning loops!")
```

---

# 📊 Program Flow

Suppose the user types:

```text
even
```

Python thinks like this:

```text
          User types

             even
               │
               ▼
      Is choice == "even" ?
          /             \
       YES               NO
        │
        ▼
Print 2
Print 4
Print 6
Print 8
Print 10
Print 12
        │
        ▼
      🛑 Skip

      elif

      else

        │
        ▼

Continue Program

↓

Print

"Charvi & Eashan are learning loops!"
```

---

# 🤔 The Big Question

This program works!

But...

What if the teacher asks us to print

```text
1 to 50
```

instead of

```text
1 to 12
```

Would we write

```python
print(2)
print(4)
print(6)
...
print(50)
```

That would be a LOT of typing!

Real programmers always ask themselves:

> **"Can I make my program shorter and smarter?"**

---

# 💡 There Must Be a Better Way

Instead of writing many `print()` statements,

we already know something that repeats work automatically.

Can you guess?

Yes!

🎉 **The `for` loop!**

A `for` loop can print many numbers with just a few lines of code.

In the next part, we will use a `for` loop to make our program much shorter, cleaner, and smarter. We will also combine **`if` statements** and **`for` loops** together to solve the complete problem like real programmers!
