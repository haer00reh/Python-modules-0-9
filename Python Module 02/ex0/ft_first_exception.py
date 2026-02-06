def check_temperature(temp_str: str) -> int:
    """Check if the temperature string is valid and within 0-40°C."""
    print(f"Testing Temp: {temp_str}")
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: '{temp_str}' is not a valid number")
    if temp > 40:
        raise ValueError(f"Error: {temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"Error: {temp}°C is too cold for plants (min 0°C)")
    else:
        print(f"Temperature {temp}°C is perfect for plants!")
    return temp


def test_temperature_input() -> None:
    """Test the check_temperature function with sample inputs."""
    print("=== Garden Temperature Checker ===")
    lst = ["-1", "21", "230", "false"]
    for each in lst:
        try:
            check_temperature(each)
        except ValueError as error:
            print(error)
    print("All tests completed - program didn't crash!")
test_temperature_input()