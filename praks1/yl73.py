from easygui import *
arv1 = enterbox("Sisestage esimene täisarv lõigus 1-10: ")
arv2 = enterbox("Sisestage teine täisarv lõigus 1-10: ")
märgid = ["+", "-", "*"]
märk = buttonbox("Valige tehe", choices = märgid)
if märk == "+":
    vastus = int(arv1) + int(arv2)
elif märk == "-":
    vastus = int(arv1) - int(arv2)
elif märk == "*":
    vastus = int(arv1) * int(arv2)
msgbox("Tehte tulemus on " + str(vastus) + ".")
