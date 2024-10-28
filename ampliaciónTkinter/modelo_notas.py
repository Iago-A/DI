class Modelo:
    def __init__(self):
        # Lista de notas para la listbox
        self.notas = []


    def agregar_nota(self, nueva_nota):
        texto = nueva_nota
        self.notas.append(texto)


    def eliminar_nota(self, indice):
        for i in reversed(indice):
            self.notas.pop(i)


    def obtener_notas(self):
        return self.notas


    def guardar_notas(self):
        with open('notas.txt', 'w') as archivo:
            for nota in self.notas:
                archivo.write(nota + "\n")


    def cargar_notas(self):
        with open("notas.txt", "r") as archivo:
            for nota in archivo:
                self.notas.append(nota.strip())
