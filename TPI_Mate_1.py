# Conversión de Números:
# Desarrollen un programa que convierta números decimales a binarios y, de forma opcional, también de binario a decimal.
# Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos.

# Se importan las librerias necesarias.
import os

# Se definen las variables
seguir = True

# Menú de opciones.
while seguir == True: 
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla  
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
    
    # Se le solicita al usuario que ingrese una la opción deseada.
    entrada = input("Ingrese una opción (1-3): ")
    if not entrada.isdigit(): # Mejora sugerida por Copilot para validar que no se ingresen letras.
        print("\nOpción inválida: Debe ingresar un número entero en el rango del 1 al 3.") 
        input("\nPresiona ENTER para continuar...")
        continue
    opcion = int(entrada)

    match opcion:
        case 1:
            # Decimal a Binario (CA2 si es negativo)
            print("\nConversión de Decimal a Binario\n") # Se muestra un título
            # --- reinicio de variables para NO arrastrar resultados previos ---
            cociente = 1
            nbina = ""
            comp1 = ""
            comp2 = ""
            # Se solicita al usuario que ingrese un número decimal
            entrada = input("\nIngrese un número decimal: ")
            if not entrada.lstrip('-').isdigit():
                print("\nError: Debe ingresar un número entero válido.")
                input("\nPresiona ENTER para continuar...")
                continue
            numd = int(entrada)        

            # Caso especial: cero
            if numd == 0:
                nbina = "0"
                bits = 8  # mostrarlo en 8 bits por defecto
                # Relleno manual a 'bits'
                while len(nbina) < bits:
                    nbina = "0" + nbina
                print(f"\nEl número en binario de {bits} bits es: {nbina}")
                input("\nPresiona ENTER para continuar...")
                continue  # salir del case 1

            # Determinar signo y trabajar con valor absoluto    
            if numd < 0:
                num_pos = -numd                 
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
                num_pos = cociente
            # Se determina la cantidad de bits.
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

            # Si es negativo, se pasa a complemento a 1 (CA1) y posteriormente a complemento a 2 (CA2)
            if esNegativo:
                i = 0
                while i < len(nbina):
                    if nbina[i] == "0":
                        comp1 += "1"
                    else:
                        comp1 += "0"
                    i += 1

                comp1_lista = []
                j = 0
                while j < len(comp1):
                    comp1_lista.append(comp1[j])
                    j += 1
                # Se invierten los bits, si es 1 pasa a 0 y si es 0 pasa a 1
                llevar = 1
                k = len(comp1_lista) - 1
                while k >= 0:
                    if comp1_lista[k] == "1" and llevar == 1:
                        comp1_lista[k] = "0"
                        llevar = 1
                    elif comp1_lista[k] == "0" and llevar == 1:
                        comp1_lista[k] = "1"
                        llevar = 0
                    k -= 1

                # Complemento a 2
                m = 0
                while m < len(comp1_lista):
                    comp2 += comp1_lista[m]
                    m += 1

                print(f"\nEl número en binario de {bits} bits con signo negativo (CA2) es: {comp2}") # Si es negativo se muestra este mensaje.
            else:
                print(f"\nEl número en binario de {bits} bits (representación directa) es: {nbina}") # Si es positivo se muestra este mensaje.

            input("\nPresiona ENTER para continuar...") # pausa antes de limpiar la pantalla
 
        case 2: 
            # Binario a Decimal
            print("\nConversión de Binario a Decimal") # Se muestra un título

            numb = input("\nIngrese un número binario: ")
            if numb.isdigit() and all(char in '01' for char in numb):
                numd = int(numb, 2) # Se convierte el número binario a decimal
                print(f"\nEl número binario {numb} en decimal es: {numd}")
            else: # En el caso que se ingrese un número inválido se muestra un mensaje.
                print("\nError: Por favor, ingrese un número binario válido (solo se permiten 0 y 1).\n")

            input("\nPresiona ENTER para continuar...") # pausa antes de limpiar la pantalla            
        case 3:
            print("\nSaliendo del programa...\n") # Se muestra un mensaje antes de salir del programa.
            seguir = False
        case _:
            print("\nOpción no válida. Por favor, elija una opción del 1 al 3.") # En el caso que se ingrese una opción no válida, se muestra este mensaje.
            
            input("\nPresiona ENTER para continuar...") # pausa antes de limpiar la pantalla

