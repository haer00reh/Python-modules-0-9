def ft_plant_age():
    value = int(input("enter plant age in days: "))
    if (value > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
