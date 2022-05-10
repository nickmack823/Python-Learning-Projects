import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data.keys())
colors = data["Primary Fur Color"]
color_values = colors.to_dict().values()
colors_list = []
# Iterate through colors
for color in color_values:
    if color not in colors_list and isinstance(color, str):
        colors_list.append(color)

color_count = []
# Iterate through count for each color
for color in colors_list:
    color_count.append(len(data[data["Primary Fur Color"] == color]))

new_dict = {
    "Fur Color": colors_list,
    "Count": color_count
}
df = pandas.DataFrame(new_dict)
df.to_csv("squirrel_count.csv")


