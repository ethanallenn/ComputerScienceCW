temp_dict = {'January': 10, 'February': 12, 'March': 15, 'April': 20, 'May': 25, 'June': 30, 'July': 35, 'August': 32, 'September': 28, 'October': 22, 'November': 15, 'December': 12}

hottest_temp = -float('inf')
coldest_temp = float('inf')

for month, temp in temp_dict.items():
    if temp > hottest_temp:
        hottest_temp = temp
        hottest_month = month
    if temp < coldest_temp:
        coldest_temp = temp
        coldest_month = month

print(f"The hottest month is {hottest_month} with an average temperature of {hottest_temp} degrees.")
print(f"The coldest month is {coldest_month} with an average temperature of {coldest_temp} degrees.")
