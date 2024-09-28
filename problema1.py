#Encontrar los numeros divisibles por 7 y multiplos de 5 en el rango de 1500 a 2700 (ambos incluidos)

def numeros_divisibles_multiplos(limite_inferior,limite_superior):
    if limite_superior> limite_inferior:

        resultado=[]

        for n in range (limite_inferior,limite_superior+1):
            if n % 7 == 0 and n % 5 == 0:
                resultado.append(n)
        return resultado        


    raise ValueError("El limite inferior debe ser menor al limite superior.")

numeros = numeros_divisibles_multiplos(1500,2700)
print(numeros)
