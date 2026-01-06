def ft_water_reminder():
    value = int(input("Days since last watering: "))
    if (value > 2):
        print("Water the plants!")
    else:
        print("plants are fine")
