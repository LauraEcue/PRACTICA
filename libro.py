class libro:
    def __init__ (self, titulo, categoria, autor):
        self.titulo = titulo
        self.categoria = categoria
        self.autor = autor
        self.esta_prestado = False

    def prestar (self):
        if (not self.esta_prestado):
            self.esta_prestado = True

            return f"El libro {self.titulo} ha sido prestado"

        else
            return f""
