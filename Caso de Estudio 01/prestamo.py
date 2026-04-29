class Prestamo:
    """Clase que representa un préstamo."""

    def __init__(self, libro, estudiante, fecha_prestamo, fecha_devolucion):
        self._libro = libro
        self._estudiante = estudiante
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion
        self._activo = True

    @property
    def libro(self):
        return self._libro

    @property
    def estudiante(self):
        return self._estudiante

    @property
    def activo(self):
        return self._activo

    def registrar_devolucion(self):
        self._activo = False
        self._libro.devolver()

    def __str__(self):
        estado = "ACTIVO" if self._activo else "DEVUELTO"
        return f"{self._libro.titulo} → {self._estudiante.nombre} ({estado})"