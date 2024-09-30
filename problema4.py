class alumnos:
    def __init__(self,nom,notas):
        self.nom=nom
        self.notas=notas
i=0
lista = []
def mostrar():
    k=0
    while k<len(lista):
        print(lista[k].nom," ", lista[k].notas)
        k+=1
while i==0:
    print("Menu")
    print("1. Registrar alumno: " )
    print("2. Consultar listado: ")
    print("3. Salir ")
    opcion = int(input())
    if opcion==1:
        print("Registrar")
        n = input("Ingrese el nombre del alumno: ")
        t= input("Ingrese las notas del alumno: ")
        per = alumnos(n,t)
        lista.append(per)
        print("Guardado con exito")
    elif opcion==2:
        print("**Listado de alumnos**")
        mostrar
    elif opcion==3:
        exit() 
    else:
        print("Opción invalida")        