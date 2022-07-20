from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class Quizinterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quiz application')
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        # Label
        self.score = Label(text='Score: 0', background=THEME_COLOR, fg='white', font=('courier', 20, 'bold'))
        self.score.grid(row=0, column=1)

        # canvas
        self.canvas = Canvas(width=300, height=250, background='white')
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=290,
                                                     text='Question text',
                                                     font=('Arial', 20, 'italic'),
                                                     fill=THEME_COLOR
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2)

        # button
        true_image = PhotoImage(file='images/true.png')
        self.true_btn = Button(image=true_image, highlightthickness=0, command=self.anwser_true)
        self.true_btn.grid(row=2, column=0, pady=20)
        false_image = PhotoImage(file='images/false.png')
        self.false_btn = Button(image=false_image, highlightthickness=0, command=self.anwser_false)
        self.false_btn.grid(row=2, column=1)
        refresh_image = PhotoImage(file='images/refresh.png')
        self.refresh_btn = Button(image=refresh_image, highlightthickness=0, command=self.refresh, state=DISABLED)
        self.refresh_btn.grid(row=0, column=0)

        #  gets the first question
        self.get_question()

        self.window.mainloop()

    def anwser_true(self):
        q_anwser = 'True'
        self.give_feedback(self.quiz.check_answer(q_anwser))
        self.true_btn.config(state=DISABLED)

    def anwser_false(self):
        q_anwser = 'False'
        self.give_feedback(self.quiz.check_answer(q_anwser))
        self.false_btn.config(state=DISABLED)

    def get_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score:{self.quiz.score}')
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_question)
            self.true_btn.config(state=ACTIVE)
            self.false_btn.config(state=ACTIVE)
        else:
            self.canvas.itemconfig(self.question_text, text='Sorry, you have reached the end of the quiz!!!')
            self.true_btn.config(state=DISABLED)
            self.false_btn.config(state=DISABLED)
            self.refresh_btn.config(state=ACTIVE)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, func=self.next_question)

        # Get the questions again from the beginning

    def refresh(self):
        self.true_btn.config(state=ACTIVE)
        self.false_btn.config(state=ACTIVE)
        self.refresh_btn.config(state=DISABLED)
        self.quiz.reset()
        self.score.config(text=f'Score:{self.quiz.score}')
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
