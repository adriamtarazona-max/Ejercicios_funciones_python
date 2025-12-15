#*** zona fucion ***
def definir_precio():
    precio = float(input("Precio del producto: "))
    return precio
def definir_cantidad():
    can = int(input("Cantidad: "))
    return can
def procesar_compra():
    subtotal = 0
    seguir = input("Agregar producto (si/no): ")
    while seguir != "no":
        precio = definir_precio()
        cantidad = definir_cantidad()
        subtotal = subtotal + (precio * cantidad)
        seguir = input("Agregar otro producto (si/no): ")
    return subtotal
def hacer_calculo_descuento(subtotal):
    if subtotal > 1000:
        descripcion = subtotal * 0.10
    else:
        if subtotal > 500:
            descripcion = subtotal * 0.05
        else:
            descripcion = 0
    total = subtotal - descripcion
    return total, descripcion
def mostrar_total(total, descripcion):
    print("descuento aplicado:", descripcion)
    print("monto final a pagar:", total)


#*** codigo principal ***
precio = definir_precio()
subtotal = procesar_compra()
total, descripcion = hacer_calculo_descuento(subtotal)
mostrar_total(total, descripcion)
