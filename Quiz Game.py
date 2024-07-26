import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = 0
        self.score = 0

        self.window = tk.Tk()
        self.window.title("Quiz Game")
        self.window.configure(bg="lightblue")

        self.question_label = tk.Label(self.window, text="", font=("Arial", 16), bg="lightblue", fg="darkblue")
        self.question_label.pack(pady=20)

        self.answer_var = tk.StringVar()
        self.answer_var.set("none")

        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(self.window, text="", variable=self.answer_var, value=str(i), font=("Arial", 14), bg="lightblue", fg="black", selectcolor="lightgreen")
            radio_button.pack(anchor="w", padx=20, pady=5)
            self.radio_buttons.append(radio_button)

        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit_answer, font=("Arial", 14), bg="darkblue", fg="white")
        self.submit_button.pack(pady=20)

        self.next_question()

    def next_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question["question"])

            for i, option in enumerate(question["options"]):
                self.radio_buttons[i].config(text=option)

            self.answer_var.set("none")
        else:
            messagebox.showinfo("Quiz Game", f"Quiz completed! Your score is {self.score}/{len(self.questions)}")
            self.window.destroy()

    def submit_answer(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            selected_option = self.answer_var.get()

            if selected_option == question["answer"]:
                self.score += 1

            self.current_question += 1
            self.next_question()

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Rome"],
        "answer": "1"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": "0"
    },
    {
        "question": "What is the largest ocean in the world?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "3"
    }
]

game = QuizGame(questions)
game.window.mainloop()