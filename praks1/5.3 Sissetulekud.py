fail = open("konto.txt", encoding="UTF-8")
for tehingud in fail:
    if float(tehingud) > 0:
        print(tehingud[:-1])
        
fail.close()