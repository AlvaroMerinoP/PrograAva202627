# Práctica 4: registro diario de una empresa

Solución del enunciado de [Practica4.pdf](Practica4.pdf), con herencia,
polimorfismo, propiedades y métodos mágicos. Requiere Python 3.10 o posterior;
utiliza únicamente la biblioteca estándar.

## Ejecución

Desde esta carpeta:

```sh
python3 main.py
```

El menú contiene las ocho opciones del PDF:

1. Introducir empleado: solicita nombre, edad, hora de nacimiento, categoría
   y antigüedad, y lo añade al registro.
2. Introducir cliente: solicita nombre, edad, hora de nacimiento y DNI.
3. Buscar por nombre (y edad): muestra todas las coincidencias e indica su tipo.
4. Mostrar registro diario: muestra empleados y clientes con todos sus datos.
5. Mostrar empleados: muestra únicamente los empleados registrados.
6. Visualizar persona por índice: acepta índices desde `0` hasta `len(registro) - 1`.
7. Combinar registros diarios: crea `otro_registro`, solicita exactamente dos
   personas (eligiendo empleado o cliente en cada caso), las añade mediante
   `agregar_persona()` y sustituye el registro actual por `registro + otro_registro`.
8. Salir.

Las horas se introducen como `12:00:00 AM`, `06:30:00 PM` o
`14:30:00 24 HOURS`. La búsqueda compara exactamente nombre y edad, respetando
mayúsculas y minúsculas. Se eliminan los espacios al principio y al final de
los textos. El DNI se trata como una cadena, sin exigir un formato no indicado
en el enunciado.

## Archivos y conceptos

| Archivo | Contenido |
| --- | --- |
| [Time.py](Time.py) | Clase `Time` y función `format_time`, reutilizadas de P2 sin su programa principal. Copia local para ejecutar P4 de forma independiente. |
| [ficha.py](ficha.py) | Clase base `Ficha`: nombre, edad y hora de nacimiento. |
| [empleado.py](empleado.py) | `Empleado(Ficha)`: añade categoría y antigüedad. |
| [cliente.py](cliente.py) | `Cliente(Ficha)`: añade DNI e igualdad por nombre y edad. |
| [registro_diario.py](registro_diario.py) | Registro, visualización polimórfica, filtro de empleados, acceso por índice y suma. |
| [utils.py](utils.py) | `leer_int`, `leer_float`, `leer_cadena` y `crear_menu`, con excepciones. |
| [main.py](main.py) | Menú y funciones para solicitar datos y ejecutar las operaciones. |
| [RegistroDiario.puml](RegistroDiario.puml) | Diagrama UML de clases y relaciones en PlantUML. |
| [tests](tests) | Pruebas con `unittest`. |

Los atributos de las personas son privados (`__nombre`, `__edad`, etc.) y se
consultan o modifican mediante `@property` y sus setters. Las clases derivadas
inicializan la parte común con `super().__init__()` y redefinen `visualizar()`
llamando a `super().visualizar()`. El registro invoca `persona.visualizar()`:
Python selecciona la implementación de cada objeto por polimorfismo.

`Ficha()` crea una hora propia a las **12:00:00 AM**, además de nombre vacío y
edad cero. El argumento `nacio=None` evita compartir una hora mutable entre
fichas creadas por defecto. Se puede proporcionar explícitamente un objeto `Time`.

`Cliente.__eq__` compara solo nombre y edad, aunque cambien DNI u hora.
`RegistroDiario.__getitem__` delega en la lista y permite índices negativos
como Python; la opción 6 del menú exige índices no negativos. `__len__` permite
consultar el tamaño. `__add__` devuelve un registro nuevo, conserva orden y
duplicados y no modifica las listas originales. Las personas siguen siendo los
mismos objetos compartidos. `es_empleado` es estático porque solo examina su
argumento. La propiedad `personas` devuelve una copia de la lista para que las
altas siempre pasen por la validación de `agregar_persona`.

Las anotaciones de listas utilizan `typing.List`, como exige el PDF.

## Validación y errores

Las utilidades de entrada lanzan excepciones en lugar de repetir internamente
la lectura: `ValueError` para texto numérico inválido, cadenas vacías o una
opción fuera de rango; `TypeError` para argumentos de tipos incorrectos.
`leer_float` acepta punto o coma decimal y rechaza infinitos y NaN, aunque no
se necesita para los datos de este menú.

Las edades y antigüedades deben ser enteros no negativos; los setters también
rechazan booleanos. `agregar_persona` solo admite empleados o clientes, y
rechaza incluso una instancia directa de `Ficha`. Los índices fuera de rango
generan `IndexError`.

El menú captura estos errores, informa y vuelve al menú principal. Una entrada
inválida no añade una persona incompleta; si falla la introducción del segundo
registro, tampoco se aplica una combinación parcial. Ctrl+C y el fin de la
entrada terminan el programa. Los datos se conservan en memoria durante la
ejecución.

## Comprobación

```sh
python3 -m unittest discover -s tests -v
```

Las pruebas comprueban los valores por defecto, las propiedades, la herencia,
la igualdad de clientes, el filtrado, los índices, la suma sin modificar los
operandos, las utilidades, las entradas inválidas y un recorrido por las ocho
opciones del menú.
