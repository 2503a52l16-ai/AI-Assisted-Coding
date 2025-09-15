# Calculate average score of a student
from typing import List

def calc_average(marks: List[int]) -> float:
    """Calculate and return the average of a list of numeric marks.

    Args:
        marks (List[int]): List of student marks (non-empty).

    Returns:
        float: The average score.

    Raises:
        ValueError: If marks list is empty.
    """
    if not marks:
        raise ValueError("Marks list cannot be empty")

    total = 0
    for m in marks:
        total += m
    average = total / len(marks)
    return average

marks = [85, 90, 78, 92]
print("Average Score is", calc_average(marks))
