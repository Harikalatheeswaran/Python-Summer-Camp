# 🐍 Day 07 - Introduction to `if`, `elif` and `else`

Welcome back! 🎉

Today we learned how Python can choose **only one option** from many choices.

This is done using:

* `if`
* `elif`
* `else`

We also learned an important way that programmers think when solving problems.

---

# 🧠 How Programmers Think

Before writing any program, we should think about three things.

## 1️⃣ Input

What information will the user give us?

Example:

```text
Student's marks
```

---

## 2️⃣ Processing

What should the computer do with that information?

Example:

* Compare the marks
* Decide the grade

---

## 3️⃣ Output

What should the computer display?

Example:

```text
The grade is A
```

---

Today our program looked like this:

```text
Input
↓

Marks

↓

Processing

Compare the marks

↓

Output

Grade
```

---

# 🎯 Today's Problem

Our English teacher asked us to write a program.

The program should give grades based on marks.

| Marks        | Grade |
| ------------ | ----- |
| 90 and above | A     |
| 80–89        | B     |
| 70–79        | C     |
| Below 70     | D     |

---

# ✍️ Step 1 - Take Input

We first ask the user for the marks.

```python
marks = input("Write the student's marks : ")
```

Remember:

`input()` always gives us a **string**.

---

# ✍️ Step 2 - Convert to Integer

```python
score = int(marks)
```

Now Python can compare numbers correctly.

---

# 🤔 Our First Attempt

At first, we wrote multiple `if` statements.

```python
if score >= 90:
    print("The grade is A")

if score >= 80:
    print("The grade is B")

if score >= 70:
    print("The grade is C")
```

---

# ❓What Happened?

Suppose the student scored:

```text
100
```

Python checks:

```text
Is 100 >= 90 ?
```

✅ Yes

So it prints:

```text
The grade is A
```

---

Then Python moves to the next `if`.

It asks:

```text
Is 100 >= 80 ?
```

✅ Yes

So it prints:

```text
The grade is B
```

---

Then Python checks again.

```text
Is 100 >= 70 ?
```

✅ Yes

So it prints:

```text
The grade is C
```

---

The output became:

```text
The grade is A
The grade is B
The grade is C
```

But this is **not correct**.

A student should receive only **one grade**.

---

# 💡 The Solution - `elif`

To solve this problem, we changed the program.

```python
if score >= 90:
    print("The grade is A")

elif score >= 80:
    print("The grade is B")

elif score >= 70:
    print("The grade is C")

else:
    print("The grade is D")
```

---

# 🧠 How Does `elif` Work?

Python starts at the top.

It checks the first condition.

If the first condition is **True**:

✅ Run that block.

🚫 Ignore everything else.

Python does **not** check the remaining `elif` statements.

---

# 🎯 Example 1

Student's marks:

```text
95
```

Python asks:

```text
Is 95 >= 90 ?
```

✅ Yes

Python prints:

```text
The grade is A
```

Then Python stops checking.

It does **not** check:

```text
Is 95 >= 80 ?
```

or

```text
Is 95 >= 70 ?
```

---

# 🎯 Example 2

Student's marks:

```text
82
```

Python asks:

```text
Is 82 >= 90 ?
```

❌ No

Move to the next condition.

```text
Is 82 >= 80 ?
```

✅ Yes

Python prints:

```text
The grade is B
```

Then Python stops.

---

# 🎯 Example 3

Student's marks:

```text
72
```

Python checks:

```text
>= 90
```

❌ No

```text
>= 80
```

❌ No

```text
>= 70
```

✅ Yes

Output:

```text
The grade is C
```

---

# 🎯 Example 4

Student's marks:

```text
40
```

Python checks:

```text
>= 90
```

❌ No

```text
>= 80
```

❌ No

```text
>= 70
```

❌ No

Now Python reaches:

```python
else:
```

Output:

```text
The grade is D
```

---

# 🏁 What We Learned Today

✅ How to think in terms of:

* Input
* Processing
* Output

✅ Difference between multiple `if` statements and `if-elif-else`

✅ Why `elif` is useful

✅ Python checks conditions from top to bottom.

✅ As soon as one condition is `True`, Python stops checking the remaining `elif` conditions.

---

# 🚀 Homework

Create a new program called:

```python
weather.py
```

Ask the user to enter the weather.

If the weather is:

```text
sunny
```

Print:

```text
Wear sunglasses! 😎
```

If the weather is:

```text
rainy
```

Print:

```text
Take an umbrella! ☔
```

Otherwise print:

```text
Have a great day! 😊
```

---

🎉 Great job!

Today you learned how to make Python choose **one answer** from many possibilities. This is an important skill that programmers use in almost every program they write.
