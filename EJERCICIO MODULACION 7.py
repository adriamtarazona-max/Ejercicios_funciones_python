#*** zona funcion ***
def definir_ventas():
    ventas = float(input("Monto de ventas del vendedor (0 o negativo para terminar): "))
    return ventas                       
def procesar_ventas(ventas):
    meta = 5000
    contador_cumplidos = 0
    total_vendedores = 0
    felicitaciones = ""

    while ventas > 0:
        total_vendedores += 1
        if ventas >= meta:
            contador_cumplidos += 1
            felicitaciones += f"Felicidades vendedor {total_vendedores}, ha cumplido la meta con ventas de {ventas}.\n"
        ventas = definir_ventas()

    return contador_cumplidos, total_vendedores, felicitaciones                                                                                     
def mostrar_resultados(contador_cumplidos, total_vendedores, felicitaciones):   
    print(f"Total de vendedores procesados: {total_vendedores}")
    print(f"Número de vendedores que cumplieron la meta: {contador_cumplidos}")
    print("registro de felicitaciones:")
    print(felicitaciones)



    

#*** codigo principal ***
ventas = definir_ventas()  
contador_cumplidos, total_vendedores, felicitaciones = procesar_ventas(ventas)
mostrar_resultados(contador_cumplidos, total_vendedores, felicitaciones)
