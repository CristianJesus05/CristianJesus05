saldo = 500000
ejecutando = True

while ejecutando:
    print("\n--- CAJERO AUTOMÁTICO ---")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")

    # Evaluamos si escribieron el número o el número con espacio
    if opcion == "1" or opcion == "1 ":
        print("\nSaldo disponible: $", saldo)

    elif opcion == "2" or opcion == "2 ":
        monto = float(input("Ingrese el monto a retirar: $"))
        
        if monto <= 0:
            print("Error: El monto a retirar debe ser mayor a $0.")
        elif monto > saldo:
            print("Error: Saldo insuficiente.")
        else:
            saldo = saldo - monto
            print("Retiro exitoso. Nuevo saldo: $", saldo)

    elif opcion == "3" or opcion == "3 ":
        monto = float(input("Ingrese el monto a depositar: $"))
        
        if monto <= 0:
            print("Error: El monto a depositar debe ser mayor a $0.")
        else:
            saldo = saldo + monto
            print("Depósito exitoso. Nuevo saldo: $", saldo)

    elif opcion == "4" or opcion == "4 ":
        print("\nGracias por utilizar el cajero automático. ¡Hasta luego!")
        ejecutando = False

    else:
        print("Opción inválida. Intente de nuevo con un número del 1 al 4.")
