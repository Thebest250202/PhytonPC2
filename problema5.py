#Suma de todos los numero primos menores que 100
lista = int(input('¿Hasta qué número quieres la lista?: '))
listado_numeros = []
cont = 0
for i in range(2, lista + 1):
    primos = True
    for j in range(2,i):
        if i == j:
           break
        elif i%j == 0:
           primos = False
        else:
           continue
    if primos == True:
        print(' ',i, end='')
        cont += 1
        listado_numeros.append(i)

print('\nHay %u números primos.' % cont )

sum_num =  sum(listado_numeros)

print("La suma de los numeros es: ")
print(sum_num)