class Ropa:
    def __init__(self, marca, talla):
        self.marca = marca
        self.talla = talla

    def describir(self):
        return f"yo tengo una camisa de {self.marca}, mi talla es {self. talla}."


#probar
ropita = Ropa("clemont", "S")
print(ropita.describir())


    

    

