# with open("weather_data.csv",) as data_file:
#     print(data_file.readlines())


# import csv
#
# with open("weather_data.csv",) as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             print(row)
#             temperatures.append(int(row[1]))
#
#
# print(temperatures)


import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(type(data))
# print(data)
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# avg_temp = data["temp"].mean()
# print(avg_temp)
#
# max_temp = data["temp"].max()
# print(max_temp)
#
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp_in_fahrenheit = (monday.temp * 9/5) + 32
# print(monday_temp_in_fahrenheit)

# create a dataframe with the data
data_dict = {
    "students": ["Rolf", "Charlie", "Anna", "Jen", "Marta", "Sam"],
    "grades": [70, 80, 90, 40, 50, 60]
}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")