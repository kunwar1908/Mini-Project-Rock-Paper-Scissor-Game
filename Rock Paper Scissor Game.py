import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    display_choices(user_choice, computer_choice)
    messagebox.showinfo("Result", f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}")

def display_choices(user_choice, computer_choice):
    user_image = images[user_choice]
    computer_image = images[computer_choice]
    user_label.config(image=user_image) # type: ignore
    computer_label.config(image=computer_image) # type: ignore

def create_gui():
    global user_label, computer_label, images

    window = tk.Tk()
    window.title("Rock Paper Scissors Game")

    images = {
        "rock": ImageTk.PhotoImage(Image.open("Mini Projects/rock.png")),
        "paper": ImageTk.PhotoImage(Image.open("Mini Projects/paper.png")),
        "scissors": ImageTk.PhotoImage(Image.open("Mini Projects/scissors.png"))
    }

    user_label = tk.Label(window)
    user_label.pack(side="left", padx=20)

    computer_label = tk.Label(window)
    computer_label.pack(side="right", padx=20)

    def on_button_click(choice):
        play_game(choice)

    rock_button = tk.Button(window, text="Rock", command=lambda: on_button_click("rock"))
    rock_button.pack()

    paper_button = tk.Button(window, text="Paper", command=lambda: on_button_click("paper"))
    paper_button.pack()

    scissors_button = tk.Button(window, text="Scissors", command=lambda: on_button_click("scissors"))
    scissors_button.pack()

    window.mainloop()

if __name__ == "__main__":
    create_gui()