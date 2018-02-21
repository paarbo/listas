limite=int(input("Introduce cuantas palabras tiene la lista: "))

if limite<1:
    print("no valido")
else:
    lista=[]
    for n in range(limite):
        print("Diga la palabra",n+1,":")
        palabra=input()
        lista+=[palabra]
    print("la lista creada es:",lista)
