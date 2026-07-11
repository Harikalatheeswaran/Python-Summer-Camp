# 🐍 Day 09 - Understanding Program Flow & Introduction to Loops


Welcome back! 🎉

Today we revised everything we learned about **`if`**, **`elif`**, and **`else`**.

We also got our **first introduction to loops**, one of the most exciting features in Python!

---

# 📝 Quick Recap

Today we revised:

* `if`
* `elif`
* `else`
* Program flow
* How Python checks conditions
* What happens after the conditions finish
* Introduction to `for` loops
* Introduction to the `range()` function

---

# 🧠 How Python Executes a Program

One of the most important things to understand is:

👉 Python reads your program **from top to bottom**.

It executes one line at a time.

Example:

```python
print("Hello")

print("Welcome")

print("Let's Learn Python")
```

Output:

```text
Hello
Welcome
Let's Learn Python
```

---

# 🪜 What is an `if-elif-else` Ladder?

When we write:

```python
if condition1:
    ...

elif condition2:
    ...

elif condition3:
    ...

else:
    ...
```

Python checks the conditions **one after another**, from top to bottom.

This group of conditions is called an:

👉 **if-elif-else ladder**

Think of it like climbing a ladder.

Python starts at the top step and keeps moving down until it finds a condition that is **True**.

---

# 📊 How an if-elif-else Ladder Works

```text
            Start
              │
              ▼
      Is Condition 1 True?
         /             \
      YES               NO
       │                 │
       ▼                 ▼
 Run Block 1      Check Condition 2
       │                 │
       │            Is it True?
       │             /      \
       │          YES        NO
       │           │          │
       ▼           ▼          ▼
     🛑 Exit     Run Block 2  Check Condition 3
                                   │
                              Is it True?
                               /      \
                            YES        NO
                             │          │
                             ▼          ▼
                        Run Block 3    else
                             │          │
                             └────┬─────┘
                                  ▼
                       Continue with the
                        remaining program
```

---

# 🧠 Important Rule

As soon as Python finds a condition that is **True**:

✅ It executes that block.

❌ It skips all the remaining `elif` conditions.

Then...

👉 Python continues with the rest of the program.

---

# 🎯 Example

Suppose we have:

```python
animal = "dog"

if animal == "dog":
    print("Bow Bow!")

elif animal == "cat":
    print("Meow!")

elif animal == "bird":
    print("Chick Chick!")

else:
    print("Animal does not exist.")

print("Eashan & Charvi are super smart!!!")
```

---

# What Happens?

Python asks:

```text
Is animal equal to "dog"?
```

Answer:

```text
YES
```

So Python prints:

```text
Bow Bow!
```

Now Python **comes out of the if-elif-else ladder**.

It does **not** check:

```text
cat
bird
else
```

Instead, Python continues with the next line of the program.

Output:

```text
Bow Bow!
Eashan & Charvi are super smart!!!
```

---

# 📊 Visualising the Program Flow

```text
          Start
            │
            ▼
   Check "dog" condition
            │
         YES ✅
            │
            ▼
 Print "Bow Bow!"
            │
            ▼
 Leave the if-elif-else ladder
            │
            ▼
Print "Eashan & Charvi are super smart!!!"
            │
            ▼
          End
```

---

# 🚀 Introduction to Loops

Now imagine we want to print our name 20 times.

One way would be:

```python
print(name)
print(name)
print(name)
print(name)
...
```

This would become very long and boring!

Instead, Python gives us something called a **loop**.

A loop repeats the same task again and again.

---

# 🔄 Our First Loop

```python
name = "Charvi & Eashan"

for i in range(20):
    print(name)
```

Output:

```text
Charvi & Eashan
Charvi & Eashan
Charvi & Eashan
...
```

It prints the name **20 times**.

---

# 🤔 What is `range()`?

`range()` tells Python:

👉 "How many times should I repeat?"

Example:

```python
range(20)
```

means:

Repeat **20 times**.

---

# 🤔 What is `i`?

In our loop we wrote:

```python
for i in range(20):
```

`i` is a variable.

Just like any other variable, we can print it.

Example:

```python
for i in range(20):
    print(i)
```

Output:

```text
0
1
2
3
4
...
19
```

Notice that Python starts counting from **0**.

---

# 🎯 Different Ways to Use `range()`

We also explored some different forms of the `range()` function.

---

## Example 1

```python
for i in range(15, 20):
    print(i)
```

Output:

```text
15
16
17
18
19
```

Python starts from **15** and stops before **20**.

---

## Example 2

```python
for i in range(1, 20, 2):
    print(i)
```

Output:

```text
1
3
5
7
9
11
13
15
17
19
```

The last number (`2`) is called the **step**.

Python skips by 2 each time.

---

# 🎁 A Sneak Peek

We discovered that loops are very powerful.

Using loops, we can:

* Print something many times.
* Count numbers.
* Build fun games.
* Create patterns.
* Solve problems using fewer lines of code.

We will learn much more about loops in the upcoming classes!

---

# 🏁 What We Learned Today

✅ Python executes programs from top to bottom.

✅ An `if-elif-else` ladder checks conditions one by one.

✅ Once a condition is `True`, Python exits the ladder.

✅ The program continues executing the remaining statements.

✅ Introduction to `for` loops.

✅ Introduction to the `range()` function.

✅ Different ways to use `range()`.

---

# 🚀 Homework

Create a file called:

```python
my_name.py
```

1. Store your name in a variable.

2. Use a `for` loop to print your name **10 times**.

Example:

```python
name = "Alex"

for i in range(10):
    print(name)
```

### 🌟 Challenge

Try these different versions and observe the output:

```python
range(5)
```

```python
range(3, 8)
```

```python
range(2, 20, 3)
```

Can you guess the output **before** running the program?

---

🎉 Great job!

Today you learned that Python doesn't stop after an `if-elif-else` ladder. <br>
It continues executing the remaining program. You also got your first exciting introduction to loops, which will help you write shorter and smarter programs!


🎉 Great job!

Today you learned that Python doesn't stop after an `if-elif-else` ladder. It continues executing the remaining program. You also got your first exciting introduction to loops, which will help you write shorter and smarter programs!
