#Escriba un programa en Python para construir el siguiente patrón.
for i in range(6):
    print("*"*i)
for i in range(6):   
    espacios= 6-i
    print(espacios*" "+"*"*i )