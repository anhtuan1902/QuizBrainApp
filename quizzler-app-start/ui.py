from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        #Create background
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, pady=20, padx=20)
        #Create score label
        self.label_score = Label(text=f"Score: {self.quiz.score}", font=("Arial", 10), fg="white",
                                 background=THEME_COLOR)
        self.label_score.grid(row=0, column=1, padx=20, pady=20)
        #Create question form
        self.canvas_font = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.canvas_text = self.canvas_font.create_text(150, 125, text="Question", font=("Ariel", 20, "italic"),
                                                        fill=THEME_COLOR, width=250)
        self.canvas_font.grid(row=1, column=0, columnspan=2, pady=50)
        #Create btn True
        self.img_true = PhotoImage(file="images/true.png")
        self.btn_true = Button(image=self.img_true, highlightthickness=0, command=self.btn_true_click)
        self.btn_true.grid(row=2, column=0, padx=20, pady=20)
        #Create btn False
        self.img_false = PhotoImage(file="images/false.png")
        self.btn_false = Button(image=self.img_false, highlightthickness=0, command=self.btn_false_click)
        self.btn_false.grid(row=2, column=1, padx=20, pady=20)
        #Update form

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas_font.configure(background="white")
        self.label_score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas_font.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas_font.itemconfig(self.canvas_text, text="You've completed the quiz\n"
                                                f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")

    def btn_true_click(self):
        """Function click btn true"""
        self.get_feedback(self.quiz.check_answer("True"))

    def btn_false_click(self):
        """Function click btn false"""
        self.get_feedback(self.quiz.check_answer("False"))

    def get_feedback(self, is_right: bool):
        if is_right:
            self.canvas_font.configure(background="green")
        else:
            self.canvas_font.configure(background="red")
        self.window.after(500, self.get_next_question)
