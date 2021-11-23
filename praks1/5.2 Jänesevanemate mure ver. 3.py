ringide_arv = int(input("Sisesta ringide arv: "))
porgandid = 0
ringide_arv += 1
for i in range(2,ringide_arv,2):
    porgandid += i
print(str(porgandid))