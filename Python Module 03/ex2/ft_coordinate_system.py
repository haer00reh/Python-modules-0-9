import sys
import math

def parse_cords(text: str) -> tuple:
    parts = text.split(",")
    if len(parts) != 3:
        raise ValueError("Coordinates must be x,y,z")

    x, y, z = map(int, parts)
    return (x, y, z)

print("=== Game Coordinate System ===")
def demo() -> None:
    print("Demo testing...")
    test = (10, 20, 5)
    print(f"Position created: {test}")
    result = math.sqrt((test[0] - 0)**2 + (test[1] - 0)**2 + (test[2] - 0)**2)
    print(f"Distance between (0, 0, 0) and {test}: {result:.2f}")
    print("Demo completed succesfully...\n")

if  len(sys.argv) > 1:
    try:
        demo()
        print(f"Parsing coordinates: \"{sys.argv[1]}\"")
        coords = parse_cords(sys.argv[1])
        print(f"Parsed position: {coords}")
        result = math.sqrt((coords[0] - 0)**2 + (coords[1] - 0)**2 + (coords[2] - 0)**2)
        print(f"Distance between (0, 0, 0) and {coords}: {result:.2f}")
        print("\nUnpacking demonstration:\n"
              f"Player at x={coords[0]}, y={coords[1]}, z={coords[2]}\n"
              f"Coordinates: X={coords[0]}, Y={coords[1]}, Z={coords[2]}")
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: ValueError, Args: {error}")
else:
    print("no arguments provided, quitting...")
