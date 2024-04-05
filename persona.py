class Persona:
    def __init__(self, nombre, dni, direccion, sexo):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo

    def obtener_nombre(self):
        return self.nombre
    
    def __str__(self) -> str:
        return "Nombre:" + self.nombre + "\nDNI:" + self.dni + "\ndireccion:" + self.direccion + "\nsexo:" + self.sexo
    
    def obtener_datos_personales(self):
        print(self)