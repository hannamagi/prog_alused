failinimi = str(input("Palun sisestahge failinimi (jukebox.txt, 80ndade.txt, eesti_muusika.txt, edm.txt): "))
fail = open(failinimi, encoding="UTF-8")
muusikapala = 1
print("Muusikapalade valik: ")
number = []
for rida in fail:
    print(str(muusikapala) + "." + str(rida[:-1]))
    muusikapala += 1
    number.append(rida)
mitmeslugu = int(input("Valige laulu järjekorranumber: "))
mitmeslugu -= 1
print("Mängitav muusikapala on " + number[mitmeslugu])
fail.close()