import pytest
from departamento import EDepartamento
from estudiante import Estudiante
from asignatura import Asignatura
from investigador import Investigador
from universidad import Universidad

def test_eliminar_asignatura():
    u = Universidad()
    prof = u.contratar_profesor_titular("Pedro García", "212S", "Plaza de España", "V", EDepartamento.DIIC, "Señales")
    pcd = Asignatura("Programación CD", 6, 2)
    with pytest.raises(ValueError):
        u.eliminar_profesor_asignatura(pcd, prof) # eliminar una asignatura que no tiene el profesor

def test_añadir_asignatura():
    e = Estudiante("José Cano", "302Y", "San Ginés", "V")
    with pytest.raises(TypeError):
        e.añadir_asignatura('fp') # no es una instancia de la clase asignatura

def test_asignatura_aprobada():
    e = Estudiante("José Cano", "302Y", "San Ginés", "V")
    pcd = Asignatura("Programación CD", 6, 2)
    with pytest.raises(ValueError):
        e.asignatura_aprobada(pcd) # no se ha matriculado

def test_cambiar_departamento():
    inv = Investigador("José Cano", "302Y", "San Ginés", "V", "Aprendizaje Máquina", EDepartamento.DIIC)
    with pytest.raises(TypeError):
        inv.cambiar_departamento('I+D') == TypeError # no es instancia de la clase EDepartamento

def test_inscibir_alumno():
    u = Universidad()
    with pytest.raises(TypeError):
        u.inscribir_alumno('Paco') # no rellena todos los campos

def test_eliminar_profesor():
    u = Universidad()
    with pytest.raises(TypeError):
        u.eliminar_profesor('Fede') # no es una instancia de la clase Profesor

def test_contratar_profesor():
    u = Universidad()
    with pytest.raises(TypeError):
        u.contratar_profesor_titular("Pedro García", "212S", "Plaza de España", "V", 'EDepartamento.DIIC', "Señales") 
        # el departamento no es una instancia de la clase EDepartamento
