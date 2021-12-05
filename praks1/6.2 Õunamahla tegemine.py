def mahlapakkide_arv(õunte_kogus):
    mahlapakkide_arv = round(õunte_kogus*0.4/3)
    return mahlapakkide_arv
õunte_kogus = float(input("Mitu kologrammi õunu on? "))
print(mahlapakkide_arv(õunte_kogus))
