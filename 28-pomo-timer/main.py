import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25  # 25
SHORT_BREAK_MIN = 5  # 5
LONG_BREAK_MIN = 20  # 20
reps = 0
timer = None
chunk = '🍅'
chunks = []


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    global reps, chunks
    reps = 0
    chunks = []
    chunks_label.config(text=chunks)
    title.config(text="timer")
    canvas.itemconfig(timer_text, text="25:00")
    start_button.config(state="normal")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, chunks, chunk
    reps += 1

    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60

    start_button.config(state="disabled")

    if reps % 8 == 0:
        countdown(long_break_time)
        title.config(text="Break:20")
    elif reps % 2 == 0:
        countdown(short_break_time)
        title.config(text="Break:05")
    else:
        countdown(work_time)
        title.config(text="Work:25")
        chunks.append(chunk)
        chunks_label.config(text=chunks)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    # print(count)

    # format count into time
    minutes = math.floor(count / 60)
    if minutes < 10:
        minutes = f"0{minutes}"
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=GREEN)

# title label
title = tk.Label(text="timer", font=(FONT_NAME, 30), fg=RED, bg=GREEN)
title.grid(row=0, column=1)

# canvas
canvas = tk.Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill='white')
canvas.grid(row=1, column=1)

# start button
start_button = tk.Button(text='start', font=(FONT_NAME, 12, 'bold'), padx=10, pady=5, bg=YELLOW, fg=RED,
                         highlightthickness=0, relief='solid', borderwidth=1, command=start_timer)
start_button.grid(row=2, column=0)

# reset button
reset_button = tk.Button(text='reset', font=(FONT_NAME, 12, 'bold'), padx=10, pady=5, bg=YELLOW, fg=RED,
                         highlightthickness=0, relief='solid', borderwidth=1, command=reset)
reset_button.grid(row=2, column=2)

# completed chunks label
chunks_label = tk.Label(text=chunks, font=(FONT_NAME, 20, 'bold'), fg=RED, bg=GREEN)
chunks_label.grid(row=3, column=1)

window.mainloop()
