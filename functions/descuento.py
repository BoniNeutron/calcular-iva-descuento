
def calcDescuento():

    repetir = "si"
    while repetir.lower() == "si":

        precio = float(input("Ingrese el precio de la prenda\n"))
        
        desc20 = precio * 0.2

        operacion = precio - desc20

        print(f"Su prenda costara: {operacion}")
        repetir = str(input("Desea realizar el calculo para otra prenda?\n"))





