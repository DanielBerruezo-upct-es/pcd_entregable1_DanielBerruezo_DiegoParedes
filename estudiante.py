from persona import Persona
from asignatura import Asignatura

class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo):
        super().__init__(nombre, dni, direccion, sexo)
        self.asignaturas = set()

    def __str__(self):
        a = ''
        for asign in self.asignaturas:
            a += asign.obtener_nombre() + ' '   
        return self.obtener_nombre() + ' Asignaturas: ' + a

    def obtener_asignaturas(self):
        a = ''
        for asign in self.asignaturas:
            a += asign.obtener_nombre() + ' ' 
        return a

    def añadir_asignatura(self, nueva_asignatura:Asignatura):
        """El estudiante escoge la asignatura a matricularse"""

        if not isinstance(nueva_asignatura, Asignatura):
            raise TypeError("El argumento 'nueva_asignatura' debe ser una instancia de la clase Asignatura")
        self.asignaturas.add(nueva_asignatura)

    def asignatura_aprobada(self, asignatura:Asignatura):

        if not isinstance(asignatura, Asignatura):
            raise TypeError("El argumento 'asignatura' debe ser una instancia de la clase Asignatura")
        if asignatura not in self.asignaturas:
            raise ValueError("El argumento 'asignatura' debe estar en la lista de asignaturas del estudiante")
        
        self.asignaturas.remove(asignatura)
