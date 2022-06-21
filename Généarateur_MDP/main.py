from random import sample
from json import load, dump
from time import sleep
from tkinter import Button, Entry, Frame, Label, Tk

minuscules = "abcdefghijklmnopqrstuvwxyz"
majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nombres = "0123456789"
symboles = "*-_@!#?"

utilisation = minuscules+majuscules+nombres+symboles
caractères = 8

motDePasse = "".join(sample(utilisation, caractères))

def change():
    motDePasse = "".join(sample(utilisation, int(nb_char.get())))
    mot["text"] = motDePasse
    app.update()
    return motDePasse

def afficher():
    def fermer():
        windows.destroy()
        app.update()
    fic = load(open("MotDePasses.json", "r"))
    windows = Frame(app, bg="deepskyblue")
    windows.grid(row=1, column=2)
    Button(windows, text="Fermer", bg="orange", command=fermer).grid()
    for mdp in fic:
        Label(windows, text=f"{mdp} : {fic[mdp]}", bg="deepskyblue").grid()


def copie():
    fic = load(open("MotDePasses.json", "r"))
    fic[Nom.get()] = mot['text']
    dump(fic, open("MotDePasses.json", "w"))
    while len(Nom.get()) > 0:
        Nom.delete(0)
    Copieur.clipboard_append(mot['text'])
    change()
    print("Copié dans le presse papier !")

app = Tk()

Button(app, text="Afficher les mots de passes", bg="orange", command=afficher).grid(pady=5)

Label(app, text="Nom :").grid(pady=5)

Nom = Entry(app)
Nom.grid()

Label(app, text="Nombre de caractères :").grid(pady=5)

nb_char = Entry(app)
nb_char.grid(pady=5)

mot = Label(app, text=motDePasse)
mot.grid(pady=5)

Button(app, text="Changer", command=change, bg="lightcoral").grid()
Copieur = Button(app, text="Copier", command=copie, bg="lime")
Copieur.grid()
app.mainloop()