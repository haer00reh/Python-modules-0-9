def ft_count_harvset_recursive():
    value = int(input("Days until harvest: "))

    def recurs(value):
        if value == 0:
            return
        recurs(value - 1)
        print(f"Day {value}")

    recurs(value)
    print("Harvest time!")
