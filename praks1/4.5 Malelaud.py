from tkinter import *
raam = Tk()
raam.title("Malelaud")
tahvel = Canvas(raam, width=800, height=800)
y0 = 0
y1 = 100

rida = 1
while rida <=8:
    x0 = 0
    x1 = 100
    if rida % 2 == 1:
        värv1 = "black"
        värv2 = "lightyellow"
    else:
        värv2 = "black"
        värv1 = "lightyellow"
    veerg = 1
    while veerg <= 8:
        if veerg % 2 == 1:
            tahvel.create_rectangle(x0,y0,x1,y1, fill=värv1)
        else:
            tahvel.create_rectangle(x0,y0,x1,y1, fill=värv2)
        x0 = x0 + 100
        x1 = x1 + 100
        veerg += 1
    y0 = y0 + 100
    y1 = y1 + 100
    rida += 1
tahvel.pack()
raam.mainloop()