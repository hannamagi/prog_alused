from tkinter import *
raam = Tk()
raam.title("Maja")
tahvel = Canvas(raam, width=400, height=400)
tahvel.create_rectangle(70,380,340,180, fill="light yellow")
#tahvel.create_polygon(80,280,340,380, fill="light pink")
tahvel.create_rectangle(125,380,180,300, fill="light blue")
tahvel.create_rectangle(230,280,280,230, fill="white" )
tahvel.create_line(125,345,140,345, width=2)
tahvel.pack()
raam.mainloop()