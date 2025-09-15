def grade(score: int) -> str:
    """Return the letter grade for a numeric score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
print("Grade for score 85 is", grade(85))
print("Grade for score 72 is", grade(72))
print("Grade for score 59 is", grade(59))
print("Grade for score 91 is", grade(91))
print("Grade for score 45 is", grade(45))
print("Grade for score 78 is", grade(78))