found = False
print ("antes", found)
for valor in [4,41,12,3,74,15] :
    if valor == 3 :
        found =  True
    print(found, valor)
    if found == True :
        break
print("despues", found)
