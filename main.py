import pandas

data = pandas.read_csv("weather_data.csv")
print("1\n")

print(data)

print("2\n")

print(type(data))
print(type(data["temp"]))

print("3\n")
data_dict = data.to_dict()
print(data_dict)

print("4\n")
data_list = data.temp.to_list()
print(data_list)
print("5\n")
# get the average temp
print(data.temp.mean())
# or
print(sum(data_list) / len(data_list))
# get the max
print("max")
print(data.temp.max())

# print a column btw its
print(data.day)
print("or")
print(data["day"])

# get data in row
print(data[data.day == "Monday"])
# or
print(data[data["day"] == "Monday"])
# get row with max temp
print(data[data.temp == data.temp.max()])
# get mondays data
monday = data[data.day == "Monday"]
print(monday.condition)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 51, 65]
    }
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")