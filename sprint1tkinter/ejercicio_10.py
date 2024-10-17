import tkinter as tk


root = tk.Tk()
root.title("Ejercicio 10")
root.geometry("500x200")


# Frame que contenga texto y scrollbar
frame = tk.Frame(root)
frame.pack(fill = "both", expand = True) # both para expandir en ambos ejes, x e y, y true para ocupar cualquier espacio adicional


# Crear texto
text = tk.Text(frame)
text.grid(row = 0, column = 0, sticky = "nsew") # Con nsew se expande norte, sur, este y oeste
poem_text = """
Me gustas cuando callas porque estás como ausente,
y me oyes desde lejos, y mi voz no te toca.
Parece que los ojos se te hubieran volado
y parece que un beso te cerrara la boca.

Como todas las cosas están llenas de mi alma
emerges de las cosas, llena del alma mía.
Mariposa de sueño, te pareces a mi alma,
y te pareces a la palabra melancolía.

Me gustas cuando callas y estás como distante.
Y estás como quejándote, mariposa en arrullo.
Y me oyes desde lejos, y mi voz no te alcanza:
déjame que me calle con el silencio tuyo.

Déjame que te hable también con tu silencio
claro como una lámpara, simple como un anillo.
Eres como la noche, callada y constelada.
Tu silencio es de estrella, tan lejano y sencillo.

Me gustas cuando callas porque estás como ausente.
Distante y dolorosa como si hubieras muerto.
Una palabra entonces, una sonrisa bastan.
Y estoy alegre, alegre de que no sea cierto.
"""

text.insert(tk.END, poem_text)


# Crear scrollbar vertical
scrollbar = tk.Scrollbar(frame, orient = "vertical", command = text.yview)
scrollbar.grid(row = 0, column = 1, sticky = "ns") # ns para estirar verticalmente, norte y sur


# Conectar texto con scrollbar
text.config(yscrollcommand = scrollbar.set)


# Ajustar tamaño del frame y el text al tamaño de la ventana si esta varía
frame.grid_rowconfigure(0, weight = 1)
frame.grid_columnconfigure(0, weight = 1)


root.mainloop()