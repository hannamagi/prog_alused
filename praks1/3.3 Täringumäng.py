from random import randint

täringute_arv = int(input("Täringute arv: "))
kord = 0
while kord < täringute_arv:
   suvaline = randint(1, 6)
   kord = kord + 1
   print(suvaline) 