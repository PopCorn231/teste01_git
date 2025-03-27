def calculate_average():
    """

    Prompts the user to input numbers separated by spaces,
    calculates the average, and returns the result.
    """
    try:
        # Prompt the user for numbers
        numbers = input("Enter numbers separated by spaces: ")
        # Convert input to a list of floats
        num_list = [float(num) for num in numbers.split()]
        # Return the average
        return sum(num_list) / len(num_list) if num_list else 0
    except ValueError:
        return "Invalid input. Please enter valid numbers."
