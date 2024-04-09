from tkinter import *

def registreerimine(var):
    f=var.get()
    if f:
        texbox.configure(show="")
        valik.configure(image=pilt1)

    else:
        texbox.configure(show="*")
        valik.configure(image=pilt2)
def textpealkirjasse():
    t=texbox.get()
    pealkiri.configure(text=t)
    texbox.delete(0,END)
aken=Tk()
aken.geometry("500x500")
aken.title("Akna pealkiri")
aken.configure(bg="#00FFFF")
aken.iconbitmap("icon.ico")
pealkiri=Label(aken,
               text="Põhielemendid",
               bg="#00FFFF",
               fg="#18420d",
               cursor="star",
               font="Britannic_Bold 16",
               justify=CENTER,
               height=3,width=26)
raam=Frame(aken)
texbox=Entry(raam,
             bg="#00FFFF",
             fg="#9edb8f",
             font="Britannic_Bold 16",
             width=16,
             show="*")
pilt1=PhotoImage(file="eye.png")
pilt2=PhotoImage(file="close.png")
var=BooleanVar() #IntVar(), StringVar()
valik=Checkbutton(raam,
                  image=pilt1, #text="Punkt1"
                  variable=var,
                  onvalue=True,
                  offvalue=False,
                  command=lambda:registreerimine(var))
#valik.deselect()
nupp=Button(raam,
            text="Vajuta mind",
            bg="#00FFFF",
            fg="white",
            font="Britannic_Bold 16",
            width=16,
            command=textpealkirjasse)

pealkiri.pack()
raam.pack()
texbox.grid(row=0, column=0)
valik.grid(row=0, column=1)
nupp.grid(row=0,column=2)
aken.mainloop()
