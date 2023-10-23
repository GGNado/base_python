import tkinter as frame
def uaglio():
	print(testo.get())

window = frame.Tk()
window.geometry("600x600")
window.title("Gui")
window.resizable(False, False)
window.configure(background="green", cursor="pirate")

primoBottone = frame.Button(text="Premimi", command=uaglio)
primoBottone.grid(row=2, column=2)
primoBottone.configure(foreground="black")

testo = frame.Entry()
testo.grid(row=0, column=2, sticky="W", pady="100")
testo.configure(background="red")
testo.configure()




if __name__ == "__main__":
	window.mainloop()