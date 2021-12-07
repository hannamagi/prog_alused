from datetime import datetime
päevik = open("paevik.txt", "a", encoding="UTF-8")
kuupäev_kellaaeg = datetime.today()
kirje = input("Mida soovid kirjutada? ")


päevik.write(str(kuupäev_kellaaeg) + "\n")
päevik.write(kirje + "\n")
#päevik.close()
open("paevik.txt", "r", encoding="UTF-8")
