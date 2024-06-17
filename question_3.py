# Task1

temperatures = [72, 75, 78, 79, 80, 81, 82,
                83, 85, 86, 87, 88, 89, 90,
                91, 92, 93, 94, 95, 96, 97,
                98, 99, 100, 101, 102, 103,
                104, 105, 106]
print(temperatures[7:14])

# Task2

low_temps = [ele for ele in temperatures if ele < 100]

print(low_temps)


# Task3

temperatures.reverse()

print(temperatures[4:10])
