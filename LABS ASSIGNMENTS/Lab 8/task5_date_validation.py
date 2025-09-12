from datetime import datetime

# -----------------------------
# Task 5: Date Validation & Formatting
# -----------------------------
def validate_and_format_date(date_str):
    """
    Validate date in MM/DD/YYYY format and convert to YYYY-MM-DD.
    Returns "Invalid Date" if format is wrong or date is invalid.
    """
    try:
        # Parse input using datetime
        valid_date = datetime.strptime(date_str, "%m/%d/%Y")
        # Convert to required format
        return valid_date.strftime("%Y-%m-%d")
    except ValueError:
        return "Invalid Date"


# -----------------------------
# Assert-based Tests
# -----------------------------
if __name__ == "__main__":
    # Example Tests
    assert validate_and_format_date("10/15/2023") == "2023-10-15"
    assert validate_and_format_date("02/30/2023") == "Invalid Date"  # Feb 30 is invalid
    assert validate_and_format_date("01/01/2024") == "2024-01-01"

    # Extra AI-Generated Tests
    assert validate_and_format_date("12/31/2023") == "2023-12-31"  # last day of year
    assert validate_and_format_date("00/10/2023") == "Invalid Date"  # invalid month
    assert validate_and_format_date("06/31/2023") == "Invalid Date"  # June has 30 days
    assert validate_and_format_date("7/4/2023") == "2023-07-04"      # single-digit month/day

    print("\n✅ All Task 5 Date Validation test cases passed successfully!")
