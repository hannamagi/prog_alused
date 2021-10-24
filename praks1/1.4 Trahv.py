nimi = input("Sisesta oma nimi: ")
lubatud_kiirus = int(input("Sisesta lubatud kiirus (km/h): "))
tegelik_kiirus = int(input("Sisesta tegelik kiirus (km/h): "))
uletatud_kiirus = tegelik_kiirus - lubatud_kiirus
trahv = uletatud_kiirus * 3
tegelik_trahv = min(190,trahv)
print(nimi + ", kiiruse ületamise eest on teie trahv " + str(tegelik_trahv) + " eurot")