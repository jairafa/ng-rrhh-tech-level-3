def contar_colisiones(movimientos):
    n = len(movimientos)
    colisiones = [0] * n
    direcciones = list(movimientos)
    print("\nIniciando...")

    while True:
        nuevas_direcciones = direcciones[:]
        print("Direcciones: %s, Colisiones: %s" % (nuevas_direcciones, colisiones))
        colision_ocurrida = False
        for i in range(n - 1):
            if direcciones[i] == 'R' and direcciones[i + 1] == 'L':
                # Colisión detectada
                colisiones[i] += 1
                colisiones[i + 1] += 1
                nuevas_direcciones[i] = 'L'
                nuevas_direcciones[i + 1] = 'R'

                # Actualizar las direcciones solo si hubo colisiones
                direcciones = nuevas_direcciones
                colision_ocurrida = True
                break
                
        if not colision_ocurrida:
            print("Resultado final:\nDirecciones: %s, Colisiones: %s" % (nuevas_direcciones, colisiones))
            break
 
    return colisiones
