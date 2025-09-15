def area_of_rectangle(length: float, width: float) -> float:
    """Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width


if __name__ == "__main__":
    print("Area of Rectangle is", area_of_rectangle(10, 20))
