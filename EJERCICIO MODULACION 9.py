#*** zona funcion ***
def definir_stock_inicial():
    stock_inicial = 50
    return stock_inicial
def definir_ventas_diarias():
    ventas_diarias = int(input("Cantidad vendida hoy: "))
    return ventas_diarias
def procesar_ventas(stock_inicial):
    punto_reposicion = 10
    stock_actual = stock_inicial
    aviso_reposicion = ""

    while stock_actual > punto_reposicion:
        ventas_diarias = definir_ventas_diarias()
        stock_actual -= ventas_diarias

        if stock_actual <= punto_reposicion:
            aviso_reposicion += "Aviso de Reposición Urgente\n"
            break

    return stock_actual, aviso_reposicion
def mostrar_resultados(stock_actual, aviso_reposicion):
    print("Stock actual:", stock_actual)
    if aviso_reposicion:
        print(aviso_reposicion)



        
#*** codigo principal ***
stock_inicial = definir_stock_inicial()
stock_actual, aviso_reposicion = procesar_ventas(stock_inicial)
mostrar_resultados(stock_actual, aviso_reposicion)
