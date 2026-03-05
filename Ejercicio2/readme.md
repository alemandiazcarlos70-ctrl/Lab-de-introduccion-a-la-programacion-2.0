## 🧮 Explicación detallada de la calculadora

### 📌 Descripción general

La calculadora fue desarrollada en lenguaje **C++** con el objetivo de realizar operaciones matemáticas básicas como suma, resta, multiplicación y división. El programa funciona mediante un menú interactivo en la consola, donde el usuario selecciona la operación deseada, ingresa dos números y obtiene el resultado correspondiente.

---

## ⚙️ Proceso de creación

### 1️⃣ Inclusión de librerías

Se utiliza la librería estándar `<iostream>` para permitir la entrada y salida de datos a través de la consola.

---

### 2️⃣ Función principal `main()`

La ejecución del programa comienza en la función `main()`, la cual es el punto de entrada principal de todo programa en C++.

---

### 3️⃣ Declaración de variables

Se declaran variables para almacenar la opción del usuario, los números ingresados y el resultado de la operación.

- `int opcion` almacena la opción del menú.
- `float num1, num2` almacenan los números a operar.
- `float resultado` guarda el resultado final.

---

### 4️⃣ Menú de opciones

Se muestra un menú en pantalla que permite al usuario seleccionar la operación matemática que desea realizar.

Las opciones disponibles son:
- Suma
- Resta
- Multiplicación
- División

---

### 5️⃣ Entrada de datos

El programa solicita al usuario:
1. Seleccionar una opción del menú.
2. Ingresar el primer número.
3. Ingresar el segundo número.

Estos datos se capturan utilizando la instrucción `cin`.

---

### 6️⃣ Uso de la estructura `switch`

La estructura de control `switch` permite ejecutar una operación específica dependiendo de la opción elegida por el usuario. Cada `case` representa una operación matemática diferente.

---

### 7️⃣ Operaciones matemáticas

- **Suma:** Se realiza la adición de ambos números.
- **Resta:** Se calcula la diferencia entre los números ingresados.
- **Multiplicación:** Se multiplican los valores proporcionados.
- **División:** Antes de realizar la operación, se valida que el segundo número no sea cero para evitar errores.

---

### 8️⃣ Validación de errores

El programa incluye una validación para evitar la división entre cero y un mensaje de error en caso de que el usuario seleccione una opción no válida.

---

### 9️⃣ Finalización del programa

El programa finaliza su ejecución correctamente al retornar el valor `0`, indicando que no ocurrieron errores durante su ejecución.

---

## 🧠 Conceptos utilizados

- Entrada y salida de datos (`cin`, `cout`)
- Variables y tipos de datos (`int`, `float`)
- Estructuras de control (`switch`, `if`)
- Operaciones aritméticas básicas
- Validación de errores
- Programación estructurada

---

## ✅ Conclusión

Este ejercicio permite reforzar los conceptos básicos de programación en C++, especialmente el uso de estructuras de control, manejo de datos por consola y operaciones matemáticas. Es una base sólida para el desarrollo de programas más complejos.
