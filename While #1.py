c = 1
total_hombres = 0
total_mujeres = 0
suma_notas_hombres = 0
suma_notas_mujeres = 0
print("--- REGISTRO DE 20 ESTUDIANTES ---")
while c <= 20:
    print(f"\nEstudiante {c}:")
    while True:
        genero = input("Ingrese su género (1: Hombre / 2: Mujer): ")
        if genero == "1" or genero == "2":
            break  
        print("Opción inválida. Por favor, ingrese exactamente 1 o 2.")
    while True:
        entrada_nota = input("Ingrese su nota (0 a 5): ")
        if entrada_nota.replace(".", "", 1).isdigit():
            nota = float(entrada_nota)
            if 0 <= nota <= 5:
                break  
            else:
                print("Nota fuera de rango. Debe ser entre 0 y 5.")
        else:
            print("Entrada no válida. Debe ingresar un número.")
    if genero == "1":
        total_hombres += 1
        suma_notas_hombres += nota
    elif genero == "2":
        total_mujeres += 1
        suma_notas_mujeres += nota      
    c += 1  
promedio_hombres = suma_notas_hombres / total_hombres if total_hombres > 0 else 0
promedio_mujeres = suma_notas_mujeres / total_mujeres if total_mujeres > 0 else 0
print("\n--- RESULTADOS FINALES ---")
print(f"Promedio Hombres: {promedio_hombres:.2f}")
print(f"Promedio Mujeres: {promedio_mujeres:.2f}")
if promedio_hombres > promedio_mujeres:
    print(f"El mejor desempeño fue de los hombres con un promedio de {promedio_hombres:.2f}")
elif promedio_mujeres > promedio_hombres:
    print(f"El mejor desempeño fue de las mujeres con un promedio de {promedio_mujeres:.2f}")
else:
    print("Hubo un empate en el desempeño de ambos géneros.")
