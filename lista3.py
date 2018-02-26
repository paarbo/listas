limite=int(input("Introduce  cuantas palabrs quieres que tenga la lista: "))
lista=[]
if limite<1:
       print("no valido")
else:
       for n in range (limite):
           print ("Dime la palabra",n+1,":")
           palabra=input()
           lista+=[palabra]
print("La lista creada es:",lista)
pregunta=input("Dime la palabra que quieres substituir: ")
por=input("Por la palabra: ")
contar=lista.count(pregunta)
for i in range (contar):
    index=lista.index(pregunta)
    lista[index]=por
    
print("La lista creada es:",lista)
