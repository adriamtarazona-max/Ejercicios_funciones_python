#*** zona funcion ***
def pedir_producto():
    producto = int(input("Que producto lleva:"))
    return producto
def cantidad_pedidos(producto):
    pedidos= int(input("Digite la cantidad de pedidos:"))
    return pedidos
def prosesar_datos(pedidos):
    c=0
    for i in range (pedidos):
        calificacion= int(input("del 1 al 5 que calificacion de:"))
        if calificacion == 5:
            print("excelente")
        c= c + calificacion
        sum= c
    return sum
def hacer_calculo(sum, pedidos):
    prom= sum / pedidos
    return sum, prom
def mostrar_mensaje(prom):
    print("el promedio es"+ str(prom))
    
    
    
#*** codigo principal ***
p = pedir_producto()
pedidos = cantidad_pedidos(p)
sum = prosesar_datos(pedidos)
prom = hacer_calculo(p, pedidos)
mostrar_mensaje(prom)

     