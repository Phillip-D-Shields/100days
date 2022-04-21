from tkinter import *

def button_click():
    print("Button clicked")
    miles_entered = miles_input.get()
    converted_kn = float(miles_entered) * 1.60934
    converted_to_km_label.config(text=format(converted_kn, '.2f'))


window = Tk()
window.title("miles to kilometers")
window.minsize(width=150, height=75)

# miles entry
miles_input = Entry( width=10)
print(miles_input.get())
miles_input.grid(column=1, row=0)

# miles label
miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

# is_equal_to label
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

# converted_miles label
converted_to_km_label = Label(text="0")
converted_to_km_label.grid(column=1, row=1)

# km label
km_label = Label(text="km")
km_label.grid(column=2, row=1)

# button
main_button = Button(window, text="convert", command=button_click)
main_button.grid(column=1, row=2)




window.mainloop()