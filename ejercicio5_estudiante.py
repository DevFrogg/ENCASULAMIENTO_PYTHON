# ============================================================
# EJERCICIO 5 - Estudiante
# ============================================================

class Estudiante:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        self._notas = []

    def agregar_nota(self, nota):
        if 0 <= nota <= 10:
            self._notas.append(nota)
            print(f"Nota {nota} agregada correctamente.")
        else:
            print("La nota debe estar entre 0 y 10.")

    def calcular_promedio(self):
        if not self._notas:
            return "No hay notas registradas."
        promedio = sum(self._notas) / len(self._notas)
        return round(promedio, 2)

    def mostrar_informacion(self):
        return (f"Estudiante: {self._nombre} | Edad: {self._edad} | "
                f"Notas: {self._notas} | Promedio: {self.calcular_promedio()}")

    # Getters
    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad

    def get_notas(self):
        return self._notas.copy()  # Devuelve copia para proteger la lista original

    # Setters
    def set_nombre(self, nombre):
        if nombre.strip():
            self._nombre = nombre
        else:
            print("El nombre no puede estar vacío.")

    def set_edad(self, edad):
        if 0 < edad < 120:
            self._edad = edad
        else:
            print("Edad no válida.")


if __name__ == "__main__":
    estudiante = Estudiante("Carlos López", 20)
    estudiante.agregar_nota(8)
    estudiante.agregar_nota(7.5)
    estudiante.agregar_nota(9)
    estudiante.agregar_nota(11)  # Nota inválida
    print(estudiante.mostrar_informacion())
