from departamento import EDepartamento
from persona import Persona
from miembo_departamento import MiembroDepartamento

class Investigador(Persona):

    def __init__(self, nombre, dni, direccion, sexo, area, departamento):
        super().__init__(nombre, dni, direccion, sexo)
        self.area = area
        self.dep = MiembroDepartamento(self, departamento)

    def __str__(self):
        return self.obtener_nombre() + ', ' + str(self.area) + ', ' + self.dep.obtener_dep()

    def cambiar_departamento(self, departamento):

        if not isinstance(departamento, EDepartamento):
            raise TypeError("El argumento 'departamento' debe ser una instancia de la clase EDepartamento")
        self.dep._cambio_departamento(departamento)
