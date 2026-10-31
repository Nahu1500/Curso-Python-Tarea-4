from abc import ABC, abstractmethod


class CuentaBancaria(ABC):

    def __init__(self, titular, cbu, saldo_inicial=0):
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        self.titular = titular
        self._cbu = cbu
        self.saldo = saldo_inicial

    @property
    def cbu(self):
        return self._cbu

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        saldo_minimo = self._saldo_minimo_permitido()
        if nuevo_saldo < saldo_minimo:
            raise ValueError(
                f"El saldo no puede ser menor que ${saldo_minimo:.2f}."
            )
        self._saldo = nuevo_saldo

    def _saldo_minimo_permitido(self):
        return 0

    def _validar_monto(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero.")

    def depositar(self, monto):
        self._validar_monto(monto)
        self.saldo += monto
        print(
            f"Depósito exitoso en {type(self).__name__}: ${monto:.2f}. "
            f"Saldo actual: ${self.saldo:.2f}"
        )
        return True

    def __str__(self):
        return (
            f"[{type(self).__name__}] Titular: {self.titular} | "
            f"CBU: {self.cbu} | Saldo: ${self.saldo:.2f}"
        )

    @abstractmethod
    def extraer(self, monto):
        pass
