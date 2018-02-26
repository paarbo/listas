limite=int(input("Introduce cuantas palabras quieres que tenga la lista: "))
lista=[]
if limite<1:
       print("no valido")
else:
       for n in range (limite):
           print ("Dime la palabra",n+1,":")
           palabra=input()
           lista+=[palabra]
print("La lista creada es:",lista)
pregunta=input("Dime la palabra que quieres eliminar: ")

contar=lista.count(pregunta)
for i in range (contar):
    index=lista.remove(pregunta)
    
    
print("La lista es ahora:",lista)
