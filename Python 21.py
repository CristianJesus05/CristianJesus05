top1_n = top2_n = top3_n = "Nadie"
top1_t = top2_t = top3_t = 9999.0
print("\n--- REGISTRO Y COMPETENCIA ---")
for i in range(1, 6):
    nombre = ""
    for intento in range(100):
        nombre = input(f"\nNombre del Atleta {i}: ").strip()
        if nombre != "" and not nombre.isdigit():
            break
    pais = ""
    for intento in range(100):
        pais = input(f"País de {nombre}: ").strip()
        if pais != "" and not pais.isdigit():
            break  
    tiempo_total = 0.0
    todos_menor_20 = True
    al_menos_un_15 = False
    for dia in range(1, 6):
        resp = ""
        for intento in range(100):
            resp = input(f"¿{nombre} hizo la prueba el Día {dia}? (si/no): ").strip().lower()
            if resp == "si" or resp == "no":
                break
        if resp == "si":
            t = float(input("  Tiempo en minutos: "))
            tiempo_total += t          
            if t >= 20: 
                todos_menor_20 = False
            if t <= 15: 
                al_menos_un_15 = True
        else:
            todos_menor_20 = False
    if todos_menor_20 and al_menos_un_15:
        print(f"--> ¡{nombre} ({pais}) es APTO! Tiempo total: {tiempo_total:.2f} min")       
        if tiempo_total < top1_t:
            top3_t, top3_n = top2_t, top2_n; top2_t, top2_n = top1_t, top1_n; top1_t, top1_n = tiempo_total, nombre
        elif tiempo_total < top2_t:
            top3_t, top3_n = top2_t, top2_n; top2_t, top2_n = tiempo_total, nombre
        elif tiempo_total < top3_t:
            top3_t, top3_n = tiempo_total, nombre
    else:
        print(f"--> {nombre} NO es apto.")
print("\n=== TOP 3 FINAL (ACUMULADO 5 DÍAS) ===")
print(f"1º Lugar: {top1_n} con {top1_t:.2f} min")
print(f"2º Lugar: {top2_n} con {top2_t:.2f} min")
print(f"3º Lugar: {top3_n} con {top3_t:.2f} min")
