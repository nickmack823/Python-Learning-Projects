
# Takes too much cleaning, use csv library instead
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if data.line_num != 1:
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# Entire table is pandas DataFrame, column is pandas Series
# print(type(data))
# print(data["temp"])

# # Converts DataFrame to dictionary
# data_dict = data.to_dict()
# print(data_dict)
#
# # Converts series to list
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # Avg y Max temperature from Series
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Pandas automatically creates attributes based on column headings
# print(data.condition)

# Get data in column by values (returns row)
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# Get value of row attribute
monday = data[data.day == "Monday"]
print(monday.condition)

# Create a DataFrame and CSV file from a dictionary
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")