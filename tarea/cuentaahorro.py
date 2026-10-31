from .cuentabancaria import CuentaBancaria


class CuentaAhorro(CuentaBancaria):

    TASA_INTERES = 0.001

    def __init__(self, titular, cbu, saldo_inicial=0):
        super().__init__(titular, cbu, saldo_inicial)

    def extraer(self, monto):
        self._validar_monto(monto)
        if monto > self.saldo:
            print(
                f"Extracción rechazada en CuentaAhorro: fondos insuficientes. "
                f"Saldo disponible: ${self.saldo:.2f}"
            )
            return False
        self.saldo -= monto
        print(
            f"Extracción exitosa de CuentaAhorro: ${monto:.2f}. "
            f"Saldo resultante: ${self.saldo:.2f}"
        )
        return True

    def aplicar_interes(self):
        interes = round(self.saldo * self.TASA_INTERES, 2)
        self.saldo += interes
        print(
            f"Interés acreditado en CuentaAhorro: ${interes:.2f}. "
            f"Nuevo saldo: ${self.saldo:.2f}"
        )
        return interes
