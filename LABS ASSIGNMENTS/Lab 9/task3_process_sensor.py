"""
Lab 9 – Task 3
AI-Assisted Code Summarization
"""

# ---------------------------------------------------
# Summary Comment (2–3 lines)
# ---------------------------------------------------
# This function processes raw sensor data by cleaning out missing values,
# calculating the average, and identifying anomalies that deviate
# significantly (more than 10 units) from the average.


def process_sensor_data(data):
    """
    Process sensor data to compute average and detect anomalies.

    The function removes invalid values (None), calculates the average of the
    cleaned dataset, and identifies anomalies that deviate more than 10 units
    from the average.

    Args:
        data (list of float or int): List of sensor readings, may include None.

    Returns:
        dict: A dictionary containing:
            - "average" (float): The average of cleaned sensor readings.
            - "anomalies" (list): Values that deviate more than 10 units
              from the average.
    """

    # ---------------------------------------------------
    # Flow-Style Step-by-Step Comments
    # ---------------------------------------------------
    # Step 1: Remove None values from the input data
    cleaned = [x for x in data if x is not None]

    # Step 2: Compute the average of the cleaned dataset
    avg = sum(cleaned) / len(cleaned)

    # Step 3: Identify values that deviate more than 10 units from the average
    anomalies = [x for x in cleaned if abs(x - avg) > 10]

    # Step 4: Return the results as a dictionary with average and anomalies
    return {"average": avg, "anomalies": anomalies}


# ---------------------------------------------------
# Real-World Use Case Documentation
# ---------------------------------------------------
"""
This function can be applied in various real-world sensor data processing scenarios. 
For example, in an IoT-based smart home system, it can help identify faulty sensor 
readings that deviate too much from normal values. In industrial monitoring systems, 
it can be used to detect abnormal temperature, pressure, or vibration readings, 
indicating potential equipment failure. Similarly, in health monitoring devices, 
the function could flag unusual heart rate or oxygen level readings for further 
inspection. By automatically filtering and summarizing sensor data, this function 
supports real-time anomaly detection and reliable decision-making.
"""


# ---------------------------------------------------
# Test the function
# ---------------------------------------------------
if __name__ == "__main__":
    sample_data = [20, 21, None, 22, 50, 19, 20, 18, 200, None, 21]
    result = process_sensor_data(sample_data)
    print("Processed Sensor Data:", result)
