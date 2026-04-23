# ============================================================
# EJERCICIO 9 - Juego
# ============================================================

class Juego:
    def __init__(self, nombre, genero, precio):
        self._nombre = nombre
        self._genero = genero
        self._precio = precio

    def mostrar_informacion(self):
        return (f"Juego: {self._nombre} | "
                f"Género: {self._genero} | "
                f"Precio: ${self._precio:.2f}")

    def esta_en_oferta(self, precio_limite):
        if precio_limite < 0:
            print("El precio límite no puede ser negativo.")
            return False
        return self._precio < precio_limite

    # Getters
    def get_nombre(self):
        return self._nombre

    def get_genero(self):
        return self._genero

    def get_precio(self):
        return self._precio

    # Setters
    def set_nombre(self, nombre):
        if nombre.strip():
            self._nombre = nombre
        else:
            print("El nombre no puede estar vacío.")

    def set_genero(self, genero):
        if genero.strip():
            self._genero = genero
        else:
            print("El género no puede estar vacío.")

    def set_precio(self, precio):
        if precio >= 0:
            self._precio = precio
        else:
            print("El precio no puede ser negativo.")


if __name__ == "__main__":
    juego = Juego("The Witcher 3", "RPG", 19.99)
    print(juego.mostrar_informacion())
    limite = 25.00
    en_oferta = juego.esta_en_oferta(limite)
    print(f"¿Está en oferta por menos de ${limite}? {'Sí' if en_oferta else 'No'}")
    juego.set_precio(30.00)
    en_oferta = juego.esta_en_oferta(limite)
    print(f"Después de actualizar el precio:")
    print(f"¿Está en oferta por menos de ${limite}? {'Sí' if en_oferta else 'No'}")
