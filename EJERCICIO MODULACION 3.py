#*** zona funcion ***
def definir_datos():
 t = input("Tipo D deposito R retiro o FIN: ")
 return t
def monto():
    m = float(input("Monto: "))
    return m
def hacer_calculo():
    saldo = 2000
    Transacciones  = 0
    tipo = definir_datos()
    while tipo != "FIN":
        if tipo == "D":
            m = monto()
            saldo = saldo + m
            Transacciones  =  Transacciones  + 1
        else:
            if tipo == "R":
                m = monto()
                if saldo - m >= 0:
                    saldo = saldo - m
                    Transacciones  =  Transacciones  + 1
                else:
                    print("No se puede retirar, saldo insuficiente")
            else:
                print("tipo no valido")

        tipo = definir_datos()
    return saldo,  Transacciones 
def mostrar_resultado(saldo,  Transacciones ):
    print("saldo final:", saldo)
    print("transacciones validas:",  Transacciones )


#*** codigo principal ***
t = definir_datos()
saldo, trans =  hacer_calculo()
mostrar_resultado(saldo, trans)