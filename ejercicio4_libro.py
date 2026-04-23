# ============================================================
# EJERCICIO 4 - Libro
# ============================================================

from datetime import datetime

class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self._titulo = titulo
        self._autor = autor
        self._año_publicacion = año_publicacion

    def descripcion(self):
        return (f"'{self._titulo}' escrito por {self._autor}, "
                f"publicado en {self._año_publicacion}.")

    def es_clasico(self):
        año_actual = datetime.now().year
        return (año_actual - self._año_publicacion) > 50

    def mostrar_informacion(self):
        clasico = "Sí" if self.es_clasico() else "No"
        return f"{self.descripcion()} ¿Es clásico? {clasico}"

    # Getters
    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_año_publicacion(self):
        return self._año_publicacion

    # Setters
    def set_titulo(self, titulo):
        if titulo.strip():
            self._titulo = titulo
        else:
            print("El título no puede estar vacío.")

    def set_autor(self, autor):
        if autor.strip():
            self._autor = autor
        else:
            print("El autor no puede estar vacío.")

    def set_año_publicacion(self, año):
        if 0 < año <= datetime.now().year:
            self._año_publicacion = año
        else:
            print("Año de publicación no válido.")


if __name__ == "__main__":
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    libro2 = Libro("El problema de los tres cuerpos", "Liu Cixin", 2008)
    print(libro1.mostrar_informacion())
    print(libro2.mostrar_informacion())
