import random
import time

opcionValida = "Ingrese una opción valida"
titulo = "A seleccionado la dificultad"

print("[Menu Matemático]")

menu = ("""
¿Que desea hacer?
	
1) Sumar
2) Restar
3) Multiplicar
4) Dividir
5) Salir
""")

menuDificultad = ("""
1) Dificultad 1
2) Dificultad 2
3) Dificultad 3
4) Dificultad 4
""")

print(menu)

opcion = int(input("Ingrese su opción: "))
print("\n")


while opcion:

    if opcion == 1:
        print("Ingrese cantidad de ejercicios a realizar")
        ejercicios = int(input("Cantidad: "))
        print("\n")
        print("Ingrese la dificultad", menuDificultad)
        dificultad = int(input("Dificultad: "))

        while dificultad:
            if dificultad == 1:
                correctas = 0
                incorrectas = 0
                print(titulo, "1")
                print("\n")
                for i in range(ejercicios):
                    respuestas = {}
                    aleatorio1 = random.randint(1, 11)
                    aleatorio2 = random.randint(1, 11)
                    print("Sumar", aleatorio1, "+", aleatorio2)
                    respuestas = int(input("Respuesta: "))
                    respuesta = aleatorio1 + aleatorio2
                    while True:
                        if respuestas == respuesta:
                            print("Respuesta correcta!")
                            correctas = correctas+1
                        else:
                            print("Respuesta incorrecta!")
                            incorrectas = incorrectas+1
                        break
                print("\n")
                print("Cantidad de buenas:", correctas)
                print("Cantidad de malas:", incorrectas)
                break

            elif dificultad == 2:
                correctas = 0
                incorrectas = 0
                print(titulo, "2")
                print("\n")
                for i in range(ejercicios):
                    respuestas = {}
                    aleatorio1 = random.randint(10, 101)
                    aleatorio2 = random.randint(10, 101)
                    print("Sumar", aleatorio1, "+", aleatorio2)
                    respuestas = int(input("Respuesta: "))
                    respuesta = aleatorio1 + aleatorio2
                    while True:
                        if respuestas == respuesta:
                            print("Respuesta correcta!")
                            correctas = correctas+1
                        else:
                            print("Respuesta incorrecta!")
                            incorrectas = incorrectas+1
                        break
                print("\n")
                print("Cantidad de buenas:", correctas)
                print("Cantidad de malas:", incorrectas)
                break

            elif dificultad == 3:
                correctas = 0
                incorrectas = 0
                print(titulo, "3")
                print("\n")
                for i in range(ejercicios):
                    respuestas = {}
                    aleatorio1 = random.randint(100, 1001)
                    aleatorio2 = random.randint(100, 1001)
                    print("Sumar", aleatorio1, "+", aleatorio2)
                    respuestas = int(input("Respuesta: "))
                    respuesta = aleatorio1 + aleatorio2
                    while True:
                        if respuestas == respuesta:
                            print("Respuesta correcta!")
                            correctas = correctas+1
                        else:
                            print("Respuesta incorrecta!")
                            incorrectas = incorrectas+1
                        break
                print("\n")
                print("Cantidad de buenas:", correctas)
                print("Cantidad de malas:", incorrectas)
                break

            elif dificultad == 4:
                correctas = 0
                incorrectas = 0
                print(titulo, "4")
                print("\n")
                for i in range(ejercicios):
                    respuestas = {}
                    aleatorio1 = random.randint(0, 1001)
                    aleatorio2 = random.randint(0, 1001)
                    print("Sumar", aleatorio1, "+", aleatorio2)
                    respuestas = int(input("Respuesta: "))
                    respuesta = aleatorio1 + aleatorio2
                    while True:
                        if respuestas == respuesta:
                            print("Respuesta correcta!")
                            correctas = correctas+1
                        else:
                            print("Respuesta incorrecta!")
                            incorrectas = incorrectas+1
                        break
                print("\n")
                print("Cantidad de buenas:", correctas)
                print("Cantidad de malas:", incorrectas)
                break

            else:
                print(opcionValida)
                break
        print(menu)

        opcion = int(input("Ingrese su opcion: "))
    elif opcion == 2:
        print("Ingrese cantidad de ejercicios a realizar")
        ejercicios = int(input("Cantidad: "))
        print("\n")
        print("Ingrese la dificultad", menuDificultad)
        dificultad = int(input("Dificultad: "))

        while dificultad:
            if dificultad == 1:
                correctas = 0
                incorrectas = 0
                print(titulo, "1")
                print("\n")
                for i in range(ejercicios):
                    respuestas = {}
                    aleatorio1 = random.randint(1, 11)
                    aleatorio2 = random.randint(1, 11)
                    print("Restar", aleatorio1, "-", aleatorio2)
                    respuestas = int(input("Respuesta: "))
                    respuesta = aleatorio1 - aleatorio2
                    while True:
                        if respuestas == respuesta:
                            print("Respuesta correcta!")
                            correctas = correctas+1
                        else:
                            print("Respuesta incorrecta!")
                            incorrectas = incorrectas+1
                        break
                print("\n")
                print("Cantidad de buenas:", correctas)
                print("Cantidad de malas:", incorrectas)
                break

            elif dificultad == 2:
                correctas = 0
                incorrectas = 0
                print(titulo, "2")
                print("\n")
                for i in range(ejercicios):
                    respuestas = {}
                    aleatorio1 = random.randint(10, 101)
                    aleatorio2 = random.randint(10, 101)
                    print("Restar", aleatorio1, "-", aleatorio2)
                    respuestas = int(input("Respuesta: "))
                    respuesta = aleatorio1 - aleatorio2
                    while True:
                        if respuestas == respuesta:
                            print("Respuesta correcta!")
                            correctas = correctas+1
                        else:
                            print("Respuesta incorrecta!")
                            incorrectas = incorrectas+1
                        break
                print("\n")
                print("Cantidad de buenas:", correctas)
                print("Cantidad de malas:", incorrectas)
                break

            elif dificultad == 3:
                correctas = 0
                incorrectas = 0
                print(titulo, "3")
                print("\n")
                for i in range(ejercicios):
                    respuestas = {}
                    aleatorio1 = random.randint(100, 1001)
                    aleatorio2 = random.randint(100, 1001)
                    print("Restar", aleatorio1, "-", aleatorio2)
                    respuestas = int(input("Respuesta: "))
                    respuesta = aleatorio1 - aleatorio2
                    while True:
                        if respuestas == respuesta:
                            print("Respuesta correcta!")
                            correctas = correctas+1
                        else:
                            print("Respuesta incorrecta!")
                            incorrectas = incorrectas+1
                        break
                print("\n")
                print("Cantidad de buenas:", correctas)
                print("Cantidad de malas:", incorrectas)
                break

            elif dificultad == 4:
                correctas = 0
                incorrectas = 0
                print(titulo, "4")
                print("\n")
                for i in range(ejercicios):
                    respuestas = {}
                    aleatorio1 = random.randint(0, 1001)
                    aleatorio2 = random.randint(0, 1001)
                    print("Restar", aleatorio1, "-", aleatorio2)
                    respuestas = int(input("Respuesta: "))
                    respuesta = aleatorio1 - aleatorio2
                    while True:
                        if respuestas == respuesta:
                            print("Respuesta correcta!")
                            correctas = correctas+1
                        else:
                            print("Respuesta incorrecta!")
                            incorrectas = incorrectas+1
                        break
                print("\n")
                print("Cantidad de buenas:", correctas)
                print("Cantidad de malas:", incorrectas)
                break

            else:
                print(opcionValida)
                break
        print(menu)

        opcion = int(input("Ingrese su opcion: "))
    elif opcion == 3:
        print("Ingrese cantidad de ejercicios a realizar")
        ejercicios = int(input("Cantidad: "))
        print("\n")
        print("Ingrese la dificultad", menuDificultad)
        dificultad = int(input("Dificultad: "))

        while dificultad:
            if dificultad == 1:
                correctas = 0
                incorrectas = 0
                print(titulo, "1")
                print("\n")
                for i in range(ejercicios):
                    respuestas = {}
                    aleatorio1 = random.randint(1, 11)
                    aleatorio2 = random.randint(1, 11)
                    print("Multiplicar", aleatorio1, "*", aleatorio2)
                    respuestas = int(input("Respuesta: "))
                    respuesta = aleatorio1 * aleatorio2
                    while True:
                        if respuestas == respuesta:
                            print("Respuesta correcta!")
                            correctas = correctas+1
                        else:
                            print("Respuesta incorrecta!")
                            incorrectas = incorrectas+1
                        break
                print("\n")
                print("Cantidad de buenas:", correctas)
                print("Cantidad de malas:", incorrectas)
                break

            elif dificultad == 2:
                correctas = 0
                incorrectas = 0
                print(titulo, "2")
                print("\n")
                for i in range(ejercicios):
                    respuestas = {}
                    aleatorio1 = random.randint(10, 101)
                    aleatorio2 = random.randint(10, 101)
                    print("Multiplicar", aleatorio1, "*", aleatorio2)
                    respuestas = int(input("Respuesta: "))
                    respuesta = aleatorio1 * aleatorio2
                    while True:
                        if respuestas == respuesta:
                            print("Respuesta correcta!")
                            correctas = correctas+1
                        else:
                            print("Respuesta incorrecta!")
                            incorrectas = incorrectas+1
                        break
                print("\n")
                print("Cantidad de buenas:", correctas)
                print("Cantidad de malas:", incorrectas)
                break

            elif dificultad == 3:
                correctas = 0
                incorrectas = 0
                print(titulo, "3")
                print("\n")
                for i in range(ejercicios):
                    respuestas = {}
                    aleatorio1 = random.randint(100, 1001)
                    aleatorio2 = random.randint(100, 1001)
                    print("Multiplicar", aleatorio1, "*", aleatorio2)
                    respuestas = int(input("Respuesta: "))
                    respuesta = aleatorio1 * aleatorio2
                    while True:
                        if respuestas == respuesta:
                            print("Respuesta correcta!")
                            correctas = correctas+1
                        else:
                            print("Respuesta incorrecta!")
                            incorrectas = incorrectas+1
                        break
                print("\n")
                print("Cantidad de buenas:", correctas)
                print("Cantidad de malas:", incorrectas)
                break

            elif dificultad == 4:
                correctas = 0
                incorrectas = 0
                print(titulo, "4")
                print("\n")
                for i in range(ejercicios):
                    respuestas = {}
                    aleatorio1 = random.randint(0, 1001)
                    aleatorio2 = random.randint(0, 1001)
                    print("Multiplicar", aleatorio1, "*", aleatorio2)
                    respuestas = int(input("Respuesta: "))
                    respuesta = aleatorio1 * aleatorio2
                    while True:
                        if respuestas == respuesta:
                            print("Respuesta correcta!")
                            correctas = correctas+1
                        else:
                            print("Respuesta incorrecta!")
                            incorrectas = incorrectas+1
                        break
                print("\n")
                print("Cantidad de buenas:", correctas)
                print("Cantidad de malas:", incorrectas)
                break

            else:
                print(opcionValida)
                break
        print(menu)

        opcion = int(input("Ingrese su opcion: "))
    elif opcion == 4:
        print("Ingrese cantidad de ejercicios a realizar")
        ejercicios = int(input("Cantidad: "))
        print("\n")
        print("Ingrese la dificultad", menuDificultad)
        dificultad = int(input("Dificultad: "))

        while dificultad:
            if dificultad == 1:
                correctas = 0
                incorrectas = 0
                print(titulo, "1")
                print("\n")
                for i in range(ejercicios):
                    respuestas = {}
                    resto = {}
                    dividendo = random.randint(1, 11)
                    divisor = random.randint(1, 11)
                    print("Dividir", dividendo, "/", divisor)
                    respuestas = int(input("Respuesta: "))
                    respuesta = dividendo // divisor
                    while True:
                        if respuestas == respuesta:
                            if respuestas == 0:
                                resto = int(input("Resto: "))
                                resto = dividendo * divisor + resto
                                print("Respuesta correcta!")
                                correctas = correctas+1
                            elif respuestas != 0:
                                resto = int(input("Resto: "))
                                resto = dividendo * divisor + resto
                                print("Respuesta correcta!")
                                correctas = correctas+1
                        else:
                            print("Respuesta incorrecta!")
                            incorrectas = incorrectas+1
                        break
                print("\n")
                print("Cantidad de buenas:", correctas)
                print("Cantidad de malas:", incorrectas)
                break

            elif dificultad == 2:
                correctas = 0
                incorrectas = 0
                print(titulo, "2")
                print("\n")
                for i in range(ejercicios):
                    respuestas = {}
                    resto = {}
                    dividendo = random.randint(1, 11)
                    divisor = random.randint(1, 11)
                    print("Dividir", dividendo, "/", divisor)
                    respuestas = int(input("Respuesta: "))
                    respuesta = dividendo // divisor
                    while True:
                        if respuestas == respuesta:
                            if respuestas == 0:
                                resto = int(input("Resto: "))
                                resto = dividendo * divisor + resto
                                print("Respuesta correcta!")
                                correctas = correctas+1
                            elif respuestas != 0:
                                resto = int(input("Resto: "))
                                resto = dividendo * divisor + resto
                                print("Respuesta correcta!")
                                correctas = correctas+1
                        else:
                            print("Respuesta incorrecta!")
                            incorrectas = incorrectas+1
                        break
                print("\n")
                print("Cantidad de buenas:", correctas)
                print("Cantidad de malas:", incorrectas)
                break

            elif dificultad == 3:
                correctas = 0
                incorrectas = 0
                print(titulo, "3")
                print("\n")
                for i in range(ejercicios):
                    respuestas = {}
                    resto = {}
                    dividendo = random.randint(1, 11)
                    divisor = random.randint(1, 11)
                    print("Dividir", dividendo, "/", divisor)
                    respuestas = int(input("Respuesta: "))
                    respuesta = dividendo // divisor
                    while True:
                        if respuestas == respuesta:
                            if respuestas == 0:
                                resto = int(input("Resto: "))
                                resto = dividendo * divisor + resto
                                print("Respuesta correcta!")
                                correctas = correctas+1
                            elif respuestas != 0:
                                resto = int(input("Resto: "))
                                resto = dividendo * divisor + resto
                                print("Respuesta correcta!")
                                correctas = correctas+1
                        else:
                            print("Respuesta incorrecta!")
                            incorrectas = incorrectas+1
                        break
                print("\n")
                print("Cantidad de buenas:", correctas)
                print("Cantidad de malas:", incorrectas)
                break

            elif dificultad == 4:
                correctas = 0
                incorrectas = 0
                print(titulo, "4")
                print("\n")
                for i in range(ejercicios):
                    respuestas = {}
                    resto = {}
                    dividendo = random.randint(1, 11)
                    divisor = random.randint(1, 11)
                    print("Dividir", dividendo, "/", divisor)
                    respuestas = int(input("Respuesta: "))
                    respuesta = dividendo // divisor
                    while True:
                        if respuestas == respuesta:
                            if respuestas == 0:
                                resto = int(input("Resto: "))
                                resto = dividendo * divisor + resto
                                print("Respuesta correcta!")
                                correctas = correctas+1
                            elif respuestas != 0:
                                resto = int(input("Resto: "))
                                resto = dividendo * divisor + resto
                                print("Respuesta correcta!")
                                correctas = correctas+1
                        else:
                            print("Respuesta incorrecta!")
                            incorrectas = incorrectas+1
                        break
                print("\n")
                print("Cantidad de buenas:", correctas)
                print("Cantidad de malas:", incorrectas)
                break

            else:
                print(opcionValida)
                break
        print(menu)

        opcion = int(input("Ingrese su opcion: "))
    elif opcion == 5:
        print("Saliendo...")
        time.sleep(2)
        print("Hasta la proxima!")
        time.sleep(1)
        break

    else:
        print(opcionValida)

        opcion = int(input("Ingrese su opcion: "))
