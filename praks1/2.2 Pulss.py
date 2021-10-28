vanus = int(input("Sisestage enda vanus: "))
sugu = input("Sisestage enda sugu: ").upper()
treening = int(input("Sisestage treeningu tüüp: "))
if (sugu == "M"):
    tervisetreening = 220 - vanus
if (sugu == "N"):
    tervisetreening = 206 - (vanus * 0.88)
    
if treening == 1:
    pulss_min = round(tervisetreening * 0.5)
    pulss_max = round(tervisetreening * 0.7)
if treening == 2:
    pulss_min = round(tervisetreening * 0.7)
    pulss_max = round(tervisetreening * 0.8)
if treening == 3:
    pulss_min = round(tervisetreening * 0.8)
    pulss_max = round(tervisetreening * 0.87)
    
print("Pulsisagedus peaks olema vahemikus " + str(pulss_min) + " kuni " + str(pulss_max) + ".")