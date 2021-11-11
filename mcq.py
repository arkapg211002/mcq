from tkinter import *
from tkinter import messagebox as msg
import json
class Quiz:
    def __init__(self):
        self.q_no=0
        self.display_title()
        self.display_question()
        self.opt_selection=IntVar()
        self.opts=self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size=len(question)
        self.correct=0
    def display_result(self):
        wrong_count=self.data_size-self.correct
        correct=f"Correct:{self.correct}"
        wrong=f"Wrong:{wrong_count}"
        score=int(self.correct/self.data_size*100)
        result=f"Score:{score}%"
        msg.showinfo("Result",f"{result}\n{correct}\n{wrong}")
    def check(self,q_no):
        if self.opt_selection.get()==answer[q_no]:
            return True
    def nextbut(self):
        if self.check(self.q_no):
            self.correct+=1
        self.q_no+=1
        if self.q_no==self.data_size:
            self.display_result()
            gui.destroy()
        else:
            self.display_question()
            self.display_options()
    def buttons(self):
        next_button=Button(gui,text="NEXT",command=self.nextbut,width=10,bg="grey",fg="white",font="bookmanoldstyle 16 bold")
        next_button.place(x=350,y=380)
        quit_button=Button(gui,text="QUIT",command=gui.destroy,width=5,bg="grey",fg="white",font="bookmanoldstyle 16 bold")
        quit_button.place(x=700,y=50)
    def display_options(self):
        val=0
        self.opt_selection.set(0)
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1
    def display_question(self):
        q_no=Label(gui,text=question[self.q_no],width=60,font="comicsansms,16,bold",anchor='w')
        q_no.place(x=70,y=100)
    def display_title(self):
        title=Label(gui,text="QUIZ",width=50,bg="grey",fg="white",font="comicsansms 20 bold")
        title.place(x=0,y=2)
    def radio_buttons(self):
        q_list=[]
        y_pos=150
        while len(q_list)<4:
            radiobt=Radiobutton(gui,text=" ",variable=self.opt_selection,value=len(q_list)+1,font="comicsansms 14")
            q_list.append(radiobt)
            radiobt.place(x=100,y=y_pos)
            y_pos+=40
        return q_list
gui=Tk()
gui.geometry("800x450")
gui.title("QUIZ")
with open('data') as f:
    data=json.load(f)
question=(data['question'])
options=(data['options'])
answer=(data['answer'])
quiz=Quiz()
gui.mainloop()




