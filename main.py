"""Student Grade Tracker.

Asks for a student's quiz, midterm and final grades, adds them up and shows
whether the student passed. Several students can be entered in one run.
"""

import math

PASS_MARK = 60


def calculate_total(quiz, mid, final):
    """Return the total grade (the three grades added together)."""
    return quiz + mid + final


def get_status(total, pass_mark=PASS_MARK):
    """Return "Pass" if total reaches the pass mark, otherwise "Fail"."""
    return "Pass" if total >= pass_mark else "Fail"


def parse_grade(text):
    """Convert text typed by the user to a grade.

    Raises ValueError for anything that is not a finite, non-negative number.
    """
    try:
        value = float(text)
    except ValueError:
        raise ValueError("grade must be a number") from None
    if math.isnan(value) or math.isinf(value):
        raise ValueError("grade must be a real number")
    if value < 0:
        raise ValueError("grade cannot be negative")
    return value


def ask_grade(label):
    """Keep asking until the user types a valid grade."""
    while True:
        try:
            return parse_grade(input(f"Enter {label} grade: "))
        except ValueError as error:
            print(f"Invalid input ({error}). Please enter a number such as 20 or 17.5.")


def ask_name():
    """Keep asking until the user types a non-empty name."""
    while True:
        name = input("Enter student name: ").strip()
        if name:
            return name
        print("Name cannot be empty.")


def summarize(results):
    """Return (count, average, passed) for a list of (name, total, status)."""
    count = len(results)
    average = sum(total for _, total, _ in results) / count if count else 0.0
    passed = sum(1 for _, _, status in results if status == "Pass")
    return count, average, passed


def main():
    results = []
    while True:
        name = ask_name()
        quiz = ask_grade("quiz")
        mid = ask_grade("mid")
        final = ask_grade("final")

        total = calculate_total(quiz, mid, final)
        status = get_status(total)
        results.append((name, total, status))

        print("Student Name:", name)
        print("Total Grade:", total)
        print("Status:", status)

        if input("Add another student? (y/n): ").strip().lower() != "y":
            break

    if len(results) > 1:
        count, average, passed = summarize(results)
        print(f"\nStudents: {count} | Average: {average:.1f} | Passed: {passed}/{count}")


if __name__ == "__main__":
    main()
