# Práctica 3: matrices con NumPy

Implementación del enunciado de `Practica3.pdf` en [matriz.py](matriz.py).
Requiere Python 3.10 o posterior y NumPy.

## Ejecución

```sh
python3 -m pip install -r requirements.txt
python3 matriz.py
```

El menú permite crear una matriz 1D, 2D o identidad, introducir sus valores,
mostrarla y acceder al submenú de suma y resta. En cada operación se solicitan
las dimensiones y los valores de una segunda matriz. La resta calcula
`matriz actual - segunda matriz`; los resultados no reemplazan la matriz actual.

Las matrices 1D se almacenan como arrays de forma `(1, n)`, reutilizando la
creación 2D, como pide el enunciado. Todos los elementos usan `np.float32`.
Las dimensiones deben ser enteros positivos y las matrices deben tener
exactamente las mismas dimensiones para operar; no se permite el broadcasting
de NumPy. Los atributos de instancia son protegidos: `_matriz`, `_nfil` y `_ncol`.

Las entradas numéricas incorrectas se vuelven a solicitar. Los decimales admiten
punto o coma; se rechazan valores no finitos y valores fuera del rango float32.
Si las dimensiones son inválidas, se informa del error y se conserva la matriz
anterior. La opción 7, Ctrl+C o el fin de la entrada terminan el programa.

## UML

[MatrizFloat.puml](MatrizFloat.puml) representa la clase en PlantUML, uno de los
formatos admitidos por la práctica 2. Incluye atributos, tipos, visibilidad y
métodos. `matriz_identidad` es de clase; `mismas_dimensiones` es estático; el resto
son métodos de instancia.

## Comprobación

```sh
python3 -m unittest discover -s tests -v
```

Las pruebas verifican creación, tipos, identidad, suma y resta sin modificar
operandos, validación de dimensiones y entradas, y navegación por los menús.
