def is_leap_year(year):
    """
    Devuelve True si el año es bisiesto y False en caso contrario.
    """
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def leap_years_between(start, end):
    """
    Devuelve una lista con los años bisiestos entre start y end.
    """
    leap_years = []
    for year in range(start, end + 1):
        if is_leap_year(year):
            leap_years.append(year)
    return leap_years

def explain_leap_year(year):
    """
    Devuelve una cadena que indica si el año es bisiesto y por qué
    """
    if year % 400 == 0:
        return f"{year} es bisiesto: es divisible entre 400."

    elif year % 100 == 0:
        return f"{year} no es bisiesto: es divisible entre 100 pero no entre 400."

    elif year % 4 == 0:
        return f"{year} es bisiesto: es divisible entre 4 y no entre 100."

    else:
        return f"{year} no es bisiesto: no es divisible entre 4."

def main() -> None:
    """
    Solicita un año y muestra la explicación correspondiente.
    """
    year = int(input("Año: "))

    if year < 1582:
        print("El calendario gregoriano se estableció en 1582.")
    else:
        print(explain_leap_year(year))

if __name__ == "__main__":
    main()
