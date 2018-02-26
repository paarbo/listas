num=int(input("Introduce el numero de palabras: "))


if num<1:
    print ("no valido")
else:
    lista=[]
    for n in range (num):
        print("Digame la palabra",n+1,":")
        palabra=input()
        lista+=[palabra]

pregunta=input("Introduce la palabra que quieres buscar: ")
contar=lista.count (palabra)
if contar==0:
    print("No se ha encontrado la palabra",pregunta,"en la lista")
if contar==1:
    print("La palabra",pregunta,"aparece en la lista",contar,"vez")
else:
    print("La palabra",pregunta,"aparece en la lista",contar,"veces")
