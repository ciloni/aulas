lista = [
            19,
            25,
            23,
            1    
        ]

for i in range(0,len(lista),1):
    print("Elemento "+str(i)+" da lista é "+str(lista[i]))

# Procure métodos de ordenação e aplique o método de ordenação bubble sort para ordenar essa lista
# 19 25 23 1 
# 19 23 1 25
# 19 1 23 25
# 1 19 23 25

for j in range(0,len(lista),1):
    for i in range(0,len(lista)-1,1):
        if(lista[i]>lista[i+1]):
            variavel_intermediaria = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = variavel_intermediaria
            
print(lista)


