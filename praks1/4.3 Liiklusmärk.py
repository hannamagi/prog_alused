from tkinter import *
raam = Tk()
raam.title("Liiklusmärk")
tahvel = Canvas(raam, width=200, height=200)

tahvel.create_oval(10,10,200,200, fill="red")
tahvel.create_rectangle(20,120,190,90, fill="white")
tahvel.pack()
raam.mainloop()