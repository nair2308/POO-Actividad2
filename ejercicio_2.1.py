class Persona:
    def __init__(self, nombre, apellidos, numero_documento_identidad, ano_nacimiento):
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento_identidad = numero_documento_identidad
        self.ano_nacimiento = ano_nacimiento

    def imprimir(self):
        print("Nombre =", self.nombre)
        print("Apellidos =", self.apellidos)
        print("Número de documento de identidad =", self.numero_documento_identidad)
        print("Año de nacimiento =", self.ano_nacimiento)
        print()

if __name__ == "__main__":
    p1 = Persona("Pedro", "Pérez", "1053121010", 1998)
    p2 = Persona("Luis", "León", "1053223344", 2001)
    p1.imprimir()
    p2.imprimir()