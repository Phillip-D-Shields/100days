from tkinter import *

import pandas
import pandas as pd
from random import choice

BACKGROUND_COLOR = '#B1DDC6'
to_learn = {}
current_card = {}

try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/chinese-hsk-1.csv')
    to_learn = original_data.to_dict(orient='records')

else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    print(f"{len(to_learn)} words to learn")
    card_canvas.itemconfig(card_bg, image=card_front_image)
    card_canvas.itemconfig(card_title, text="中文", fill="black")
    card_canvas.itemconfig(card_word, text=current_card["中文"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    card_canvas.itemconfig(card_bg, image=card_back_image)
    card_canvas.itemconfig(card_title, text="English", fill="white")
    card_canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    pandas.DataFrame(to_learn).to_csv('data/words_to_learn.csv', index=False)
    next_card()


window = Tk()
window.title("flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)


# canvas card display
card_canvas = Canvas(window, width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_bg = card_canvas.create_image(400, 263, image=card_front_image)
card_title = card_canvas.create_text(400, 150, text="title", font="Arial 40 italic")
card_word = card_canvas.create_text(400, 275, text="word", font="Arial 40 bold")
card_canvas.grid(row=0, column=0, columnspan=2)

# fail button
fail_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=fail_image, command=next_card, highlightthickness=0, border=0)
unknown_button.grid(row=1, column=0)

# pass button
pass_image = PhotoImage(file="images/right.png")
known_button = Button(image=pass_image, command=is_known, highlightthickness=0, border=0)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()