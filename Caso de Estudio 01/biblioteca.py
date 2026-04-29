from prestamo import Prestamo


class Biblioteca:
    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = []
        self._estudiantes = []
        self._prestamos = []

    def registrar_libro(self, libro):
        self._libros.append(libro)
        print(f"Libro registrado: {libro.titulo}")

    def registrar_estudiante(self, estudiante):
        self._estudiantes.append(estudiante)
        print(f"Estudiante registrado: {estudiante.nombre}")

    def _buscar_libro(self, isbn):
        for libro in self._libros:
            if libro.isbn == isbn:
                return libro
        return None

    def _buscar_estudiante(self, cedula):
        for estudiante in self._estudiantes:
            if estudiante.cedula == cedula:
                return estudiante
        return None

    def prestar_libro(self, isbn, cedula, fecha_prestamo, fecha_devolucion):
        libro = self._buscar_libro(isbn)
        estudiante = self._buscar_estudiante(cedula)

        if libro and estudiante and libro.disponible:
            libro.prestar()
            prestamo = Prestamo(libro, estudiante, fecha_prestamo, fecha_devolucion)
            self._prestamos.append(prestamo)
            return f"Préstamo realizado: {libro.titulo}"

        return "No se pudo realizar el préstamo"

    def devolver_libro(self, isbn, cedula):
        for prestamo in self._prestamos:
            if prestamo.libro.isbn == isbn and prestamo.estudiante.cedula == cedula and prestamo.activo:
                prestamo.registrar_devolucion()
                return "Libro devuelto"
        return "No encontrado"