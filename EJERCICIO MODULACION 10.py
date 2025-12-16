#*** zona funcion ***
def definir_datos():
    horas = int(input("Horas extra trabajadas: "))
    return horas
def hacer_calculo():
    total = 0
    empleados = 0
    horas = definir_datos()
    while horas >= 0:
        if horas > 5:
            bono = horas * 15
            total = total + bono
            empleados = empleados + 1
        else:
            if horas > 0:
                bono = horas * 10
                total = total + bono
                empleados = empleados + 1
        horas = definir_datos()
    return total, empleados
def mostrar_resultado(total, empleados):
    print("Bonificacion total:", total)
    print("Empleados con bonificacion:", empleados)


#*** codigo principal ***
total, empleados = hacer_calculo()
mostrar_resultado(total, empleados)
