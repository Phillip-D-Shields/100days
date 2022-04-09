# from turtle import Turtle, Screen
#
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
print(table)

table.field_names = ["pokemon name", "type"]
table.add_rows(
    [
        ["pikachu", "electric"],
        ["charmander", "fire"],
        ["squirtle", "water"],
    ]
)

print(table)

table.align = "l"
table.align["pokemon name"] = "r"
print(table)
