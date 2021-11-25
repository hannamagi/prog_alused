fail = open("sisseranne.txt", encoding="UTF-8")
sisseränne = []
for rida in fail:
    sisseränne.append(rida)
fail.close()
fail = open("valjaranne.txt", encoding="UTF-8")
väljaränne = []
for rida in fail:
    väljaränne.append(rida)
fail.close()
rändesaldod = []
i = 0
while i < 10:
    rändesaldod.append(int(sisseränne[i]) - int(väljaränne[i]))
    i += 1
print(rändesaldod)
if max(rändesaldod) > 0 :
    print("Suurim positiivne rändesaldo oli 10.aastal.")
else:
    print("Positiivse rändesaldoga aastaid ei ole.")