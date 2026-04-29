from faker import Faker
from libro import Libro
from estudiante import Estudiante
from biblioteca import Biblioteca

fake = Faker("es_ES")


def main():
    print("==============================================")
    print(" SISTEMA DE GESTIÓN DE BIBLIOTECA UNEMI")
    print("==============================================")

    print("\nIntegrantes del grupo:")
    print("Andres Jesús Reyes Ayala")
    print("Marcos David Medina Lopez")
    print("Javier Israel Rodriguez Meza")
    print("Roddy Antonio Marcos Franco")
    print("Benjamin Jose Cabrera Yepe")

    biblioteca = Biblioteca("Biblioteca Grupo UNEMI")

    print("\n--- REGISTRO DE LIBROS ALEATORIOS ---")
    for i in range(1, 6):
        titulo = fake.word().title()
        autor = fake.name()
        libro = Libro(f"00{i}", titulo, autor)
        biblioteca.registrar_libro(libro)

    print("\n--- REGISTRO DE ESTUDIANTES ALEATORIOS ---")
    estudiantes_generados = []

    for i in range(1, 4):
        estudiante = Estudiante(
            str(fake.random_number(digits=10)),
            fake.first_name(),
            fake.last_name(),
            "Ingeniería en Sistemas"
        )
        estudiantes_generados.append(estudiante)
        biblioteca.registrar_estudiante(estudiante)

    print("\n--- PRÉSTAMOS REALIZADOS ---")
    for i in range(2):
        libro = biblioteca._libros[i]
        estudiante = estudiantes_generados[i]
        print(
            biblioteca.prestar_libro(
                libro.isbn,
                estudiante.cedula,
                "26/04/2026",
                "03/05/2026"
            )
        )

    print("\n--- DEVOLUCIÓN ---")
    print(
        biblioteca.devolver_libro(
            biblioteca._libros[0].isbn,
            estudiantes_generados[0].cedula
        )
    )

    print("\n--- VALIDACIÓN DE DISPONIBILIDAD ---")
    print(
        biblioteca.prestar_libro(
            biblioteca._libros[1].isbn,
            estudiantes_generados[2].cedula,
            "26/04/2026",
            "03/05/2026"
        )
    )


if __name__ == "__main__":
    main()