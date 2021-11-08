from random import randint

pöialpoisside_arv = int(input("Mitu pöialpoissi tahab õunu? "))
kord = 0
õunad = 14
while kord < pöialpoisside_arv:
    kord = kord + 1
    suvaline = randint(1, 2)
    print(suvaline)
    õunad = õunad - suvaline
print("Lumivalgekesele jäi " + str(õunad))