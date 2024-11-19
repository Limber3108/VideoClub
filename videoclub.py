print("Bienvenido al videoclub para acceder debes de rellenar lo siguiente que te pido")
nombre = input("Introduce tu nombre: ")
apellidos = input("Introduce tu apellido: ")
edad = int(input("Introduce tu edad: "))
if edad < 13:
    peliculas = int(input(""" Puedes elegir algunas de estas 2 peliculas
                                1: Campeones:
                                2: Un Gran equipo
                                Introduce el numero 1 o 2: """))
    if peliculas == 1:
        eleccion = "Campeones"
    if peliculas == 2:
        eleccion = "Un gran equipo"
elif edad > 12 and edad < 18:
    peliculas2 = int(input("""Puedes elegir algunas de estas 3 peliculas
                                3: Campeones
                                4: Un gran equipo
                                5: Blade Runner
                                6: El caballero oscuro 
                                Introduce del 3 al 6: """))
    if peliculas2 == 3:
        eleccion = "Campeones"
    if peliculas2 == 4:
        eleccion = "Un gran equipo"
    if peliculas2 == 5:
        eleccion = "Blade Runner"
    if peliculas2 == 6:
        eleccion = "El Caballero oscuro"
else:
    peliculas3 = int(input("""Puedes elegir algunas de estas 3 peliculas
                                7: Campeones
                                8: Un gran equipo
                                9: Blade Runner
                                10: El caballero oscuro
                                11: Matrix
                                12: Watchmen
                                Introduce del 7 al 12: """))
    if peliculas3 == 7:
        eleccion = "Campeones"
    if peliculas3 == 8:
        eleccion = "Un gran equipo"
    if peliculas3 == 9:
        eleccion = "Blade runner"
    if peliculas3 == 10:
        eleccion = "El caballero oscuro"
    if peliculas3 == 11:
        eleccion = "Matrix"
    if peliculas3 == 12:
        eleccion = "Watchmen"
print(nombre, apellidos, edad, eleccion)