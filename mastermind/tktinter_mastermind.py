from tkinter import Label,Tk

root = Tk()

# # La fenêtre créée par défaut avec le code précédent est étirable. 
# # Nous pouvons figer ses dimensions à l’aide de la méthode resizable
# root.resizable(False, False)

root.title("Matsermind")

Label(root, text='Hello World').pack()

# une boucle infinie servant à capter les signaux émis par les actions de l’utilisateur. 
# On la placera généralement à la toute fin du programme.
root.mainloop()