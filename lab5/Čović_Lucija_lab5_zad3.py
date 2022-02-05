import io
import numpy as np
import csv

with open("distance.csv") as fle:
    first=True
    gradovi = []
    stablo = []
    udaljenosti = {}
    obidjeni = []
    ukupna_udaljenost = 0

    for line in fle:
        if(first):
            gradovi = list(line.split(","))
            gradovi.pop(0)
            first = False
        else:
            first1 = True
            grad = None
            grad_udaljenosti = []
            n = 0
            for udaljenost in line.split(","):
                if(first1):
                    grad = udaljenost
                    first1 = False
                elif("-" in udaljenost):
                    n+=1
                    continue
                else:
                    if((gradovi[n].replace("\n",""),grad.replace("\n","")) in udaljenosti):
                        n+=1
                        continue
                    else:
                        udaljenosti[(grad.replace("\n",""),gradovi[n].replace("\n",""))] = int(udaljenost)
                        n+=1
    
    print("Obidjeni putevi:\n")
    while(len(udaljenosti)>0):
        ky = min(udaljenosti.items(), key = lambda x: x[1])
        key = ky[0]
        val = udaljenosti.pop(key)
        #ako u presjeku obidjenih vrhova nadjemo jedan od 2 vrha, tada imamo petlju i taj brid ne koristimo
        presjek = np.intersect1d(np.array(obidjeni),np.array(key))
        #ako su oba grada u skupini obidjenih, imamo petlju
        if(len(presjek)>1):
            continue
        else:
            if(key[0] not in obidjeni):
                obidjeni.append(key[0])
            if(key[1] not in obidjeni):
                obidjeni.append(key[1])
            ukupna_udaljenost+=val
            print(key[0]," - ",key[1],":",val)
    
    print("\nUkupna udaljenost:",ukupna_udaljenost)