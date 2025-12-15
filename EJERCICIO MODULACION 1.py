#*** zona funcion ***
def definir():
    producto = int (input("Que producto lleva:"))
    return producto
def cantidad():
    pedidios = int(input("Cantidad de pedidos: "))
    return pedidios
def procesar(pedidos):
    total = 0
    continuacion = 0 
    for norte in range (pedidos):
        print("Califcacion del pedido:")
        calificacion = int(input("Del 1 al 5:"))
        if calificacion == 5:
            print("Excelente")
            total = total + calificacion
            continuacion = continuacion + 1
    return total, continuacion
def hacer_calculo(total, continuacion):
    if continuacion > 0:
        prom = total / continuacion
    else:
        prom = 0
    return prom
def mostrar_resultado(prom):
    print("El promedio es :", prom)




#*** codigo principal ***
producto = definir()
cantidad = cantidad()
total, continuacion = procesar(cantidad)
prom = hacer_calculo (total, continuacion)
mostrar_resultado(prom)
