from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = '#375362'


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_display = Label(self.window, text="Score: 0", bg=THEME_COLOR, fg='white')
        self.score_display.grid(row=0, column=1)

        self.canvas = Canvas(self.window, width=300, height=250, bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125, width=280,
                                                   text='something here\nmulti line filler\nfor a better idea',
                                                   font=('Arial', 20, 'italic'), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_button_image = PhotoImage(file='images/true.png')
        false_button_image = PhotoImage(file='images/false.png')

        self.true_button = Button(image=true_button_image, highlightthickness=0, command=self.check_answer_is_true)
        self.true_button.grid(row=2, column=0, )

        self.false_button = Button(image=false_button_image, highlightthickness=0, command=self.check_answer_is_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_display.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text=f"You got {self.quiz.score} out of {len(self.quiz.question_list)}")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def check_answer_is_true(self) -> bool:
        is_correct = self.quiz.check_answer("True")
        self.feedback(is_correct)

    def check_answer_is_false(self) -> bool:
        is_correct = self.quiz.check_answer("False")
        self.feedback(is_correct)

    def feedback(self, is_correct: bool):
        if is_correct:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(2000, self.get_next_question)
