# ==============================================================================
# SAGA DE REPOSITORIOS PYTHON 2026
# Repositorio: 2026_10_P02_R02_gestor-presupuestos-capacitacion
# Principio 2: Control de flujo y estructuras de datos básicas (Nivel: Consolidación)
# ==============================================================================

# --- DATOS INICIALES DEL PROGRAMA ---
actividades = [
    {"id": 1, "nombre": "Excel intermedio", "costo": 450.0, "participantes": 20, "categoria": "Ofimática"},
    {"id": 2, "nombre": "Python básico", "costo": 900.0, "participantes": 15, "categoria": "Tecnología"},
    {"id": 3, "nombre": "Seguridad laboral", "costo": 350.0, "participantes": 30, "categoria": "Seguridad"},
    {"id": 4, "nombre": "Power BI", "costo": 750.0, "participantes": 12, "categoria": "Tecnología"},
    {"id": 5, "nombre": "Liderazgo", "costo": 600.0, "participantes": 18, "categoria": "Gestión"},
    {"id": 6, "nombre": "Comunicación", "costo": 280.0, "participantes": 25, "categoria": "Gestión"}
]

presupuesto_disponible = 3000.0
ultimo_id_asignado = 6


# --- FUNCIONES AUXILIARES DE VALIDACIÓN ---

def leer_entero_positivo(mensaje):
    """Solicita un número entero estrictamente mayor a cero con reintento ante errores."""
    while True:
        entrada = input(mensaje).strip()
        try:
            val = int(entrada)
            if val > 0:
                return val
            print("  [Error] Debe ingresar un número entero mayor a 0.")
        except ValueError:
            print("  [Error] Entrada no válida. Debe ingresar un número entero.")


def leer_float_positivo(mensaje, incluir_cero=False):
    """Solicita un número decimal positivo con opción de permitir cero."""
    while True:
        entrada = input(mensaje).strip()
        try:
            val = float(entrada)
            if incluir_cero and val >= 0:
                return val
            elif not incluir_cero and val > 0:
                return val
            
            limite_txt = "mayor o igual a 0" if incluir_cero else "mayor a 0"
            print(f"  [Error] Debe ingresar un valor numérico {limite_txt}.")
        except ValueError:
            print("  [Error] Entrada no válida. Debe ingresar un número válido.")


