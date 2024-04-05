from universidad import Universidad
from departamento import EDepartamento

# creamos la universidad
u = Universidad()

# contratar profesores
prof01 = u.contratar_profesor_titular("Pedro García", "212S", "Plaza de España", "V", EDepartamento.DIIC, "Señales")
prof02 = u.contratar_profesor_asociado("María Gómez", "988J", "Paseo Alfonso XIII", "M", EDepartamento.DIS)
prof03 = u.contratar_profesor_titular("María Rodríguez", "811V", "Alameda", "M", EDepartamento.DITEC, "Machine Learning")

print(prof01.obtener_datos_personales()) # devolvemos los datos del profesor

# contratar investigadores
inv01 = u.contratar_investigador("Juan Rodríguez", "255M", "Calle Mayor", "V", "Señales", EDepartamento.DIS)
inv02 = u.contratar_investigador("Antonio Martínez", "432Q", "Calle Roma", "V", "Machine Learning", EDepartamento.DITEC)

# añadir alumnos
alu01 = u.inscribir_alumno("Ángela Pérez", "793K", "Reina Victoria", "M")
alu02 = u.inscribir_alumno("José Cano", "302Y", "San Ginés", "V")
alu03 = u.inscribir_alumno("Rocío Cegarra", "965O", "Santa Ana", "M")

# crea asignaturas
pcd = u.crear_asignatura("Programación CD", 6, 2)
ml = u.crear_asignatura("Machine Learning", 6, 2)
sys = u.crear_asignatura("Señales y sistemas", 6, 2)
fc = u.crear_asignatura("Fundamentos computadores", 6, 1)
fp = u.crear_asignatura("Fundamentos programación", 6, 1)

# asignar profesores a asignaturas

u.asignar_asignatura_profesor(ml, prof01)
u.asignar_asignatura_profesor(ml, prof02)
u.asignar_asignatura_profesor(pcd, prof03)
u.asignar_asignatura_profesor(sys, prof02)
u.asignar_asignatura_profesor(sys, prof01)
u.asignar_asignatura_profesor(fc, prof02)
u.asignar_asignatura_profesor(fc, prof03)
u.asignar_asignatura_profesor(fp, prof01)

# cambian el área de investigación los titulares

prof01.cambiar_area("Algoritmos")
prof03.cambiar_area("Algoritmos secuenciales")

# matriculamos a los alumnos en las asignaturas

alu01.añadir_asignatura(ml)
alu01.añadir_asignatura(pcd)
alu01.añadir_asignatura(sys)
alu01.añadir_asignatura(fc)
alu01.añadir_asignatura(fp)

alu02.añadir_asignatura(ml)
alu02.añadir_asignatura(pcd)
alu02.añadir_asignatura(sys)
alu02.añadir_asignatura(fp)

alu03.añadir_asignatura(fp)
alu03.añadir_asignatura(sys)
alu03.añadir_asignatura(fc)

print(alu02.obtener_asignaturas())

# quitamos las aprobadas
alu01.asignatura_aprobada(fc)
alu01.asignatura_aprobada(fp)
alu02.asignatura_aprobada(sys)

try:
    alu02.asignatura_aprobada(fc) # intentamos una que no existe para observar que devuelve el error
except ValueError as e:
    print("ERROR: ", e)

try:
    alu03.asignatura_aprobada('sys')
except TypeError as e:
    print("ERROR: ", e) # intentamos una que no es una instancia para observar como devuelve el error

alu03.asignatura_aprobada(fc)

print(alu02.obtener_asignaturas()) # observamos que se han quitado las aprobadas

print(fc.obtener_profesores())
print(prof03.obtener_asignaturas())

# eliminamos a un profesor de una asignatura
u.eliminar_profesor_asignatura(fc, prof03)
try:
    u.eliminar_profesor_asignatura(sys, prof03)
except ValueError as e:
    print("ERROR: ", e) # intentamos eliminar un profesor que no existe

# observamos como se ha quitado el profesor 3 de la lista de profesores de fc y viceversa
print(fc.obtener_profesores())
print(prof03.obtener_asignaturas())

# cambiamos de departamento a un investigador
inv01.cambiar_departamento(EDepartamento.DIIC)
prof03.cambiar_departamento(EDepartamento.DITEC)

print(u)