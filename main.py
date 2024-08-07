from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

language = pandas.read_csv("data/french_words.csv")
to_learn = language.to_dict(orient="records")
current_card = {}


# Get data
def change_word():
    global current_card, flip_timer
    canvas.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_word, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_word, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


# UI setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
title_word = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


# correct button
my_image = PhotoImage(file="images/right.png")
right_button = Button(image=my_image, highlightthickness=0, command=change_word)
right_button.grid(row=1, column=0)

# incorrect button
my_image_wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=my_image_wrong, highlightthickness=0, command=change_word)
wrong_button.config(bg=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=1)

change_word()
window.mainloop()

