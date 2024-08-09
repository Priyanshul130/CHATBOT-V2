# DEVELOPED BY <PRIYANSHUL SHARMA>
# WEb page piyanshul.is-a.dev
from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer



window= Tk()
window.title("Chatbot")
bubbles = [] 

canvas = Canvas(window, width=600, height=600,bg="sky blue")
canvas.grid(row=0,column=0,columnspan=3)

bot=ChatBot("")

trainer=ChatterBotCorpusTrainer(bot)

#trainer.train('chatterbot.corpus.english')


trainer.train(
    "chatterbot.corpus.english")
    #"chatterbot.corpus.english.history",
    #"chatterbot.corpus.english.literature")


class chatBubble:
    def __init__(self,master,user,message=""):
        
        if user==1:
            colour="SpringGreen2"
            x=50
            y=450
            col=1
        else:
            colour="coral"
            x=400
            y=450
            col=2

        self.master=master
     
        self.frame=Frame(master)
        
        lbl=Label(self.frame,text=message,bg=colour,wraplength=600,anchor=W)
        lbl.pack()
        self.window=self.master.create_window(x,y,anchor=SW,window=self.frame)

       
        self.master.create_polygon(self.draw_triangle(self.window),fill=colour)

    def draw_triangle(self,widget):
        x1,y1,x2,y2=self.master.bbox(widget)

        return x1, y2 - 15, x1 - 25, y2 + 10, x1, y2

def send_message(user,message):
    if bubbles:

        canvas.move(ALL,0,-50)
    a=chatBubble(canvas,user,message)   
    bubbles.append(a)

def send():
    message=entry.get()
    send_message(2,entry.get())
    entry.delete(0,END)
    reply=bot.get_response(message)
    send_message(1,str(reply).strip())
    


entry = Entry(window,width=50)
entry.grid(row=1,column=0,columnspan=2)
Button(window,text="Send",width=5,command=send).grid(row=1,column=2)
window.mainloop()
