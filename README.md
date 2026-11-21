# 🎓 Student Grade Tracker

A small Python command-line program that adds up a student's quiz, midterm and final grades and tells you whether the student **passed or failed**. It can handle several students in one run and shows a class summary at the end.

![Python](https://img.shields.io/badge/Python-3-3776AB?style=flat-square&logo=python&logoColor=white)
![Tests](https://img.shields.io/badge/tests-pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)

## 📌 Features

- Enter a student's name and their quiz, midterm and final grades
- Total grade = quiz + midterm + final
- **Pass** when the total is **60 or more**, otherwise **Fail**
- Input validation: non-numbers, negative numbers and empty names are rejected and asked again (the program no longer crashes)
- Enter several students in one run and see the number of students, the class average and how many passed
- Unit tests with `pytest`

## 🛠️ Built with

- Python 3 (standard library only)
- `pytest` for tests (development only)

## ▶️ Example

```text
Enter student name: Sarah
Enter quiz grade: 20
Enter mid grade: 25
Enter final grade: 40
Student Name: Sarah
Total Grade: 85.0
Status: Pass
Add another student? (y/n): n
```

Invalid input is handled gracefully:

```text
Enter quiz grade: abc
Invalid input (grade must be a number). Please enter a number such as 20 or 17.5.
```

## 🚀 How to run

```bash
git clone https://github.com/ghadahh2004/Student-Grade-Tracker.git
cd Student-Grade-Tracker
python main.py
```

## 🧪 Run the tests

```bash
pip install pytest
python -m pytest
```

Tests also run automatically on every pull request through GitHub Actions.

## 📂 Project structure

```text
Student-Grade-Tracker/
├── main.py            # the program (logic functions + command-line interface)
├── tests/
│   └── test_main.py   # unit tests
├── conftest.py        # lets pytest import main.py
└── README.md
```

## 🔭 Ideas for future improvements

- Let each grade have its own maximum mark and weight, instead of simply adding the three grades
- Save students' results to a CSV file
- Add letter grades (A, B, C, ...)
- A simple graphical interface

## 📖 What I learned

- Reading user input with `input()` and converting it to `float`
- Handling errors with `try` / `except`
- Splitting code into small, testable functions
- Writing unit tests with `pytest`
