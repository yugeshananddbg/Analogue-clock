from tkinter import *
from PIL import Image ,ImageTk,ImageDraw
from datetime import *
from math import *
import time

class Clock:
    def __init__(self,root):
        self.root=root
        self.root.title("GUI Analouge clock")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        title = Label(self.root, text="Analouge clock made by Yugesh", font=("times new roman", 50, "bold"), bg="#04444a", fg="white")
        title.place(x=0, y=50,relwidth=1)

        self.lbl=Label(self.root, bg="white" ,bd=20,relief=RAISED)
        self.lbl.place(x=450, y=150,width=400,height=400)
        # self.clock_image()
        self.working()


    def clock_image(self,hr,min_,sec_):
        clock= Image.new("RGB",(400,400),(255,255,255))
        draw=ImageDraw.Draw(clock)
        #clock image
        bg=Image.open("watch.png")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))

        # formula to rotate clock
        origin=200,200
        #clock Hour line
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="black" , width=3)
        clock.save("clock_new.png")
        # clock Minute line
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))), fill="blue", width=3)
        clock.save("clock_new.png")
        # clock second line
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))), fill="red", width=3)
        # ellipse
        draw.ellipse((195,195,210,210,),fill="black")


        clock.save("clock_new.png")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360

        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)


root=Tk()
obj=Clock(root)
root.mainloop()