from departamento import EDepartamento
from persona import Persona
from miembo_departamento import MiembroDepartamento


class Profesor(Persona):

    def __init__(self, nombre, dni, direccion, sexo, departamento:EDepartamento): 
        """Al crear el profesor, guardamos sus datos personales, además habrá que pasarle el tipo de profesor y el departamento"""

        super().__init__(nombre, dni, direccion, sexo)
        self.asignaturas = set()
        self.dep = MiembroDepartamento(self, departamento)

    def __str__(self):
        name = self.obtener_nombre()
        dep = self.dep.obtener_dep()
        a = ''
        for asign in self.asignaturas:
            a += asign.obtener_nombre() + ' '    

        txt = name + ', ' + dep + ', ' + "Asignaturas: " + a

        return txt
    
    def cambiar_departamento(self, departamento:EDepartamento):

        if not isinstance(departamento, EDepartamento):
            raise TypeError("El argumento 'departamento' debe ser una instancia de la clase EDepartamento")
        
        self.dep._cambio_departamento(departamento)

    
    def obtener_asignaturas(self):
        a = 'El profesor ' + self.obtener_nombre() + ' imparte: '
        for asignatura in self.asignaturas:
           a += asignatura.obtener_nombre() + ' '
        return a
    
    def _añadir_asignatura(self, nueva_asignatura):
        """Este método es protegido porque será la universidad la que asigne asignaturas al profesor"""
        self.asignaturas.add(nueva_asignatura)

    def _eliminar_asignatura(self, asignatura):
        """Este método es protegido porque será la universidad la que elimine asignaturas al profesor"""
        if asignatura in self.asignaturas:
            self.asignaturas.remove(asignatura)
            

class Asociado(Profesor):
    
    def __init__(self, nombre, dni, direccion, sexo, departamento: EDepartamento):
        super().__init__(nombre, dni, direccion, sexo, departamento)  
    
class Titular(Profesor):
    
    def __init__(self, nombre, dni, direccion, sexo, departamento: EDepartamento, area):
        super().__init__(nombre, dni, direccion, sexo, departamento)    
        self.area = area

    def cambiar_area(self, area):     
            self.area = area