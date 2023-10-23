def calcolo_stipendio(stipendio: float, percentuale: int):
	return stipendio + (stipendio * percentuale / 100)

#fila 1: esercizio 1. Stampare i successivi 3 numeri. esercizio 2: trovare gli errori nel codice

#es1

numero = int(input("Inserisci un numero >> "))
#numero = int(numero)
for x in range(1,4):
	print(numero+x)

print("---------------")

#fila 2: esercizio 1: stampare i successivi 2 numeri. esercizio 2: stampare lo stipendio del +5%, +10% e +20%

stipendio = float(input("Inserisci stipendio >> "))
primoStipendio = calcolo_stipendio(stipendio, 5)
secondoStipendio = calcolo_stipendio(stipendio, 10)
terzoStipendio = calcolo_stipendio(stipendio, 20)

print(f"Primo stipendio = {primoStipendio}\nSecondo Stipendio = {secondoStipendio}\nTerzo stipendio = {terzoStipendio}")





