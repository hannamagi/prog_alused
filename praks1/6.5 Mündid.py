def pronksikarva_summa(täisarvud):
    summa = 0
    for münt in täisarvud:
        if int(münt) <= 5:
            summa += int(münt)
    return summa
    
failinimi = input("Sisestage failinimi (mündid.txt): ")
fail = open( failinimi, encoding="UTF-8")
print("Hoiupõrsasse läheb " + str(pronksikarva_summa(fail)) + " senti.")
