import sys
import math

def parse_cords(cords: str) -> tuple:
    try:
        s = cords.split(",")
        n = [int(e) for e in s]
        tp = tuple(n)
        print(f"parsed position: {tp}")
        print(f"Distance between (0, 0, 0) and {tp}: {calculate_distance((0, 0, 0), tp):.2f}")    
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: ValueError, Args: {error}")

def calculate_distance(pos1: tuple, pos2: tuple) -> int:
    x1, y1, z1, = pos1
    x2, y2, z2 = pos2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


print("=== Game Coordinate System ===\n")
sample = (10, 20, 5)
if len(sys.argv) == 1:
    print("no Coordinates provided, usage: python3 ft_coordinate_system.py \"x,y,z\"")
else:
    print(f"Position created: {sample}")
    print(f"Distance between (0, 0, 0) and {sample}: {calculate_distance((0, 0, 0), sample):.2f}")
    print(f"Parsing coordinates: {sys.argv[1]}")
    parse_cords(sys.argv[1])
