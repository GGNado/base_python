'''
def somma(a: int, b: int) -> int:
    return a+b
def scrivi():
    print("Scrivo")

a = []
for i in range(0,10):
    a.append(i*i)

print(a)
print(f"La somma dei numeri è: {somma(10,10)}")
scrivi()

lista = []
tupla = () #Elementi costanti
insiemi = {} #Lista che non puo contenere 2 volte lo stesso elemento
'''

class Persona:
	#Costruttore, self sempre = this
	def __init__(self, nome : str, cognome : str, anni: int):
		self.nome = nome
		self.cognome = cognome
		self.anni = anni

	#To string, self sempre
	def __str__(self):
		return f"Ciao sono {self.nome, self.cognome, self.anni}"

persona = Persona("Luigi", "Massa", 18)
print(persona)
print(persona.nome)

persone = [
	Persona("Francesco", "Lange", 17),
	Persona("Catello", "Dapice", 17),
	Persona("Fabio", "Russo", 17),
]

for p in persone:
	print(p)

persone2 = {
	"kekko": Persona("Francesco", "Lange", 17),
	"ciuraro": Persona("Catello", "Dapice", 17),
}

for chiave, pers in persone2.items():
	print(f"{chiave}: {pers}")