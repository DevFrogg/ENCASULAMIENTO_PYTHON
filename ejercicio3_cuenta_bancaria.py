# ============================================================
# EJERCICIO 3 - CuentaBancaria
# ============================================================

class CuentaBancaria:
    def __init__(self, titular, saldo, numero_cuenta):
        self._titular = titular
        self._saldo = saldo
        self._numero_cuenta = numero_cuenta

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${self._saldo:.2f}")
        else:
            print("El monto a depositar debe ser mayor a 0.")

    def retirar(self, monto):
        if monto <= 0:
            print("El monto a retirar debe ser mayor a 0.")
        elif monto > self._saldo:
            print("Saldo insuficiente. No se puede realizar el retiro.")
        else:
            self._saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${self._saldo:.2f}")

    def mostrar_informacion(self):
        return (f"Titular: {self._titular} | "
                f"Cuenta: {self._numero_cuenta} | "
                f"Saldo: ${self._saldo:.2f}")

    # Getters
    def get_titular(self):
        return self._titular

    def get_saldo(self):
        return self._saldo

    def get_numero_cuenta(self):
        return self._numero_cuenta

    # Setters
    def set_titular(self, titular):
        if titular.strip():
            self._titular = titular
        else:
            print("El nombre del titular no puede estar vacío.")

    def set_saldo(self, saldo):
        if saldo >= 0:
            self._saldo = saldo
        else:
            print("El saldo no puede ser negativo.")


if __name__ == "__main__":
    cuenta = CuentaBancaria("Ana García", 1000.0, "001-123456")
    print(cuenta.mostrar_informacion())
    cuenta.depositar(500)
    cuenta.retirar(200)
    cuenta.retirar(2000)   # Intento fallido
    print(cuenta.mostrar_informacion())
