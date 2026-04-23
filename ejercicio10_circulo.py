# ============================================================
# EJERCICIO 10 - Circulo
# ============================================================

import math

class Circulo:
    def __init__(self, radio):
        if radio < 0:
            raise ValueError("El radio no puede ser negativo.")
        self._radio = radio

    def calcular_area(self):
        return round(math.pi * self._radio ** 2, 4)

    def calcular_circunferencia(self):
        return round(2 * math.pi * self._radio, 4)

    def mostrar_informacion(self):
        return (f"Círculo | Radio: {self._radio} | "
                f"Área: {self.calcular_area()} | "
                f"Circunferencia: {self.calcular_circunferencia()}")

    # Getter
    def get_radio(self):
        return self._radio

    # Setter con validación
    def set_radio(self, radio):
        if radio >= 0:
            self._radio = radio
        else:
            print("El radio no puede ser negativo.")


if __name__ == "__main__":
    circulo = Circulo(5)
    print(circulo.mostrar_informacion())
    circulo.set_radio(10)
    print("Después de cambiar el radio:")
    print(circulo.mostrar_informacion())
    circulo.set_radio(-3)  # Intento inválido

    # Intento de crear un círculo con radio negativo
    try:
        circulo_invalido = Circulo(-1)
    except ValueError as e:
        print(f"Error al crear el círculo: {e}")
