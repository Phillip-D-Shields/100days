import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Function to generate a random password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 16))]
    password_numbers = [choice(numbers) for _ in range(randint(6, 14))]
    password_symbols = [choice(symbols) for _ in range(randint(4, 8))]

    password_list = password_letters + password_numbers + password_symbols
    # print(password_list)
    shuffle(password_list)
    # print(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy("".join(password))


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    # print("add password clicked")
    website_entered = website_input.get()
    email_username_entered = email_username_input.get()
    password_entered = password_input.get()

    if len(website_entered) == 0 or len(email_username_entered) == 0 or len(password_entered) == 0:
        messagebox.showerror("Error", "Please fill in all fields")
    else:
        is_ok = messagebox.askokcancel(title=website_entered,
                                       message=f"Username: {email_username_entered}\nPassword: {password_entered}\nis this ok to save?")

        if is_ok:
            with open('passwords.txt', 'a') as file:
                file.write(website_entered + ' | ' + email_username_entered + ' | ' + password_entered + '\n')
            website_input.delete(0, 'end')
            password_input.delete(0, 'end')
            # print("Password added")
            messagebox.showinfo("Password Generated", "great success")


# ---------------------------- UI SETUP ------------------------------- #
# window
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas
logo_canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
logo_canvas.create_image(100, 100, image=logo_img)
logo_canvas.grid(row=0, column=1)

# website label
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)

# website input
website_input = tk.Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="ew")
website_input.focus()

# email or username label
email_username_label = tk.Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

# email or username input
email_username_input = tk.Entry(width=35)
email_username_input.grid(row=2, column=1, columnspan=2, sticky="ew")
email_username_input.insert(0, "matua.phillip.shields@gmail.com")

# password label
password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

# password input
password_input = tk.Entry(width=21)
password_input.grid(row=3, column=1, sticky="ew")

# generate password button
generate_password_button = tk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

# add password button
add_password_button = tk.Button(text="Add Password", width=36, command=add_password)
add_password_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
