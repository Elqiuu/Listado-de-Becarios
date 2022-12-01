# Listado de becarios
# bajo, medio bajo, medio, medio alto, alto
estudiantes = [
        {'nombre': 'Elkin','carrera': 'Software', 'sexo': 'M', 'estado': 'Medio', 'promedio': 80, 'asistencia': 100, 'beca': False, 'deuda':20.50, 'tipo':''},
        {'nombre': 'Kevin','carrera': 'Software', 'sexo': 'H', 'estado': 'Medio alto', 'promedio': 92, 'asistencia': 95, 'beca': False,'deuda':0, 'tipo':''},
        {'nombre': 'Danilo','carrera': 'Software', 'sexo': 'H', 'estado': 'Medio bajo', 'promedio': 98, 'asistencia': 80, 'beca': False,'deuda':0, 'tipo':''},
        {'nombre': 'Sofi','carrera': 'Biologia', 'sexo': 'M', 'estado': 'Alto', 'promedio': 95, 'asistencia': 98, 'beca': False,'deuda':0,'tipo':''},
        {'nombre': 'Edison','carrera': 'Biologia', 'sexo': 'H', 'estado': 'Alto', 'promedio': 90, 'asistencia': 99, 'beca': False,'deuda':0, 'tipo':''},
        {'nombre': 'Jonayker','carrera': 'Biologia', 'sexo': 'M', 'estado': 'Bajo', 'promedio': 85, 'asistencia': 93, 'beca': False,'deuda':0, 'tipo':''},
        {'nombre': 'Diana','carrera': 'Alimento', 'sexo': 'M', 'estado': 'Bajo', 'promedio': 88, 'asistencia': 92, 'beca': False,'deuda':0, 'tipo':''},
        {'nombre': 'Cristhina','carrera': 'Alimento', 'sexo': 'H', 'estado': 'Medio bajo', 'promedio': 92, 'asistencia': 90, 'beca': False,'deuda':0, 'tipo':''},
        {'nombre': 'Andrea','carrera': 'Industrial', 'sexo': 'H', 'estado': 'Medio bajo', 'promedio': 93, 'asistencia': 85, 'beca': False,'deuda':0, 'tipo':''},
        {'nombre': 'Zuleyka','carrera': 'Industrial', 'sexo': 'H', 'estado': 'Alto', 'promedio': 95, 'asistencia': 89, 'beca': False,'deuda':0, 'tipo':''},
        ]

def beca_academica():
    for i in estudiantes:
        cumplep = False
        cumplea = False
        cumpled = False
        if 95 <= i['promedio'] <= 100:
            cumplep = True

        if 95 <= i['asistencia'] <= 100:
            cumplea = True

        if i['deuda'] == 0:
            cumpled = True


        if cumplep and cumplea and cumpled:
            i['beca'] = True
            i['tipo'] = 'Exelencia academica'

    for i in estudiantes:
        if i['beca'] == True:
            print(f"Beca académica a {i['nombre']} {i['tipo']} ")




def beca_socioeconomia():
    for i in estudiantes:
        cumplee= False
        cumpl=False
        cum=False
        cu=False
        if 90 <= i['promedio'] <= 100:
            cumplee = True

        if 90 <= i['asistencia'] <= 100:
            cumpl = True

        if i['deuda'] ==0:
            cum= True

        if i['estado'] == 'Bajo' or i['estado']== 'Medio bajo':
            cu= True

        if cumplee and cumpl and cum and cu:
            i['beca'] = True
            i['tipo'] = 'Socio-economica'

    for i in estudiantes:
        if i['beca']== True:
            print(f"Beca academica a {i['nombre']} {i['tipo']} ")


def run():
    beca_academica()
    beca_socioeconomia()


if __name__ == "__main__":
    run()

