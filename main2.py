a = [i*i for i in range(10)] #Combinare for + lista
print(a)

b = [i*i for i in range(10) if i%2 == 0] #Combinare if + for + lista
print(b)

dizionario = {"a" : 1, "b": 2}
c = {chiave: valori for chiave, valori in dizionario.items()}
print(c)

lista = [i for i in range(10)]
print(lista[-1]) #prendere ultimo elemento
print(lista[3:7]) #parte da indice 3
print(lista[-1::-1]) #Parti dall'ultimo valore con step -1