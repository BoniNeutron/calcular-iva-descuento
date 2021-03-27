
import functions.descuento
import functions.iva

def programa():

    print("Bienvenido a almacenes boni, con este programa podras hacer diferentes calculos que te seran utiles al momento de comprar en nuestro almacen.")

    repetir = "si"
    while repetir.lower() == "si":

        print("Hoy te ofrecemos 20% de descuento en la seccion de ropa y te ofrecemos una herramienta para saber el IVA que te cobraremos en ciertos productos.")
        opcion = str(input("Que operacion desea realizar:\n1. Conocer descuento.\n2. Calcular iva.\n"))

        if opcion.lower() == "1" or opcion == "descuento":

            functions.descuento.calcDescuento()

        elif opcion.lower() == "2" or opcion == "iva":

            functions.iva.calcIva()
        
        else:

            print("La opcion elegida no esta en la lista.")

        programa()

programa()