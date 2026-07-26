# 🐍 Day 12 - Combining `if` Statements and `for` Loops (Part 2)

Welcome back! 🎉

In Part 1, we solved the problem by writing many `print()` statements.

Although the program worked, we noticed that writing lots of `print()` statements becomes difficult when the numbers become larger.

Today, we will improve our program by using a **`for` loop**.

---

# 🚀 Using a `for` Loop

Instead of writing:

```python
print(2)
print(4)
print(6)
print(8)
...
print(50)
```

Python can repeat the work for us!

We only need to write:

```python
print("Even numbers from 1 to 50")

for i in range(2, 51, 2):
    print(i)
```

---

## 🧠 Think Like Python

Python sees:

```python
for i in range(2, 51, 2):
```

and thinks:

```text
Start at 2

↓

Print the number

↓

Jump by 2

↓

Print the next number

↓

Repeat

↓

Stop before 51
```

---

## 📊 Visualising the Loop

```text
2 -----> 4 -----> 6 -----> 8 -----> 10 -----> ... -----> 50

Jump by 2 every time
```

Notice something important.

We wrote:

```python
range(2, 51, 2)
```

Python stops before **51**.

Therefore,

the last number printed is:

```text
50
```

---

# 🎯 Printing Odd Numbers

Now let's print odd numbers.

```python
print("Odd numbers from 1 to 50")

for i in range(1, 50, 2):
    print(i)
```

---

## 📊 Visualising the Loop

```text
1 -----> 3 -----> 5 -----> 7 -----> 9 -----> ... -----> 49

Jump by 2 every time
```

Python starts from **1**.

Then jumps by **2**.

So it prints only odd numbers.

---

# 🧩 Combining `if` and `for`

Now we combined everything we have learned.

Until today we learned:

✅ `if`

✅ `elif`

✅ `else`

✅ `for`

Now we can use them together!

---

# 📝 Complete Program

```python
choice = input("You want to print even or odd numbers between 1 to 50: ")

if choice == "even":

    print("Even numbers from 1 to 50")

    for i in range(2, 51, 2):
        print(i)

elif choice == "odd":

    print("Odd numbers from 1 to 50")

    for i in range(1, 50, 2):
        print(i)

else:

    print("Invalid Choice.")

print("Charvi & Eashan are learning loops!")
```

---

# 🧠 How Python Thinks

Suppose the user types:

```text
even
```

Python follows these steps.

```text
Start Program

        │

        ▼

Ask the user

        │

        ▼

User types

even

        │

        ▼

Is choice == "even" ?

       YES ✅

        │

        ▼

Print

Even numbers from 1 to 50

        │

        ▼

Start the for loop

        │

        ▼

2

↓

4

↓

6

↓

8

↓

...

↓

50

        │

        ▼

Loop Finished

        │

        ▼

Skip

elif

Skip

else

        │

        ▼

Print

"Charvi & Eashan are learning loops!"

        │

        ▼

Program Ends
```

---

# 🤔 Why Do We Use `elif`?

Some students asked a very good question.

Why do we write:

```python
if

elif

else
```

instead of

```python
if

if

else
```

Let's understand.

---

Suppose the user types:

```text
even
```

Python checks:

```python
if choice == "even":
```

Answer:

```text
YES ✅
```

Python prints all the even numbers.

Now Python reaches:

```python
elif
```

Python skips it.

Then Python also skips:

```python
else
```

because one condition was already True.

---

## 📊 Visualisation

```text
User

↓

even

↓

if choice == "even"

↓

YES ✅

↓

Run EVEN loop

↓

🛑 Leave the if-elif-else ladder

↓

Continue the remaining program
```

---

# 🚫 What If We Used Two `if` Statements?

Imagine writing:

```python
if choice == "even":
    ...

if choice == "odd":
    ...

else:
    ...
```

Python would check the second `if` **even after** the first one had already run.

That is unnecessary.

Using:

```python
if

elif

else
```

is cleaner and faster because Python stops checking once it finds the correct answer.

---

# 🧠 Think Like a Programmer

Whenever you solve a problem, always ask yourself:

```text
Can I make my program

Shorter?

Cleaner?

Smarter?
```

That is exactly what we did today.

Instead of writing many `print()` statements,

we used a loop.

---

# 🏁 What We Learned Today

✅ How to combine `if` statements and `for` loops.

✅ Why loops save us from writing many `print()` statements.

✅ How Python executes a `for` loop.

✅ Why we use `elif` instead of multiple `if` statements.

✅ How real programmers combine small concepts together to solve bigger problems.

---

# 🚀 Homework

Write a Python program that asks the user whether they want to print **even** numbers or **odd** numbers between **50 and 100**.

### Example

If the user types:

```text
even
```

The program should print:

```text
50
52
54
...
100
```

If the user types:

```text
odd
```

The program should print:

```text
51
53
55
...
99
```

If the user enters anything else, print:

```text
Invalid Choice.
```

---

## 🌟 Challenge

Can you solve the homework **without looking at today's class program**?

Think carefully about:

* Where should the loop start?
* Where should it stop?
* What should the step be?

Try writing the program on your own first.

---

# 🎉 Congratulations!

Today you learned something very important.

Until now, you learned different Python concepts one by one.

Today, you became a better programmer by **combining different concepts together**.

This is exactly how real programmers build games, apps, websites, and software.

Keep practicing, keep experimenting, and most importantly...

### **Have fun coding! 🐍🚀**
