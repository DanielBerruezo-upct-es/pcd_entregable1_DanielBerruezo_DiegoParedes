class MiembroDepartamento:

    def __init__(self, puesto, departamento):
        self.puesto = puesto
        self.departamento = departamento

    def __str__(self):
        return str(self.departamento) + str(self.puesto)
    
    def obtener_dep(self):
        return str(self.departamento)

    def _cambio_departamento(self, new_dep):
        """Este método es protegido porque se hará desde la clase del miembro el cambio de departamento y tanto profesores como investigadores pueden acceder"""
        self.departamento = new_dep