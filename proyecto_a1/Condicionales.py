def run():
    cargos = ({"Cargo": "Asistente", "sueldo":900},
              {"Cargo": "Analista", "sueldo":1500},
              {"Cargo": "Expecialista", "sueldo":2000})
    diasmes = 22
    horasdia = 8
    semanahoras = 40
    meshoras = 176
    nombre = input("Ingrese su nombre:")
    horas = int(input("Ingrese horas laboradas:"))
    cargo = int(input("Ingrese un numero (1. Asistente, 2. Analista, 3. Expecialista : "))
    sexo = input("Ingrese sexo (H. Hombre, M . Mujer): ")
    numerohijo = int(input("Ingrese numero de hijos: "))
    cargo = cargo -1
    sueldo = cargos[cargo] ["sueldo"]
    valorhora = sueldo / meshoras
    total = round((valorhora * horas),2)
    print(f"Estimado(a) {nombre} usted ha laborado un total "
          f"de {horas} horas, su cargo es {cargos[cargo]['Cargo']} y su sueldo del mes es: {total} ")
    if (sexo == 'H'):
        bono = 20 * numerohijo
    else:
        bono = 30 * numerohijo
    total = total + bono
    print(f"Usted tiene un bono {bono}, su sueldo actualizado del mes es {total}")


if __name__ == "__main__":
    run()
