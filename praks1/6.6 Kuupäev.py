def kuu_nimi(aasta_kuud):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    return kuud[int(aasta_kuud) - 1]
def kuupäev_sõnena(kuupäev):
    kuupäevad = kuupäev.split(".")
    kuupäev = kuupäevad[0] + ". " + kuu_nimi(kuupäevad[1]) + " " + kuupäevad[2] + ". a"
    return kuupäev

kuupäev = input("Sisesta kuupäev kujul DD.MM.YYYY: ")
print(str(kuupäev_sõnena(kuupäev)))