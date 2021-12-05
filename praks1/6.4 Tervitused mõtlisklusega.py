def tervitus(järjekord):
    print("""Võõrustaja: "Tere!" """)
    print("Täna" + str(järjekord) + ". kord tervitab, mõtliskleb võõrustaja")
    print("""Külaline: "Tere, suur tänu kutse eests" """)
järjekord = int(input("Sisestage külaliste arv: "))
for i in range(1 , järjekord + 1):
    tervitus(i)