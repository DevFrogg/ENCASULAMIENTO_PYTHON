# ============================================================
# EJERCICIO 6 - Rectángulo
# ============================================================

class Rectangulo:
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    def calcular_area(self):
        return self._base * self._altura

    def calcular_perimetro(self):
        return 2 * (self._base + self._altura)

    def mostrar_informacion(self):
        return (f"Rectángulo | Base: {self._base} | Altura: {self._altura} | "
                f"Área: {self.calcular_area()} | Perímetro: {self.calcular_perimetro()}")

    # Getters
    def get_base(self):
        return self._base

    def get_altura(self):
        return self._altura

    # Setters
    def set_base(self, base):
        if base > 0:
            self._base = base
        else:
            print("La base debe ser mayor a 0.")

    def set_altura(self, altura):
        if altura > 0:
            self._altura = altura
        else:
            print("La altura debe ser mayor a 0.")


if __name__ == "__main__":
    rect = Rectangulo(5, 3)
    print(rect.mostrar_informacion())
    rect.set_base(10)
    rect.set_altura(4)
    print("Después de modificar las dimensiones:")
    print(rect.mostrar_informacion())
