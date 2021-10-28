isekoht = input("Kas soovite istekohta ise valida (ise) või loosida (loos)? ")
if isekoht == "ise":
    soovitud_koht = input("Kas soovite istuda akna ääres (aken) või mitte (muu)? ")
    if soovitud_koht == "aken":
        print("Valisite ise. Aknakoht" )
    elif soovitud_koht == "muu":
        print("Valisite ise. Vahekigukoht")
        
if isekoht == "loos":
    from random import randint
    koht = randint(1, 3)
    if (koht >= 2):
        print("Istekoht loositi. Vahekäik")
    else:
        print("Istekoht loositi. Aknakoht")
        
    
    