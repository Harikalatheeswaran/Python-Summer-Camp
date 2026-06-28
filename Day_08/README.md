# 🐍 Day 08 - Using `if`, `elif` and `else` with Animals

Welcome back! 🎉

Today we used everything we learned about **`if`**, **`elif`**, and **`else`** to build a fun program.

Our program asked the user to choose an animal and then printed the sound that the animal makes.

Along the way, we also revised one of the most important ways programmers think when solving problems.

---

# 🧠 How Programmers Think

Whenever we solve a programming problem, we first think about three things.

## 1️⃣ Input

What information will the user give us?

Example:

```text
Animal name
```

---

## 2️⃣ Processing

What should the computer do with that information?

Example:

* Check whether the animal is a dog, cat or bird.
* Decide which sound to print.

---

## 3️⃣ Output

What should the computer display?

Example:

```text
Dog says: Bow Bow!
```

---

Our program looked like this:

```text
           Input
             │
             ▼
      Animal Name
             │
             ▼
        Processing
(Check which animal was entered)
             │
             ▼
           Output
(Print the correct animal sound)
```

---

# 🎯 Today's Problem

We wanted to create a small animal sound program.

The user can choose one of these animals:

```text
🐕 Dog
🐈 Cat
🐥 Bird
```

If the user enters any other animal, we display:

```text
Animal does not exist.
```

---

# ✏️ Step 1 - Display the Animals

First, we show the user the available animals.

```python
print("There are 3 animals : ")
print("🐕 dog")
print("🐈 cat")
print("🐥 bird")
```

Output:

```text
There are 3 animals :

🐕 dog
🐈 cat
🐥 bird
```

---

# ✏️ Step 2 - Take Input

Now we ask the user to type the animal name.

```python
animal = input("Type the animal : ")
```

Example:

```text
dog
```

The value entered by the user is stored inside the variable:

```python
animal
```

---

# ✏️ Step 3 - Check the First Condition

```python
if animal == "dog":
```

Python asks:

```text
Did the user type "dog"?
```

If the answer is YES:

```python
print("Dog says 🐶: Bow Bow!")
```

---

# ✏️ Step 4 - Check the Second Condition

If the first condition is False, Python moves to the next condition.

```python
elif animal == "cat":
```

Python asks:

```text
Did the user type "cat"?
```

If YES:

```python
print("Cat says 😸: Meow Meow!")
```

---

# ✏️ Step 5 - Check the Third Condition

If the first two conditions are False, Python checks:

```python
elif animal == "bird":
```

If YES:

```python
print("Bird says 🐤: Chick Chick!")
```

---

# ✏️ Step 6 - The `else` Block

If none of the conditions are True, Python finally reaches:

```python
else:
```

It prints:

```python
print("Animal does not exist.")
```

---

# 🧠 How Python Thinks

Python checks the conditions one by one from top to bottom.

As soon as it finds the **first True condition**, it executes that block and **stops checking the remaining conditions**.

---

# 📊 Example 1 - User enters "dog"

```text
             dog
              │
              ▼
      Is animal == "dog" ?
          /            \
       YES              NO
        │
        ▼
Print "Bow Bow!"
        │
        ▼
     🛑 STOP

Python does NOT check:

animal == "cat"
animal == "bird"
else
```

---

# 📊 Example 2 - User enters "cat"

```text
             cat
              │
              ▼
      Is animal == "dog" ?
          /            \
       YES              NO
                          │
                          ▼
             Is animal == "cat" ?
                 /            \
              YES              NO
               │
               ▼
      Print "Meow Meow!"
               │
               ▼
            🛑 STOP

Python does NOT check:

animal == "bird"
else
```

---

# 📊 Example 3 - User enters "bird"

```text
             bird
               │
               ▼
      Is animal == "dog" ?
               │
              NO
               ▼
      Is animal == "cat" ?
               │
              NO
               ▼
     Is animal == "bird" ?
            /         \
         YES           NO
          │
          ▼
 Print "Chick Chick!"
          │
          ▼
       🛑 STOP

Python does NOT check:

else
```

---

# 📊 Example 4 - User enters "lion"

```text
             lion
              │
              ▼
      Is animal == "dog" ?
              │
             NO
              ▼
      Is animal == "cat" ?
              │
             NO
              ▼
     Is animal == "bird" ?
              │
             NO
              ▼
             else
              │
              ▼
 Print "Animal does not exist."
```

---

# 💡 Think Like Python

Imagine Python is reading your program.

It always starts from the top.

```text
Condition 1

↓

Condition 2

↓

Condition 3

↓

else
```

As soon as Python finds one condition that is **True**, it immediately stops checking the rest.

---

# 📝 Complete Program

```python
# We write a program to ask the user to enter an animal name.
# We have 3 animals: dog, cat and bird.
# If the user enters one of these animals,
# we print the sound it makes.
# Otherwise, we print "Animal does not exist."

# How programmers think:
# Input → Processing → Output

print("There are 3 animals : ")
print("🐕 dog")
print("🐈 cat")
print("🐥 bird")

animal = input("Type the animal : ")

if animal == "dog":
    print("Dog says 🐶: Bow Bow!")

elif animal == "cat":
    print("Cat says 😸: Meow Meow!")

elif animal == "bird":
    print("Bird says 🐤: Chick Chick!")

else:
    print("Animal does not exist.")
```

---

# 🏁 What We Learned Today

✅ Input → Processing → Output

✅ Taking user input

✅ Using `if`

✅ Using `elif`

✅ Using `else`

✅ How Python checks conditions from top to bottom

✅ Python stops checking after the first True condition

✅ Writing fun interactive programs

---

# 🚀 Homework

Create a new file called:

```python
favorite_fruit.py
```

Ask the user to enter a fruit.

Available fruits:

* 🍎 apple
* 🍌 banana
* 🍇 grapes

If the user enters one of these fruits, print a fun message.

Example:

```text
Apple is crunchy! 🍎
```

If the user enters any other fruit, print:

```text
Sorry! We don't have information about that fruit.
```

---

🎉 Great job!

Today you built another interactive Python program and became even better at using **`if`**, **`elif`**, and **`else`**. Keep practicing, and soon you'll be able to build your own games and mini projects!
