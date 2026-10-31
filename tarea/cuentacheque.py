from .cuentabancaria import CuentaBancaria


class CuentaCheque(CuentaBancaria):

    def __init__(self, titular, cbu, saldo_inicial=0, costo_emision=50):
        if costo_emision < 0:
            raise ValueError("El costo de emisión no puede ser negativo.")
        self._costo_emision = costo_emision
        super().__init__(titular, cbu, saldo_inicial)

    @property
    def costo_emision(self):
        return self._costo_emision

    def extraer(self, monto):
        self._validar_monto(monto)
        total_requerido = monto + self.costo_emision
        if total_requerido > self.saldo:
            print(
                f"Extracción rechazada en CuentaCheque: fondos insuficientes. "
                f"Total requerido: ${total_requerido:.2f}. "
                f"Saldo disponible: ${self.saldo:.2f}"
            )
            return False
        self.saldo -= total_requerido
        print(
            f"Extracción exitosa de CuentaCheque: monto ${monto:.2f}, "
            f"comisión ${self.costo_emision:.2f}. "
            f"Saldo resultante: ${self.saldo:.2f}"
        )
        return True
