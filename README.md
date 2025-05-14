# Python Beginner Mini Projects

This repository contains three beginner-level Python projects designed to practice basic programming skills, user input handling, and control flow.

## Project 1: Voice Assistant

### Description

A simple text-based voice assistant that can perform basic tasks like:

* Greet the user
* Search Google and YouTube
* Tell the current time and date
* Exit the program

### Features

* Uses basic `input` and `print` functions.
* Utilizes web search by opening URLs via the `webbrowser` module.
* Uses the `datetime` module to display date and time.

### Usage Example

```
Hi, I am your assistant.
Please enter your name: John
Hello John, what can I do for you?

Options:
1. Search Google
2. Search YouTube
3. Tell me the time
4. Tell me the date
5. Exit
```

---

## Project 2: BMI Calculator

### Description

This project calculates the Body Mass Index (BMI) of a user based on their weight and height inputs.

### Features

* Input validation for weight and height.
* Calculates BMI and classifies into:

  * Underweight
  * Normal weight
  * Overweight
  * Obese
* Provides health advice based on BMI category.

### Usage Example

```
Enter your weight in kilograms: 70
Enter your height in meters: 1.75

Results:
Your BMI is: 22.86
Category: Normal weight
You are in a healthy weight range. Keep maintaining good habits!
```

---

## Project 3: Password Generator

### Description

A customizable random password generator that allows the user to select the types of characters included in the password.

### Features

* User-defined password length.
* Option to include:

  * Lowercase letters
  * Uppercase letters
  * Numbers
  * Symbols
* Displays the generated password and evaluates its strength.

### Usage Example

```
Enter desired password length: 12
Include lowercase letters? (y/n): y
Include uppercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

Your generated password is:
Aj3@9kLm&1Zq
Password strength: Strong
```

---

## Getting Started

1. Clone the repository or download the project files.
2. Ensure Python 3.x is installed.

---

## Requirements

* Python 3.x
* No external libraries required. Uses standard Python libraries:

  * `datetime`
  * `webbrowser`
  * `random`
  * `string`

---

## How to Run

Open terminal or command prompt in the project directory and run any of the Python files:

```
python task1_voice_assistant.py
python task2_bmi_calci.py
python task3_password_generator.py
```

---

