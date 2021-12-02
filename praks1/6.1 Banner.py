def banner(reklaamlause, arv):
    reklaamlause.upper()

arv = int(input("Mitu korda soovite reklaamlauset kuvada? "))
reklaamlause = input("Sisestage reklaamlause: ")
banner(reklaamlause, arv)
for i in range(0, arv):
    print(reklaamlause.upper())
