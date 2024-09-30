#Escriba un programa en Python para construir el siguiente patrón.
for i in range(1,6):
    print("*"*i)
for i in range(1,6):   
    espacios= i-6
    print( espacios*" "+ "*"*i)