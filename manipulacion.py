carreras: tuple[str, ...] = ("Ingeniería de Software", "Contabilidad", "Derecho")

personas: list[tuple[str, str, int, int]] = [
    # nombre, apellido, edad, carrera
]

estudiantes: list[dict[str, str | int]] = [
    # Lista de diccionario con nombre, apellido, edad, carrera
]

for _ in range(5):
    print("")
    nombre = input("Por favor, ingrese su nombre:")
    apellido = input("Por favor, ingrese su apellido:")
    edad = int (input("Por favor, ingrese su edad:"))
    carrera = int (input("Por favor, ingrese su carrera:"))

    persona = (nombre, apellido, edad, carrera)
    personas.append(persona)

for persona in personas:
  estudiante = {"nombre": persona[0],"apellido": persona[1], 
                "edad": persona[2],"carrera": carreras[persona[3]]}

  estudiantes.append(estudiante)

for estudent in estudiantes:
   print(f"{estudent["nombre"]} {estudent["apellido"]} tiene {estudent["edad"]} años y estudia {estudent["carrera"]}")




