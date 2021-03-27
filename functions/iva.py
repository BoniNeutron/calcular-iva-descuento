
def calcIva():

    repetir = "si"
    while repetir.lower() == "si":

        print("Conozca cuanto porcentaje se le cobrara por el producto, segun a la categoria que pertenezca.")
        operacion = str(input("Su producto pertenece a:\n1. La canasta familiar.\n2. Es una vivienda.\n"))

        if operacion.lower() == "1" or operacion == "canasta":
            
            print("Al pertenecer a la canasta familiar solo se le aplicara un 5% de IVA a su producto.")

            costoCanasta = int(input("Ingrese el precio del producto\n"))

            soloIva = costoCanasta * 0.05
            conIva = costoCanasta + soloIva

            print(f"El IVA de su procto es: {soloIva} por lo cual tendra que cancelar: {conIva}")

        elif operacion.lower() == "2" or operacion == "vivienda":
        
            print("La compra de una vivienda nueva obliga al comprador a pagar el IVA al vendedor. Los tipos impositivos establecidos actualmente son: 10% con carácter general.")

            costoVivienda = int(input("Ingrese el precio de la vivienda\n"))

            soloIva = costoVivienda * 0.1
            conIva = costoVivienda + soloIva

            print(f"El IVA de su vivienda es: {soloIva} por lo cual tendra que cancelar: {conIva}")

        else:

            print("La opcion elegida no esta en la lista.")

        repetir = str(input("Desea realizar otra operacion?\n"))


