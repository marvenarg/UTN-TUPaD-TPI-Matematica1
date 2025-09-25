# Conversión de Números:
# Desarrollen un programa que convierta números decimales a binarios y, de forma opcional, también de binario a decimal.
# Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos.

import os

numd = 0
numb = 0
seguir = True
cociente = 1
nbina = ""

while seguir == True: 
    os.system('cls' if os.name == 'nt' else 'clear')  # limpia la pantalla  
    #Menu
    ancho = 52
    titulo = "Menú"
    opciones = [
        "Elija una de las siguientes opciones:",
        "1. Convertir Decimal a Binario",
        "2. Convertir Binario a Decimal",
        "3. Salir"
    ]

    # Línea superior
    print("-" * ancho)

    # Título centrado
    print("|" + titulo.center(ancho - 2) + "|")

    # Espacio vacío
    print("|" + " " * (ancho - 2) + "|")

    # Opciones
    for opcion in opciones:
        print("| " + opcion.ljust(ancho - 3) + "|")
        print("|" + " " * (ancho - 2) + "|")

    # Línea inferior
    print("-" * ancho)
    
    opcion = int(input("Ingrese una opción (1-3): "))
    
    match opcion:
        case 1:
            # Decimal a Binario
            print("\nConversión de Decimal a Binario\n")
            numd = int(input("\nIngrese un número decimal: "))    
            if numd < 0:
                num_pos = numd * -1                
                esNegativo = True
            else:
                num_pos = numd
                esNegativo = False    

            while cociente != 0:
                cociente = num_pos // 2
                residuo = num_pos % 2
                if residuo == 0:
                    nbina = "0" + nbina
                else:
                    nbina = "1" + nbina    
                    #nbits += 1
                num_pos = cociente

            bits = len(nbina)
            if bits <= 8:
                bits = 8
            elif bits <= 16:
                bits = 16
            elif bits <= 32:
                bits = 32
            else:
                bits = 64

            # Rellenar con ceros a la izquierda manualmente
            while len(nbina) < bits:
                nbina = "0" + nbina

            # Si es negativo, paso a complemento a 1
            if esNegativo:
                comp1 = ""
                for bit in nbina:
                    if bit == "0":
                        comp1 += "1"
                    else:
                        comp1 += "0"

                comp1_lista = list(comp1)  # lo paso a lista porque los strings no son mutables
                llevar = 1

                # Sumo 1 al complemento a 1 para obtener el complemento a 2
                for i in range(len(comp1_lista) - 1, -1, -1):  # recorro de derecha a izquierda
                    if comp1_lista[i] == "1" and llevar == 1:
                        comp1_lista[i] = "0"
                        llevar = 1
                    elif comp1_lista[i] == "0" and llevar == 1:
                        comp1_lista[i] = "1"
                        llevar = 0

                comp2 = "".join(comp1_lista)
                print(f"\nEl número en binario de {bits} bits con signo negativo es: {comp2}")

            else:
                 print(f"\nEl número en binario de {bits} bits es: {nbina}")     
 
                #numb = bin(numd).replace("0b", "")
                #print(f"\nEl número decimal {numd} en binario es: {numb}")

            input("\nPresiona ENTER para continuar...")  # pausa antes de limpiar
        case 2:
            print("\nConversión de Binario a Decimal")

            numb = input("\nIngrese un número binario: ")
            if numb.isdigit() and all(char in '01' for char in numb):
                numd = int(numb, 2)
                print(f"\nEl número binario {numb} en decimal es: {numd}")
            else:
                print("\nError: Por favor, ingrese un número binario válido (solo se permiten 0 y 1).\n")

            input("\nPresiona ENTER para continuar...")             
        case 3:
            print("\nSaliendo del programa...\n")
            seguir = False
        case _:
            print("\nOpción no válida. Por favor, elija una opción del 1 al 3.")
            
            input("\nPresiona ENTER para continuar...")  

