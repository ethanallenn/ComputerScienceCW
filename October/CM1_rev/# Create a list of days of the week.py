days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperatures = {}
for day in days_of_week:
    temperature = float(input(f"Enter the temperature for {day}: "))
    temperatures[day] = temperature
warmest_day = max(temperatures, key=temperatures.get)
print(f"The warmest day is {warmest_day} with a temperature of {temperatures[warmest_day]} degrees.")