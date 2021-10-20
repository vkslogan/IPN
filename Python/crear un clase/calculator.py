import funciones.py
#PROGRAMA PRINCIPAL
continua = True
while(continua):
    seleccion = menu()
    resultado = OperacionesBasicas(seleccion)
    print(str(resultado))
    print("Quieres continuar (s/n)? ")
    if(input() == "s" or input() == "S"):
        continua = True
    else:
        continua = False
        print("Fin del programa")
