menor = None
print("Antes")
for valor in [9,41,12,3,74,15] :
    if menor == None :
        menor = valor
    elif valor < menor :
        menor = valor
    print(menor, valor )
print ("el menor es: ", menor)
