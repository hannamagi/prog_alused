from tkinter import *
raam = Tk()
raam.title("Lipp")
tahvel = Canvas(raam, width=400, height = 300)

tahvel.create_rectangle(350,100,100,50, fill="blue")
tahvel.create_rectangle(350,100,100,150, fill="black")
tahvel.create_rectangle(350,150,100,200, fill="yellow")
tahvel.pack()
raam.mainloop()