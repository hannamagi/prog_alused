täisarv = int(input("Sisestage täisarv: "))
i = 1
nisuterad = 0

while i <= täisarv:
    if i == 1:
        nisuterad = 1
    else:
        nisuterad = nisuterad * 2
    i = i + 1

    
print("Nisuteri " + str(täisarv) + ". ruudu eest: " + str(nisuterad))