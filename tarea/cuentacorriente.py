from .cuentabancaria import CuentaBancaria


class CuentaCorriente(CuentaBancaria):

    def __init__(self, titular, cbu, saldo_inicial=0, limite_descubierto=500):
        if limite_descubierto < 0:
            raise ValueError("El límite de descubierto no puede ser negativo.")
        self._limite_descubierto = limite_descubierto
        super().__init__(titular, cbu, saldo_inicial)

    @property
    def limite_descubierto(self):
        return self._limite_descubierto

    def _saldo_minimo_permitido(self):
        return -self._limite_descubierto

    def extraer(self, monto):
        self._validar_monto(monto)
        saldo_disponible = self.saldo + self.limite_descubierto
        if monto > saldo_disponible:
            print(
                f"Extracción rechazada en CuentaCorriente: límite de "
                f"descubierto excedido. Disponible: ${saldo_disponible:.2f}"
            )
            return False
        self.saldo -= monto
        print(
            f"Extracción exitosa de CuentaCorriente: ${monto:.2f}. "
            f"Saldo resultante: ${self.saldo:.2f}"
        )
        return True
