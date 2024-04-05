class Asignatura:
    def __init__(self, nombre, creditos, curso):
        self.creditos = creditos
        self.nombre = nombre
        self.profesores = set()
        self.curso = curso

    def __str__(self):
        p = ' '
        for prof in self.profesores:
            p += prof.obtener_nombre() + ' '   
        return self.nombre + ', Creditos: ' + self.creditos + ', Curso: ' + self.curso + ', Profesores: ' + p

    def obtener_nombre(self):
        return self.nombre

    def obtener_profesores(self):
        p = 'La asignatura ' + self.obtener_nombre() + ' la imparten: '
        for profesor in self.profesores:
           p += profesor.obtener_nombre() + ' '
        return p
    
    def _añadir_profesor(self, new_prof):
        """Este método es protegido porque será la universidad la que asigne profesores a la asignatura"""
        self.profesores.add(new_prof)
    
    def _eliminar_profesor(self, old_prof):
        """Este método es protegido porque será la universidad la que elimine profesores a la asignatura"""

        if old_prof not in self.profesores:
            raise ValueError(f"El profesor {old_prof.obtener_nombre()} no imparte la asignatura {self.obtener_nombre()}")
        
        self.profesores.remove(old_prof)


        