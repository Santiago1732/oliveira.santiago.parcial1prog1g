# 1. Crear una función llamada aplicarAumento que reciba como parámetro el precio de un producto y 
# devuelva el valor del producto con un aumento del 5%. Realizar la llamada desde el main.

def aplicar_aumento(precio_producto):

    valor_porcentaje = (precio_producto * 5)/100
    valor_con_aumento = valor_porcentaje + precio_producto
    
    return valor_con_aumento