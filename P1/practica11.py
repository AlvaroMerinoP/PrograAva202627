import re
from datetime import datetime


def anonymize_report(report: str) -> str:
    """Sustituye los datos personales y calcula la edad en urgencias."""
    # \d significa dígito.
    # {1,2} permite uno o dos dígitos; {4} exige cuatro.
    date_pattern = re.compile(r"\b\d{1,2}/\d{1,2}/\d{4}\b")

    # Los paréntesis guardan la fecha para recuperarla con group(1).
    birth_pattern = re.compile(
        r"^Fecha de nacimiento:\s*(\d{1,2}/\d{1,2}/\d{4})[ \t]*$",
        re.MULTILINE
    )

    visit_pattern = re.compile(
        r"^(\d{1,2}/\d{1,2}/\d{4})[ \t]+(?:Dr\.|Dra\.)",
        re.MULTILINE
    )

    birth_match = birth_pattern.search(report)
    visit_match = visit_pattern.search(report)

    if birth_match is None or visit_match is None:
        raise ValueError("Falta la fecha de nacimiento o la de urgencias.")

    # Convertimos las cadenas en fechas para comparar sus componentes.
    birth = datetime.strptime(birth_match.group(1), "%d/%m/%Y")
    visit = datetime.strptime(visit_match.group(1), "%d/%m/%Y")

    age = visit.year - birth.year

    # Si todavía no había cumplido años, restamos uno.
    if (visit.month, visit.day) < (birth.month, birth.day):
        age -= 1

    report = birth_pattern.sub(f"Edad: {age}", report)

    # ^ indica el principio de una línea y $ su final.
    report = re.sub(
        r"^Nombre:[^\n]*$",
        "Nombre: PACIENTE",
        report,
        flags=re.MULTILINE
    )

    # Sustituimos desde Dr. o Dra. hasta el final de esa línea.
    report = re.sub(
        r"\b(?:Dr\.|Dra\.)[^\n]*",
        "MEDICO",
        report
    )

    # Finalmente ocultamos las fechas restantes.
    report = date_pattern.sub("FECHA", report)

    return report


def main() -> None:
    """Prueba la anonimización con el ejemplo y otra fecha de urgencias."""
    report = """Informe clínico de Urgencias
Nombre: Juan Pérez López
Género: Hombre
Fecha de nacimiento: 12/05/1980
Motivo de consulta: dolor abdominal
12/05/2023 Dr. Ramírez
Tratamiento: reposo y analgésicos"""

    print(anonymize_report(report))

    # El día anterior a su cumpleaños todavía tenía 42 años.
    print("\nCaso adicional:")
    other_report = report.replace("12/05/2023", "11/05/2023")
    print(anonymize_report(other_report))


if __name__ == "__main__":
    main()

