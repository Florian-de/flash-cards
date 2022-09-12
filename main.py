from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
words = pandas.read_csv("data/french_words.csv").to_dict(orient="records")

current_card = {}

def change_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    n = random.randint(0, len(words))
    current_card = words[n]
    canvas.itemconfig(card_image, image=frontcard_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_image, image=backcard_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def delete_word():
    global words
    words.remove(current_card)
    data = pandas.DataFrame(words)
    data.to_csv("data/french_words.csv", index=False)
    change_word()



window = Tk()
window.title("Flash-Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer =  window.after(3000, flip_card)

wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")
backcard_image = PhotoImage(file="images/card_back.png")
frontcard_image = PhotoImage(file="images/card_front.png")

wrong_button = Button(image=wrong_image, highlightthickness=0, command=change_word)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_image, highlightthickness=0, command=delete_word)
right_button.grid(row=1, column=1)

canvas = Canvas(width=800, height=526)
card_image = canvas.create_image(410, 273, image=frontcard_image)
card_title = canvas.create_text(400, 150, text="Hello", font=("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="trouve", font=("Arial", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


change_word()






window.mainloop()


