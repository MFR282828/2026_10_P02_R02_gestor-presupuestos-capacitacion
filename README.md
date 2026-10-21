# Gestor de Presupuestos de Capacitación

Aplicación de consola (CLI) desarrollada en Python para gestionar las actividades de capacitación del área de Recursos Humanos. Permite registrar, consultar, actualizar, eliminar, filtrar, ordenar manualmente y analizar los costos frente a un presupuesto disponible.

---

## Objetivo de aprendizaje

Consolidar los conceptos y herramientas fundamentales del **Principio 2: Control de flujo y estructuras de datos básicas**:
- Manipulación de estructuras complejas básicas (listas de diccionarios).
- Bucles iterativos (`while`, `for`) y sentencias condicionales (`if`, `elif`, `else`).
- Algoritmos manuales de búsqueda, acumulación, conteo y cálculo de extremos (mínimos y máximos).
- Algoritmo de ordenación manual (Burbuja / Bubble Sort) sin recurrir a funciones integradas como `sort()` o `sorted()`.
- Menú interactivo con validación activa de tipos y entradas para evitar bloqueos del programa.

---

## Mapa de Principios de la Saga Python 2026

- [X] **Principio 1. Fundamentos del lenguaje Python**
- [X] **Principio 2. Control de flujo y estructuras de datos básicas**
- [ ] **Principio 3. Funciones, parámetros y alcance de variables**
- [ ] **Principio 4. Manejo de errores y excepciones**
- [ ] **Principio 5. Comprensiones y código idiomático de Python**
- [ ] **Principio 6. Calidad del código y convenciones profesionales**
- [ ] **Principio 7. Programación Orientada a Objetos (POO)**
- [ ] **Principio 8. Complejidad algorítmica y análisis de eficiencia**
- [ ] **Principio 9. Módulos, paquetes y reutilización de código**
- [ ] **Principio 10. PIP, entornos virtuales y dependencias**
- [ ] **Principio 11. Aplicaciones CRUD y persistencia de datos**
- [ ] **Principio 12. Testing y validación automatizada**
- [ ] **Principio 13. Estadística computacional, simulación y programación dinámica**
- [ ] **Principio 14. Arquitectura de proyectos y distribución de paquetes**
- [ ] **Principio 15. Principios SOLID y patrones de diseño**

---

## Funcionalidades principales

1. **Mostrar actividades:** Listado organizado en tabla.
2. **Registrar actividad:** Asignación automática de ID y verificación de nombres duplicados.
3. **Buscar por ID:** Consulta detallada de datos.
4. **Actualizar actividad:** Modificación selectiva de campos.
5. **Eliminar actividad:** Remoción previa confirmación.
6. **Calcular coste total:** Acumulador explícito de importes.
7. **Estadísticas avanzadas:** Métricas completas, promedios y búsqueda manual de valores extremos (mayor y menor coste).
8. **Filtrado dinámico:** Filtros por rangos de costo, categorías y número de participantes.
9. **Ordenación manual:** Ordenamiento por costo ascendente o descendente mediante Bubble Sort.
10. **Informe presupuestario:** Análisis de ejecución, porcentaje utilizado, saldo y estado del presupuesto.
11. **Gestión de presupuesto:** Modificación del saldo disponible con validación de importes no negativos.

---

## Tecnologías utilizadas

- **Lenguaje:** Python 3 (Biblioteca estándar exclusivamente).
- **Entorno de desarrollo:** VS Code / Terminal PowerShell.
- **Control de versiones:** Git & GitHub.

---

## Estructura del repositorio

```text
2026_10_P02_R02_gestor-presupuestos-capacitacion/
├── .gitignore
├── main.py
└── README.md