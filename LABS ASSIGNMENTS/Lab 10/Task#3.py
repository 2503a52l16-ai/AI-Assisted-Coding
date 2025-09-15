def calculate_percentage(amount: float, percentage: float) -> float:
    """Calculate a given percentage of an amount.

    Args:
        amount (float): The base amount.
        percentage (float): The percentage value.

    Returns:
        float: The calculated percentage of the amount.
    """
    return amount * percentage / 100


# Example usage
total_amount = 200   # Base value
discount_rate = 15   # Percentage to apply

# Calculate and print 15% of 200
print("Discount Amount is", calculate_percentage(total_amount, discount_rate))
