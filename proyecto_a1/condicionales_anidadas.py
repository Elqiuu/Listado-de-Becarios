#Listado de Becarios
#Hacer un diccionario de sistema becario

#Academicas: Promedio de 95 - 100 y Asistencia de asignaturas >= 90% y deudas de 0.

#Situacion vulnerable: Estado socio economico bajo o medio bajo y Asistencia de asignaturas >= 90%, Promedio de 80 - 100
#y deudas de 0
#Bajo, medio bajo,medio,medio alto, alto

def beca_academica(estudiantes):
    for i in estudiantes:
        cumplea= False
        cumplep = False
        cumpled = False
        if i['promedio']>= 95 and i['promedio']<= 100:
            cumplep = True

        if i['asistencia'] >= 95 and i['asistencia'] <= 100:
            cumplea = True

        if i['deuda'] == 0:
            cumpled = True

        if cumplep == True and cumplea == True and cumpled == True:
            i['beca'] = True

    for i in estudiantes:
        if i['beca'] == True:
            print(f"Beca academica {i['nombre']} {i['beca']}")

def beca_socioeconomica(estudiantes):
    for x in estudiantes:
        cumplee = False
        cumpl = False
        cum = False
        socio = False
        if x['promedio']>= 90 and x['promedio']<= 100:
            cumplee = True

        if x['asistencia']>= 90 and x['promedio']<=100:
            cumpl = True

        if x['deuda'] == 0:
            cum = True

        if x['estado'] == bajo:
            socio = True

        if cumplee == True and cumpl == True and cum == True and socio == True:
            x['beca'] == True
            x['tipo'] == 'Socio-economico'

    for x in estudiantes:
        if x['beca'] == True:
            print(f"Estimado\a {x['nombre']} fue aceptado {x['beca']} {x['tipo']}")








def run():
    estudiantes = [
        {'nombre' : 'Elkin' , 'carrera' :  'Software' , 'sexo' : 'H' , 'estado' : 'bajo' , 'promedio' : 95 , 'asistencia' : 100,'beca': False, 'deuda' : 0, 'tipo' : ''},
        {'nombre' : 'Kevin' , 'carrera' :  'Software' , 'sexo' : 'H' , 'estado' : 'bajo' , 'promedio' : 90 , 'asistencia' : 90 ,'beca': False, 'deuda' : 0 , 'tipo' : ''},
        {'nombre' : 'Kristhel' , 'carrera' :  'Software' , 'sexo' : 'M' , 'estado' : 'medio bajo' , 'promedio' : 79 , 'asistencia' : 95 ,'beca': False, 'deuda' : 12, 'tipo' : ''},
        {'nombre' : 'Mariela' , 'carrera' :  'Biotecnologia' , 'sexo' : 'M' , 'estado' : 'alto' , 'promedio' : 100 , 'asistencia' : 80 ,'beca': False, 'deuda' : 0, 'tipo' : ''},
        {'nombre' : 'Sofia' , 'carrera' :  'Biotecnologia' , 'sexo' : 'M' , 'estado' : 'alto' , 'promedio' : 100 , 'asistencia' : 98 ,'beca': False, 'deuda' : 10, 'tipo' : ''},
        {'nombre' : 'Williams' , 'carrera' :  'Biotecnologia' , 'sexo' : 'H' , 'estado' : 'alto' , 'promedio' : 94 , 'asistencia' : 100,'beca': False, 'deuda' : 0, 'tipo' : ''},
        {'nombre' : 'Miguel' , 'carrera' :  'Industrial' , 'sexo' : 'H' , 'estado' : 'medio alto' , 'promedio' : 90 , 'asistencia' : 98,'beca': False, 'deuda' : 67, 'tipo' : ''},
        {'nombre' : 'Carmen' , 'carrera' :  'Industrial' , 'sexo' : 'M' , 'estado' : 'alto' , 'promedio' : 95 , 'asistencia' : 90,'beca': False, 'deuda' : 0, 'tipo' : ''},
        {'nombre' : 'Cristopher' , 'carrera' :  'Industrial' , 'sexo' : 'H' , 'estado' : 'medio alto' , 'promedio' : 70 , 'asistencia' : 96,'beca': False, 'deuda' : 13, 'tipo' : ''},
        {'nombre' : 'Edison' , 'carrera' :  'Industrial' , 'sexo' : 'H' , 'estado' : 'medio alto' , 'promedio' : 80 , 'asistencia' : 97,'beca': False, 'deuda' : 0, 'tipo' : ''}
                   ]
    beca_academica(estudiantes)
    beca_socioeconamica(estudiantes)




if __name__ == "__main__":
   run()
