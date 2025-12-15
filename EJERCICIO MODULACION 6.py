#*** zona funcion ***
def definir_cpu():
    cpu = float(input("Uso de CPU de un servidor: "))
    return cpu
def procesar_cpu():
    alertas = 1
    mediciones = 1
    uso = definir_cpu()
    while uso >= 0:
        mediciones = mediciones + 1
        if uso > 90:
            print("Alerta:Uso critico")
            alertas = alertas + 1
        uso = definir_cpu()
    return alertas, mediciones

def mostrar_resultado(alertas, mediciones):
    print("Total de medicione:", mediciones)
    print("Alerta critica:", alertas)





#*** codigo principal ***
cpu = definir_cpu()
alertas, mediciones = procesar_cpu()
mostrar_resultado(alertas, mediciones)