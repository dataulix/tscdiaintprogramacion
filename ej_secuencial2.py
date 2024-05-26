# EJERCICIO 2: Un pintor de casas debe hacer un presupuesto para un cliente.
# Lo que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. 
# El cliente le indica que necesita conocer el costo de mano de obra para pintar una
# pared rectangular de un galpón. El pintor cobra un monto fijo por cada metro cuadrado.
# Puedes hacer un algoritmo para calcular el costo de mano de obra para pintar la pared.


monto_fijo = float(input("Ingresa el monto fijo por m2: "))
metros = float(input("Ingresa los metroa cuadrados: "))
total = monto_fijo * metros
print("El total es: $", total)

