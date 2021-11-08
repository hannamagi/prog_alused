ringid = int(input("Sisesta ringide arv: "))
i = 1
kokku = 0
porgandid = 0
while i <= ringid:
    porgandid = porgandid + i
    i = i + 1
    kokku = porgandid + kokku
print("Porgandite koguarv on " + str(kokku))