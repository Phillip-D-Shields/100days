import pandas as pd

data = pd.read_csv('squirrels.csv')

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
# print(gray_squirrels)
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrels, red_squirrels, black_squirrels)

new_data_dict = {
    'fur color': ['Gray', 'Cinnamon', 'Black'],
    'count': [gray_squirrels, red_squirrels, black_squirrels]
}

new_data_frame = pd.DataFrame(new_data_dict)
new_data_frame.to_csv('squirrels_by_color.csv')