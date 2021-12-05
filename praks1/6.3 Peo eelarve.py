def eelarve(külalised):
    ruumirent = 55
    summa = külalised * 10 + ruumirent
    return summa
kutsutud = int(input("Mitu inimest on kutsutud? "))
tulemas = int(input("Mitu inimest on tulemas? "))
print("Maksimaalne eelarve: " + str(eelarve(kutsutud)) + " eurot")
print("Minimaalne eelarve: " + str(eelarve(tulemas)) + " eurot")
    