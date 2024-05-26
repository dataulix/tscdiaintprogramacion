# EJERCICIO 3: Un hincha de fútbol desea conocer la cantidad de puntos que su
# equipo lleva acumulados en el campeonato, para ello recibe cada semana la	
# información de la cantidad total de partidos, desde el inicio del campeonato, que
# el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado	
# recibe un punto, por cada partido ganado tres puntos y por los perdidos cero puntos.

ganados = int(input("Ingresa la cantidad de partidos ganados: "))
empatados = int(input("Ingresa la cantidad de partido empatados: "))
perdidos = int(input("Ingresa la cantidad de partidos perdidos: "))
total = ganados * 3 + empatados * 1 + perdidos * 0
print("El total de puntos de su equipo es: ", total)


