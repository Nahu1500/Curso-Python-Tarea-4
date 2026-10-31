from tarea import cuentaahorro as ca, cuentacorriente as cc, cuentacheque as ch 


# --- CASOS DE PRUEBA ---
ahorro = ca.CuentaAhorro("Carlos Rossi", "285001", saldo_inicial=1000)
corriente = cc.CuentaCorriente("María López", "285002", saldo_inicial=500, limite_descubierto=1000)
cheque = ch.CuentaCheque("Empresa SRL", "285003", saldo_inicial=2000, costo_emision=100)

cuentas = [ahorro, corriente, cheque]

print("--- ESTADO INICIAL ---")
for c in cuentas:
    print(c)

print("\n--- PRUEBA POLIMÓRFICA DE EXTRACCIONES ($800) ---")
for c in cuentas:
    c.extraer(800)

print("\n--- PRUEBA DE INTERÉS EN CUENTA AHORRO ---")
ahorro.aplicar_interes()

print("\n--- PRUEBA DE LECTURA Y PROTECCIÓN (@property) ---")
print(f"Saldo consultado: ${ahorro.saldo}")
#ahorro.saldo = -500  # Descomentar para verificar que arroja ValueError
#ahorro.cbu = "999"   # Descomentar para verificar que arroja AttributeError (solo lectura)