mayor = None
menor = None
while True:
    num = input("Ingrese un numero: ")
    if num == "Fin" :
        break
    else:
        try :
            num=float(num)
            if mayor is None :
                mayor = num
                menor = num
            elif mayor < num :
                mayor = num
            elif menor > num :
                menor = num
        except :
            print("Entrada invalida, si desea terminar escriba: Fin")
print("Maximo es", mayor)
print("Minimo es", menor)
