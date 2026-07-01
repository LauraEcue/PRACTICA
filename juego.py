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


        if self.__vida <= 0:
            self.__vida = 0
            print (f"{self.nombre} caido en combate")

        else:
            print (f"{self.nombre} esquivó")


    def Atacar(self):
        print(f"{self.nombre} realiza ataque")

    def Esta_vivo(self):
        return self.__vida > 0

    def Get__vida(self):
        return self.__vida


#otra clase con herencia

class Guerro(Personaje):
    def __init__(self, nombre, vida, nivel, fuerza):
        super().__init__ (self, nombre, vida, nivel)
        self.fuerza = fuerza

    def Atacar(self):
        daño = self.nivel + self.fuerza
        return daño
    print(f"")

    

class Mago(Personaje):
    def __init__(self, nombre, vida, nivel, fuerza, maná):
        super().__init__(self, nombre, nivel, fuerza)
        self.maná = maná



        