def leer_texto_no_vacio(mensaje):
    """Solicita una cadena de texto asegurando que no esté vacía."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("  [Error] El texto no puede estar vacío. Intente de nuevo.")


def obtener_actividad_por_id(id_actividad):
    """Busca y retorna el diccionario de la actividad por ID, o None si no existe."""
    for act in actividades:
        if act["id"] == id_actividad:
            return act
    return None


# --- FUNCIONES DEL MENÚ PRINCIPAL ---

def RF01_mostrar_actividades(lista=None):
    """RF01: Muestra todas las actividades registradas en formato tabular."""
    datos = actividades if lista is None else lista
    
    print("\n--------------------------------------------------------------------------------")
    print(f"{'ID':<5} | {'Nombre':<22} | {'Costo (S/)':<12} | {'Participantes':<13} | {'Categoría':<15}")
    print("--------------------------------------------------------------------------------")
    
    if not datos:
        print("  No hay actividades para mostrar.")
        print("--------------------------------------------------------------------------------")
        return

    for act in datos:
        print(f"{act['id']:<5} | {act['nombre']:<22} | {act['costo']:<12.2f} | {act['participantes']:<13} | {act['categoria']:<15}")
    print("--------------------------------------------------------------------------------")


def RF02_registrar_actividad():
    """RF02: Registra una nueva actividad asignando un ID único automático."""
    global ultimo_id_asignado
    print("\n--- REGISTRAR NUEVA ACTIVIDAD ---")
    
    nombre = leer_texto_no_vacio("Ingrese nombre de la actividad: ")
    
    # Verificación de duplicado por nombre (Ejercicio de lógica #11)
    duplicado = False
    for act in actividades:
        if act["nombre"].lower() == nombre.lower():
            duplicado = True
            break
            
    if duplicado:
        print(f"  [Advertencia] Ya existe una actividad registrada con el nombre '{nombre}'.")
        confirmar = input("¿Desea registrarla de todos modos? (s/n): ").strip().lower()
        if confirmar != 's':
            print("  Registro cancelado por el usuario.")
            return

    costo = leer_float_positivo("Ingrese el costo de la actividad (S/): ")
    participantes = leer_entero_positivo("Ingrese número de participantes: ")
    categoria = leer_texto_no_vacio("Ingrese la categoría: ")

    ultimo_id_asignado += 1
    nueva_actividad = {
        "id": ultimo_id_asignado,
        "nombre": nombre,
        "costo": costo,
        "participantes": participantes,
        "categoria": categoria
    }
    actividades.append(nueva_actividad)
    print(f"  [Éxito] Actividad '{nombre}' registrada con el ID {ultimo_id_asignado}.")


def RF03_buscar_actividad():
    """RF03: Busca y muestra una actividad por su ID."""
    print("\n--- BUSCAR ACTIVIDAD POR ID ---")
    id_buscar = leer_entero_positivo("Ingrese el ID a buscar: ")
    act = obtener_actividad_por_id(id_buscar)
    
    if act is None:
        print(f"  [Información] No se encontró ninguna actividad con el ID {id_buscar}.")
    else:
        print("\n  Información encontrada:")
        print(f"  - ID: {act['id']}")
        print(f"  - Nombre: {act['nombre']}")
        print(f"  - Costo: S/ {act['costo']:.2f}")
        print(f"  - Participantes: {act['participantes']}")
        print(f"  - Categoría: {act['categoria']}")


def RF04_actualizar_actividad():
    """RF04: Modifica los campos de una actividad existente dejando vacíos los no modificados."""
    print("\n--- ACTUALIZAR ACTIVIDAD ---")
    id_act = leer_entero_positivo("Ingrese el ID de la actividad a actualizar: ")
    act = obtener_actividad_por_id(id_act)
    
    if act is None:
        print(f"  [Información] No existe actividad con el ID {id_act}.")
        return

    print(f"  Actualizando '{act['nombre']}' (Presione Enter sin escribir nada para conservar el valor actual):")

    # Actualizar Nombre
    nuevo_nombre = input(f"  Nuevo nombre [{act['nombre']}]: ").strip()
    if nuevo_nombre:
        act["nombre"] = nuevo_nombre

    # Actualizar Costo
    nuevo_costo_str = input(f"  Nuevo costo [{act['costo']:.2f}]: ").strip()
    if nuevo_costo_str:
        try:
            val_costo = float(nuevo_costo_str)
            if val_costo > 0:
                act["costo"] = val_costo
            else:
                print("  [Advertencia] Costo inválido. Conservando valor anterior.")
        except ValueError:
            print("  [Advertencia] Entrada no numérica. Conservando valor anterior.")

    # Actualizar Participantes
    nuevos_part_str = input(f"  Nuevos participantes [{act['participantes']}]: ").strip()
    if nuevos_part_str:
        try:
            val_part = int(nuevos_part_str)
            if val_part > 0:
                act["participantes"] = val_part
            else:
                print("  [Advertencia] Cantidad de participantes inválida. Conservando valor anterior.")
        except ValueError:
            print("  [Advertencia] Entrada no entera. Conservando valor anterior.")

    # Actualizar Categoría
    nueva_cat = input(f"  Nueva categoría [{act['categoria']}]: ").strip()
    if nueva_cat:
        act["categoria"] = nueva_cat

    print("  [Éxito] Registro actualizado correctamente.")


def RF05_eliminar_actividad():
    """RF05: Elimina un registro previa confirmación."""
    print("\n--- ELIMINAR ACTIVIDAD ---")
    id_act = leer_entero_positivo("Ingrese el ID de la actividad a eliminar: ")
    act = obtener_actividad_por_id(id_act)
    
    if act is None:
        print(f"  [Información] No se encontró actividad con el ID {id_act}.")
        return

    confirmar = input(f"¿Está seguro de eliminar '{act['nombre']}' (ID {act['id']})? (s/n): ").strip().lower()
    if confirmar == 's':
        actividades.remove(act)
        print("  [Éxito] La actividad ha sido eliminada.")
    else:
        print("  Operación de eliminación cancelada.")


def RF06_calcular_coste_total():
    """RF06: Suma de los costos con acumulador manual explícito."""
    costo_total = 0.0
    for act in actividades:
        costo_total += act["costo"]
    return costo_total


def RF07_mostrar_estadisticas():
    """RF07: Calcula métricas completas recorriendo la lista con ciclos manuales."""
    print("\n========================================")
    print("      ESTADÍSTICAS DE CAPACITACIÓN      ")
    print("========================================")
    
    total_actividades = len(actividades)
    if total_actividades == 0:
        print("  No hay actividades registradas para calcular estadísticas.")
        print("========================================")
        return

    # Variables acumuladoras y contadoras explícitas
    costo_total = 0.0
    total_participantes = 0
    count_mayor_500 = 0
    count_mayor_igual_500 = 0
    
    actividad_mas_cara = None
    actividad_mas_economica = None

    for act in actividades:
        c = act["costo"]
        p = act["participantes"]
        
        costo_total += c
        total_participantes += p
        
        if c > 500.0:
            count_mayor_500 += 1
        if c >= 500.0:
            count_mayor_igual_500 += 1
            
        # Extremos manuales
        if actividad_mas_cara is None or c > actividad_mas_cara["costo"]:
            actividad_mas_cara = act
            
        if actividad_mas_economica is None or c < actividad_mas_economica["costo"]:
            actividad_mas_economica = act

    costo_promedio_actividad = costo_total / total_actividades
    costo_promedio_participante = (costo_total / total_participantes) if total_participantes > 0 else 0.0

    print(f"Total de actividades:                  {total_actividades}")
    print(f"Coste total comprometido:              S/ {costo_total:.2f}")
    print(f"Coste promedio por actividad:          S/ {costo_promedio_actividad:.2f}")
    print(f"Actividad de mayor coste:              {actividad_mas_cara['nombre']} (S/ {actividad_mas_cara['costo']:.2f})")
    print(f"Actividad de menor coste:              {actividad_mas_economica['nombre']} (S/ {actividad_mas_economica['costo']:.2f})")
    print(f"Actividades con coste > S/ 500:         {count_mayor_500}")
    print(f"Actividades con coste >= S/ 500:        {count_mayor_igual_500}")
    print(f"Total de participantes registrados:    {total_participantes}")
    print(f"Coste promedio por participante:       S/ {costo_promedio_participante:.2f}")
    print("========================================")


def RF08_filtrar_actividades():
    """RF08: Filtra las actividades según múltiples criterios."""
    print("\n--- OBTENER FILTROS DE ACTIVIDADES ---")
    print("1. Costo superior a un importe")
    print("2. Costo inferior a un importe")
    print("3. Costo dentro de un intervalo")
    print("4. Por categoría determinada")
    print("5. Participantes mayor o igual que un valor")
    
    opcion = input("Seleccione criterio (1-5): ").strip()
    coincidencias = []

    if opcion == "1":
        limite = leer_float_positivo("Ingrese el costo mínimo: ", incluir_cero=True)
        for act in actividades:
            if act["costo"] > limite:
                coincidencias.append(act)

    elif opcion == "2":
        limite = leer_float_positivo("Ingrese el costo máximo: ", incluir_cero=True)
        for act in actividades:
            if act["costo"] < limite:
                coincidencias.append(act)

    elif opcion == "3":
        min_i = leer_float_positivo("Ingrese el costo inferior del intervalo: ", incluir_cero=True)
        max_i = leer_float_positivo("Ingrese el costo superior del intervalo: ", incluir_cero=True)
        for act in actividades:
            if min_i <= act["costo"] <= max_i:
                coincidencias.append(act)

    elif opcion == "4":
        cat_buscar = leer_texto_no_vacio("Ingrese la categoría a buscar: ").lower()
        for act in actividades:
            if act["categoria"].lower() == cat_buscar:
                coincidencias.append(act)

    elif opcion == "5":
        min_p = leer_entero_positivo("Ingrese número de participantes mínimo: ")
        for act in actividades:
            if act["participantes"] >= min_p:
                coincidencias.append(act)
    else:
        print("  Opción de filtro inválida.")
        return

    print(f"\nResultados del filtro ({len(coincidencias)} encontradas):")
    RF01_mostrar_actividades(coincidencias)


def RF09_ordenar_actividades_manualmente():
    """RF09: Ordena manualmente la lista por costo con el algoritmo Bubble Sort sin sort()."""
    if not actividades:
        print("\n  No hay actividades para ordenar.")
        return

    print("\n--- ORDENAR ACTIVIDADES MANUAMENTE POR COSTO ---")
    print("1. Orden Ascendente (Menor a Mayor)")
    print("2. Orden Descendente (Mayor a Menor)")
    sentido = input("Seleccione el sentido (1-2): ").strip()

    if sentido not in ["1", "2"]:
        print("  Opción no válida.")
        return

    # Copia manual superficial para preservar la lista original intacta
    copia_ordenada = []
    for item in actividades:
        copia_ordenada.append(dict(item))

    n = len(copia_ordenada)
    # Algoritmo de Ordenación Burbuja (Bubble Sort)
    for i in range(n):
        for j in range(0, n - i - 1):
            debe_intercambiar = False
            if sentido == "1":  # Ascendente
                if copia_ordenada[j]["costo"] > copia_ordenada[j + 1]["costo"]:
                    debe_intercambiar = True
            elif sentido == "2":  # Descendente
                if copia_ordenada[j]["costo"] < copia_ordenada[j + 1]["costo"]:
                    debe_intercambiar = True

            if debe_intercambiar:
                temp = copia_ordenada[j]
                copia_ordenada[j] = copia_ordenada[j + 1]
                copia_ordenada[j + 1] = temp

    print("\nListado ordenado resultante (lista original no modificada):")
    RF01_mostrar_actividades(copia_ordenada)


def RF10_mostrar_informe_presupuestario():
    """RF10: Muestra el informe de ejecución del presupuesto y su estado."""
    print("\n========================================")
    print("        INFORME PRESUPUESTARIO          ")
    print("========================================")

    costo_total = RF06_calcular_coste_total()

    print(f"Presupuesto disponible:     S/ {presupuesto_disponible:.2f}")
    print(f"Coste total comprometido:   S/ {costo_total:.2f}")

    if presupuesto_disponible <= 0:
        print("----------------------------------------")
        print("Estado: Presupuesto no válido")
        print("========================================")
        return

    saldo_restante = presupuesto_disponible - costo_total
    porcentaje_uso = (costo_total / presupuesto_disponible) * 100.0

    print(f"Saldo restante:             S/ {saldo_restante:.2f}")
    print(f"Porcentaje utilizado:       {porcentaje_uso:.2f} %")
    print("----------------------------------------")

    if costo_total < presupuesto_disponible:
        print("Estado: Dentro del presupuesto")
    elif costo_total == presupuesto_disponible:
        print("Estado: Presupuesto utilizado al 100 %")
    else:
        exceso = costo_total - presupuesto_disponible
        print(f"Estado: Exceso presupuestario (Excedido en S/ {exceso:.2f})")

    print("========================================")


def RF11_cambiar_presupuesto():
    """RF11: Actualiza el valor global del presupuesto disponible."""
    global presupuesto_disponible
    print("\n--- CAMBIAR PRESUPUESTO DISPONIBLE ---")
    print(f"Presupuesto actual: S/ {presupuesto_disponible:.2f}")
    
    nuevo_presupuesto = leer_float_positivo("Ingrese nuevo presupuesto disponible (S/): ")
    presupuesto_disponible = nuevo_presupuesto
    print(f"  [Éxito] El presupuesto disponible se actualizó a S/ {presupuesto_disponible:.2f}.")


# --- BUCLE PRINCIPAL DE LA APLICACIÓN ---

def menu_principal():
    """Despliega el menú interactivo con las 12 opciones requeridas."""
    while True:
        print("\n================================================")
        print(" GESTOR DE PRESUPUESTOS DE CAPACITACIÓN (R02)")
        print("================================================")
        print(" 1. Mostrar todas las actividades")
        print(" 2. Registrar una actividad")
        print(" 3. Buscar una actividad por ID")
        print(" 4. Actualizar una actividad")
        print(" 5. Eliminar una actividad")
        print(" 6. Calcular el coste total")
        print(" 7. Mostrar estadísticas")
        print(" 8. Filtrar actividades")
        print(" 9. Ordenar actividades manualmente por coste")
        print("10. Mostrar el informe presupuestario")
        print("11. Cambiar el presupuesto disponible")
        print("12. Salir")
        print("================================================")

        opcion = input("Seleccione una opción (1-12): ").strip()

        if opcion == "1":
            RF01_mostrar_actividades()
        elif opcion == "2":
            RF02_registrar_actividad()
        elif opcion == "3":
            RF03_buscar_actividad()
        elif opcion == "4":
            RF04_actualizar_actividad()
        elif opcion == "5":
            RF05_eliminar_actividad()
        elif opcion == "6":
            total = RF06_calcular_coste_total()
            print(f"\n  [Resultado] El coste total acumulado de las actividades es: S/ {total:.2f}")
        elif opcion == "7":
            RF07_mostrar_estadisticas()
        elif opcion == "8":
            RF08_filtrar_actividades()
        elif opcion == "9":
            RF09_ordenar_actividades_manualmente()
        elif opcion == "10":
            RF10_mostrar_informe_presupuestario()
        elif opcion == "11":
            RF11_cambiar_presupuesto()
        elif opcion == "12":
            print("\n  Gracias por utilizar el Gestor de Presupuestos de Capacitación. ¡Hasta pronto!")
            break
        else:
            print("\n  [Error] Opción no válida. Ingrese un número del 1 al 12.")


if __name__ == "__main__":
    menu_principal()