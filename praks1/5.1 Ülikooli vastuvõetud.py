fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
    vastuvõetud.append(int(rida))
fail.close()

print(vastuvõetud)
aasta = int(input("Palun sisestage, millise aasta andmeid vajate (2011-2019): "))
print(str(aasta) + " aastal oli vastuvõetuid " + str(vastuvõetud[aasta-2011]))
