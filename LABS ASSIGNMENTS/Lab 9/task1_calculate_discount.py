"""
Lab 9 – Task 1
Automatic Code Commenting & Documentation
"""

# ---------------------------------------------------
# Version 1: AI-Generated Comments
# ---------------------------------------------------
def calculate_discount_ai(price, discount_rate):
    # Calculates the discount amount
    discount = price * discount_rate / 100
    # Subtracts the discount amount from the original price
    final_price = price - discount
    return final_price


# ---------------------------------------------------
# Version 2: Manual Comments
# ---------------------------------------------------
def calculate_discount_manual(price, discount_rate):
    # Step 1: Calculate the discount amount by multiplying price with discount rate
    discount = price * discount_rate / 100
    # Step 2: Subtract discount amount from the original price to get final price
    final_price = price - discount
    return final_price


# ---------------------------------------------------
# Version 3: Google-Style Docstring
# ---------------------------------------------------
def calculate_discount_google(price, discount_rate):
    """
    Calculate the final price after applying a discount.

    Args:
        price (float): The original price of the item.
        discount_rate (float): The discount rate as a percentage.

    Returns:
        float: The final price after applying the discount.
    """
    discount = price * discount_rate / 100
    final_price = price - discount
    return final_price


# ---------------------------------------------------
# Version 4: NumPy-Style Docstring
# ---------------------------------------------------
def calculate_discount_numpy(price, discount_rate):
    """
    Calculate the final price after applying a discount.

    Parameters
    ----------
    price : float
        The original price of the item.
    discount_rate : float
        The discount rate as a percentage.

    Returns
    -------
    float
        The final price after applying the discount.
    """
    discount = price * discount_rate / 100
    final_price = price - discount
    return final_price


# ---------------------------------------------------
# Test the functions
# ---------------------------------------------------
if __name__ == "__main__":
    price = 1000
    discount_rate = 10

    # Calculate discount separately for display
    discount_amount = price * discount_rate / 100

    print("Original Price:", price)
    print("Discount Rate:", discount_rate, "%")
    print("Discount Amount:", discount_amount)
    print("AI Version Final Price:", calculate_discount_ai(price, discount_rate))
    print("Manual Version Final Price:", calculate_discount_manual(price, discount_rate))
    print("Google Docstring Final Price:", calculate_discount_google(price, discount_rate))
    print("NumPy Docstring Final Price:", calculate_discount_numpy(price, discount_rate))
