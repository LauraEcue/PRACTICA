class libro:
    def __init__ (self, titulo, categoria, autor):
        self.titulo = titulo
        self.categoria = categoria
        self.autor = autor
        self.prestado = False

    def prestar (self):
        if (not self.prestado):
            self.prestado = True

            return f"El libro {self.titulo} ha sido prestado"

        else:
            return f"El libro {self.titulo} no esta prestado"

    def devolver(self):
        self.prestado=False
        return f"el libro {self.titulo} ha sido devuelto"

    def esta_prestado(self):
        return not self.prestado


class Biblioteca:
    def __init__(self,nombre):
        self.nombre = nombre
        self.lista_libros = []

    def agregar_libro(self,nuevo_libro):
        self.lista_libros.append(nuevo_libro)
        print (f"{nuevo_libro.titulo}, Agregado a la biblioteca")

    def mostrar_libro(self):
        print(f"biblioteca: {self.nombre}")
        for libro in self.lista_libros: 
            print(f"titulo: {libro.titulo}")
            print(f"categoria: {libro.categoria}")
            print(f"autor: {libro.autor}")
            if libro.esta_prestado():
                print("estado prestado")
            else:
                print("estado disponible")

#Libros
L1 = libro("100 años de soledad", "aventura", "gabriel")
L2 = libro("anita", "Comedia", "nicoll")
L3 = libro("La melancolia de los feos", "misterio", "Mario mendoza")
L4 = libro("El padrino", "Misterio", "Mario mendoza")
L5 = libro("La odisea", "Epica", "Homero")


B1 = Biblioteca("Biblioteca unica central")

#Agregar libros
B1.agregar_libro(L1)
B1.agregar_libro(L2)
B1.agregar_libro(L3)
B1.agregar_libro(L4)
B1.agregar_libro(L5)

print(L1.prestar())
print(L2.prestar())
print(L1.devolver())
print(L3.esta_prestado())

print ("*****************")
#mostrar lista de libro
B1.mostrar_libro()


    
        