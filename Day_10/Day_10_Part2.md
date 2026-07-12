# 🐍 Day 10 - Understanding `for` Loops & the `range()` Function (Part 2)

Welcome back! 🎉

In Part 1, we learned:

* What a loop is
* Why loops are useful
* The syntax of a `for` loop
* What indentation means
* How `range(5)`, `range(1,5)` and `range(1,10,2)` work

Today we explored a few more exciting examples of the `range()` function and got a surprise introduction to looping through strings!

---

# 🔢 Counting Backwards

So far, we have been counting forwards.

But did you know Python can also count backwards?

Yes! 🎉

To count backwards, we use a **negative step**.

---

# 🎯 Example 1 - Counting Backwards

```python
for i in range(10, 5, -1):
    print(i)
```

Output:

```text
10
9
8
7
6
```

Notice that Python starts from **10**.

Then it goes backwards by **1**.

It stops before **5**.

---

# 📊 Visualising `range(10,5,-1)`

```text
Start

10 ← 9 ← 8 ← 7 ← 6
 ▲
 │
Jump backwards by 1

Stop before 5
```

---

# 🤔 Why Did We Use -1?

The third number inside `range()` is called the **step**.

A positive step moves **forward**.

```text
+1
+2
+3
```

A negative step moves **backward**.

```text
-1
-2
-3
```

---

# 🎯 Example 2 - What Happens Here?

```python
for i in range(0, -6):
    print(i)
```

Many beginners think this will print:

```text
0
-1
-2
-3
-4
-5
```

But...

Nothing gets printed!

Why?

Because Python is trying to move **forward** by default.

It starts at **0**.

The stop value is **-6**.

Python cannot reach **-6** by moving forward.

---

# 📊 Visualising `range(0,-6)`

```text
Start

0 → 1 → 2 → 3 → 4 → ...

Target is:

-6

❌ Python can never reach -6 by moving forward.
```

So the loop never starts.

---

# ✅ Correct Way

```python
for i in range(0, -6, -1):
    print(i)
```

Output:

```text
0
-1
-2
-3
-4
-5
```

---

# 📊 Visualising `range(0,-6,-1)`

```text
0 ← -1 ← -2 ← -3 ← -4 ← -5

Jump backwards by 1

Stop before -6
```

---

# 🧠 Remember This Rule

```text
Positive Step (+)

↓

Move Forward →

Negative Step (-)

↓

Move Backward ←
```

---

# 🌟 A Surprise!

Until now we thought loops only worked with numbers.

Then we tried something surprising.

```python
for i in "birds":
    print(i)
```

Everyone was excited because...

Python can also loop through **letters**!

---

# 🤔 What Happens?

The word is:

```text
birds
```

Python looks at one letter at a time.

---

# 📊 Visualising the Loop

```text
┌──────────────────────┐
│      birds           │
└──────────────────────┘

Iteration 1

b

↓

print(i)

↓

b
```

---

Iteration 2

```text
i

↓

print(i)

↓

i
```

---

Iteration 3

```text
r

↓

print(i)

↓

r
```

---

Iteration 4

```text
d

↓

print(i)

↓

d
```

---

Iteration 5

```text
s

↓

print(i)

↓

s
```

---

# 📊 Complete Flow

```text
Word

birds

      │
      ▼

Letter 1

b

↓

Print b

↓

Letter 2

i

↓

Print i

↓

Letter 3

r

↓

Print r

↓

Letter 4

d

↓

Print d

↓

Letter 5

s

↓

Print s

↓

Loop Ends
```

---

# 🧠 Think Like Python

When Python sees:

```python
for i in "birds":
```

It thinks:

```text
Take the first letter.

↓

Put it inside i.

↓

Run the code.

↓

Take the next letter.

↓

Repeat.

↓

Continue until every letter has been used.
```

---

# 💡 Common Beginner Mistakes

### ❌ Forgetting Indentation

Wrong:

```python
for i in range(5):
print(i)
```

Correct:

```python
for i in range(5):
    print(i)
```

---

### ❌ Expecting the Stop Number to Print

```python
range(5)
```

Prints:

```text
0
1
2
3
4
```

It does **NOT** print **5**.

---

### ❌ Using a Positive Step When Going Backwards

Wrong:

```python
range(10,5)
```

Nothing happens.

Correct:

```python
range(10,5,-1)
```

---

# 🏁 What We Learned Today

✅ `range(start, stop)`

✅ `range(start, stop, step)`

✅ Positive step

✅ Negative step

✅ Forward loops

✅ Reverse loops

✅ Looping through strings

✅ Every letter can be visited one by one

---

# 🚀 Homework

## Question 1

Print the numbers from **5 to 15**.

---

## Question 2

Print only the even numbers from **2 to 20**.

(Hint: Use a step of **2**.)

---

## Question 3

Print the numbers from **20 down to 10**.

---

## Question 4

Store your name in a variable.

Use a loop to print each letter one by one.

Example:

```python
name = "Alex"

for letter in name:
    print(letter)
```

---

## 🌟 Bonus Challenge

Can you predict the output before running?

```python
for i in range(3, 15, 3):
    print(i)
```

Then check your answer by running the program!

---

# 🎉 Congratulations!

Today you learned that loops are much more powerful than simply repeating print statements.

You discovered that Python can:

* Count forwards
* Count backwards
* Skip numbers
* Visit every letter in a word

These are the building blocks for writing exciting programs, games, and puzzles in Python.

Keep practicing, keep experimenting, and most importantly...

**Have fun coding! 🐍🚀**
