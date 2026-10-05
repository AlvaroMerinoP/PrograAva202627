# P1

## Preguntas y respuestas sobre las prácticas

### 3. ¿Cómo representa una lista los coeficientes de un polinomio?

La posición de cada coeficiente indica su exponente. Por ejemplo, `[4.0, 1.0, 0.0, 2.0]` representa `4.0 + x + 2.0x**3`. Para escribirlo de mayor a menor exponente, se recorre la lista desde el final y se omiten los coeficientes que valen cero.

### 4. ¿Qué diferencia hay entre `==` e `is`?

`==` compara los valores de dos objetos. `is` comprueba si ambos son el mismo objeto en memoria. Dos cadenas pueden tener el mismo contenido sin ser el mismo objeto. El ejercicio 10 utiliza `is` para comparar los objetos guardados en dos posiciones de la lista.

### 5. ¿Cuándo se ejecuta el `else` de un bucle `for`?

Se ejecuta si el bucle termina sin ejecutar un `break`, incluso si la lista está vacía. En el ejercicio 10 permite indicar que ninguna cadena tiene más de diez caracteres. En el 12 permite crear un nuevo grupo cuando no se ha encontrado uno de anagramas adecuado.

### 6. ¿Por qué hay que calcular la edad antes de ocultar las fechas del informe?

Porque se necesitan la fecha de nacimiento y la fecha de urgencias originales. Primero se restan los años y, si el cumpleaños todavía no había llegado en la fecha de urgencias, se resta uno más. Después se sustituye la fecha de nacimiento por la edad y las fechas restantes por `FECHA`.

### 7. ¿Cómo se comprueba si dos palabras son anagramas?

En el ejercicio 12 se convierten ambas cadenas a minúsculas, se eliminan los espacios y se ordenan sus letras con `sorted()`. Si las listas resultantes son iguales, son anagramas. Así, `"Roma"` y `"amor"` coinciden, pero `"aab"` y `"abb"` no, porque cada letra debe aparecer el mismo número de veces.
