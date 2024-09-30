ent=int(input("Hasta que numero quieres la lista"))
lista_num = []
for i in range(2, ent):
    b=0
    for j in range(1, (i//2)+1):
        if((i%j)==0):
            b= b+j;
    if(b==i):
        print("perfecto")
else:
    print("no perfecto")