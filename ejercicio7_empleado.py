# ============================================================
# EJERCICIO 7 - Empleado
# ============================================================

class Empleado:
    def __init__(self, nombre, salario, departamento):
        self._nombre = nombre
        self._salario = salario
        self._departamento = departamento

    def aumentar_salario(self, porcentaje):
        if porcentaje > 0:
            aumento = self._salario * (porcentaje / 100)
            self._salario += aumento
            print(f"Salario actualizado con un aumento del {porcentaje}%.")
        else:
            print("El porcentaje de aumento debe ser mayor a 0.")

    def mostrar_informacion(self):
        return (f"Empleado: {self._nombre} | "
                f"Departamento: {self._departamento} | "
                f"Salario: ${self._salario:.2f}")

    # Getters
    def get_nombre(self):
        return self._nombre

    def get_salario(self):
        return self._salario

    def get_departamento(self):
        return self._departamento

    # Setters
    def set_nombre(self, nombre):
        if nombre.strip():
            self._nombre = nombre
        else:
            print("El nombre no puede estar vacío.")

    def set_salario(self, salario):
        if salario >= 0:
            self._salario = salario
        else:
            print("El salario no puede ser negativo.")

    def set_departamento(self, departamento):
        if departamento.strip():
            self._departamento = departamento
        else:
            print("El departamento no puede estar vacío.")


if __name__ == "__main__":
    empleado = Empleado("María Torres", 50000, "Tecnología")
    print(empleado.mostrar_informacion())
    empleado.aumentar_salario(15)
    print(empleado.mostrar_informacion())
    empleado.aumentar_salario(-5)  # Intento inválido
