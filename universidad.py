from departamento import EDepartamento
from estudiante import Estudiante
from profesor import Asociado, Titular, Profesor
from asignatura import Asignatura
from investigador import Investigador


class Universidad:

    def __init__(self):
        self.profesores = set()
        self.alumnos = set()
        self.investigadores = set()

    def __str__(self):
        txt = "UNIVERSIDAD: \n"
        txt += "-- Profesores --\n"
        for profesor in self.profesores:
            txt += str(profesor) + "\n"
            
        txt += "** Investigadores **\n"
        for inv in self.investigadores:
            txt += str(inv) + "\n"

        txt += "$$ Alumnos $$\n"
        for alumno in self.alumnos:
            txt += str(alumno) + "\n"

        return txt

    def contratar_profesor_titular(self, nombre, dni, direccion, sexo, departamento:EDepartamento, area):
        """La universidad se encarga de contratar al profesor, por lo tanto, reciben una persona, el departamento y el area."""

        if not isinstance(departamento, EDepartamento):
            raise TypeError("El argumento 'departamento' debe ser una instancia de la clase EDepartamento")
        
        profesor = Titular(nombre, dni, direccion, sexo, departamento, area)
        self.profesores.add(profesor)
        return profesor

    def contratar_profesor_asociado(self, nombre, dni, direccion, sexo, departamento:EDepartamento):
        """La universidad se encarga de contratar al profesor, por lo tanto, reciben una persona y el departamento."""       
        
        if not isinstance(departamento, EDepartamento):
            raise TypeError("El argumento 'departamento' debe ser una instancia de la clase EDepartamento")
        
        profesor = Asociado(nombre, dni, direccion, sexo, departamento)
        self.profesores.add(profesor)
        return profesor
    
    def contratar_investigador(self, nombre, dni, direccion, sexo, area, departamento:EDepartamento):
        """La universidad se encarga de contratar al investigador, por lo tanto, reciben una persona, 
        el área de investigación y el departamento."""

        if not isinstance(departamento, EDepartamento):
            raise TypeError("El argumento 'departamento' debe ser una instancia de la clase EDepartamento")
        
        investigador = Investigador(nombre, dni, direccion, sexo, area, departamento)
        self.investigadores.add(investigador)
        return investigador

    def inscribir_alumno(self, nombre, dni, direccion, sexo):
        """La universidad se encarga de inscribir al alumno, por lo tanto, reciben únicamente una persona."""

        alumno = Estudiante(nombre, dni, direccion, sexo)
        self.alumnos.add(alumno)
        return alumno
    
    def crear_asignatura(self, nombre, creditos, curso):
        """La universidad se encarga de crear las asignaturas, decidiendo su nombre, curso y créditos."""
        asignatura = Asignatura(nombre, creditos, curso)
        return asignatura
    
    def asignar_asignatura_profesor(self, asignatura:Asignatura, profesor:Profesor):
        """Este método es mediante el cual la universidad, asigna profesores a asignaturas y viceversa. 
        Desde aquí se accede a las clases profesor y asignatura para modificar sus datos."""
        if not isinstance(asignatura, Asignatura):
            raise TypeError("El argumento 'asignatura' debe ser una instancia de la clase Asignatura")
        if not isinstance(profesor, Profesor):
            raise TypeError("El argumento 'profesor' debe ser una instancia de la clase Profesor")

        asignatura._añadir_profesor(profesor)
        profesor._añadir_asignatura(asignatura)

    def eliminar_profesor_asignatura(self, asignatura:Asignatura, profesor:Profesor):
        """Este método es mediante el cual la universidad elimina profesores de asignaturas y viceversa. 
        Desde aquí se accede a las clases profesor y asignatura para modificar sus datos."""
        if not isinstance(asignatura, Asignatura):
            raise TypeError("El argumento 'asignatura' debe ser una instancia de la clase Asignatura")
        if not isinstance(profesor, Profesor):
            raise TypeError("El argumento 'profesor' debe ser una instancia de la clase Profesor")

        asignatura._eliminar_profesor(profesor)
        profesor._eliminar_asignatura(asignatura)

    def eliminar_profesor(self, profesor:Profesor):

        if not isinstance(profesor, Profesor):
            raise TypeError("El argumento 'profesor' debe ser una instancia de la clase Profesor")
        
        self.profesores.remove(profesor)

    def eliminar_alumno(self, alumno:Estudiante):

        if not isinstance(alumno, Estudiante):
            raise TypeError("El argumento 'alumno' debe ser una instancia de la clase Estudiante")
        
        self.alumnos.remove(alumno)
            
    
    def eliminar_investigador(self, investigador:Investigador):

        if not isinstance(investigador, Investigador):
            raise TypeError("El argumento 'investigador' debe ser una instancia de la clase Investigador")
        
        self.investigadores.remove(investigador)