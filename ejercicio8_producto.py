# ============================================================
# EJERCICIO 8 - Producto
# ============================================================

class Producto:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    def aumentar_stock(self, cantidad):
        if cantidad > 0:
            self._stock += cantidad
            print(f"Stock aumentado en {cantidad}. Stock actual: {self._stock}")
        else:
            print("La cantidad a aumentar debe ser mayor a 0.")

    def disminuir_stock(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a disminuir debe ser mayor a 0.")
        elif cantidad > self._stock:
            print(f"No hay suficiente stock. Stock disponible: {self._stock}")
        else:
            self._stock -= cantidad
            print(f"Stock reducido en {cantidad}. Stock actual: {self._stock}")

    def mostrar_informacion(self):
        return (f"Producto: {self._nombre} | "
                f"Precio: ${self._precio:.2f} | "
                f"Stock: {self._stock}")

    # Getters
    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio

    def get_stock(self):
        return self._stock

    # Setters
    def set_nombre(self, nombre):
        if nombre.strip():
            self._nombre = nombre
        else:
            print("El nombre no puede estar vacío.")

    def set_precio(self, precio):
        if precio >= 0:
            self._precio = precio
        else:
            print("El precio no puede ser negativo.")

    def set_stock(self, stock):
        if stock >= 0:
            self._stock = stock
        else:
            print("El stock no puede ser negativo.")


if __name__ == "__main__":
    producto = Producto("Auriculares Bluetooth", 89.99, 50)
    print(producto.mostrar_informacion())
    producto.aumentar_stock(20)
    producto.disminuir_stock(10)
    producto.disminuir_stock(100)  # Intento inválido
    print(producto.mostrar_informacion())
