from typing import List

def welcome_students(student_list: List[str]) -> None:
    """Print a welcome message for each student in the list."""
    for student in student_list:
        print("Welcome", student)


if __name__ == "__main__":
    students = ["Alice", "Bob", "Charlie"]
    welcome_students(students)
