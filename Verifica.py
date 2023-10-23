docenti = {
	"Chiave": "Valore",
	"Informatica": "Prota",
	"Italiano": "Ciaciona"
}
def aggiungi_prof(materia: str, insegnante: str):
	docenti[materia] = insegnante

def modifica_valore(materia: str):
	if materia in docenti:
		insegnate = input("Valore trovato, inserisci il nuovo professore >> ")
		docenti[materia] = insegnate


def stampa_successivo(valore: int):
	print(valore+1)
	print(valore+2)
	print(valore+3)

	for x in range(1, 4):
		print(valore+x)


def stampa_stipendio(stipendio: float):
	stipendioA = stipendio + (stipendio * 5 / 100)
	stipendioB = stipendio + (stipendio * 10 / 100)
	stipendioC = stipendio + (stipendio * 20 / 100)

	print(stipendioA, stipendioB, stipendioC)



def is_pari(valore: int):
	if valore % 2 == 0:
		print(f"{valore} = Pari")
	else:
		print(f"{valore} = Dispari")

if __name__ == "__main__":
	aggiungi_prof("a", "b")
	modifica_valore("a")

	for materia in docenti:
		#STAMPA IL VAlORE, ESISTE ANCHE UN'ALTRO METODO PIÙ DIFFICILE
		print(docenti[materia])

	for x in range(1, 101):
		is_pari(x)

	stampa_successivo(1)
	stampa_stipendio(100)

