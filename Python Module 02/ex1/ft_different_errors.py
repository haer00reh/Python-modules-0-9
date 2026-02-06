def garden_operations(flag: int) -> None:
    """Perform different garden operations
       that can raise various errors based on the flag."""
    if flag == 0:
        try:
            flag = int("false")
        except ValueError:
            raise ValueError("cant convert a string that contains a NON-DIGIT")
    elif flag == 1:
        try:
            flag = 12 / 0
        except ZeroDivisionError:
            raise ZeroDivisionError("you cant divide by ZERO")
    elif flag == 2:
        try:
            open("BLABLA.txt", "r")
        except FileNotFoundError:
            raise FileNotFoundError("file does NOT exist")
    elif flag == 3:
        try:
            dic = {"book": "knowledge"}
            print(dic["phone"])
        except KeyError:
            raise KeyError("element does NOT exist in the dictionary")


def test_error_types() -> None:
    """Test all the garden_operations error types."""
    print("=== Garden Error Types Demo ===")
    lst = ["ValueError", "ZeroDivisionError", "FileNotFoundError", "KeyError"]
    for n in range(0, 4):
        print(f"\ntesting {lst[n]}...")
        try:
            garden_operations(n)
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, KeyError) as error:
            print(f"Caught: {error}")
    print("\nTesting multiple errors together...")
    try:
        garden_operations(0)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")
test_error_types()