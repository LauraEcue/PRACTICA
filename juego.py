class Personaje:
    def __init__(self, nombre, vida, nivel):
        self.nombre = nombre
        self.__vida = vida
        self.nivel = nivel

    def Recibir_daño(self, cantidad):
        if cantidad > 0:
            self.__vida -= cantidad

        print(f"{self.nombre} recibio {self.cantidad} de daño. ")
        (f"vida restante:{self.__vida}")
        

