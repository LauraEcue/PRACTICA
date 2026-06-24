class Empleado:
    def __init__(self, nombre, salariobase):
        self.nombre = nombre
        self.salariobase = salariobase

    def calcular_salario(self):
        return self.salariobase


class Vendedor (Empleado):
    def __init__(self, nombre, salariobase, comisiones):
        super(). __init__(nombre, salariobase)
        self.comisiones = comisiones

    def calcular_salario(self):
        return self.salariobase + self.comisiones


class Desarrollador (Empleado):
    def __init__(self, nombre, salariobase, bono):
        super(). __init__(nombre, salariobase)
        self.bono = bono

    def calcular_salario(self):
        return self.salariobase + self.bono


#probar
Laura = Desarrollador("Laura", 180000, 50000)
print(f"salario de {Laura.nombre}:{Laura.calcular_salario()}")


    
