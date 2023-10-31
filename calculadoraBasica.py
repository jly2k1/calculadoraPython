#Calculadora basica en Python

expresion = ""
posicionOperador = 0
terminar = ""
resultado = 0

#bucle que termina hasta que el usuario se lo indique:

while(terminar != "S" and terminar != "s"):
    print("Digita la expresion que quieres evaluar:")

    expresion = input()
    
    if("+" in expresion or "-" in expresion or "*" in expresion or "/" in expresion):
        if(expresion.find("+") >= 0):
            posicionOperador = expresion.find("+")
        elif(expresion.find("-") >= 0):
            posicionOperador = expresion.find("-")
        elif(expresion.find("*") >= 0):
            posicionOperador = expresion.find("*")
        elif(expresion.find("/") >= 0):
            posicionOperador = expresion.find("/")

        #obtenemos los numeros de la cadena 'partiendola' desde el signo de operacion
        num1Cad, num2Cad = "", ""

        num1Cad = expresion[0:posicionOperador]
        num2Cad = expresion[(posicionOperador+1):len(expresion)]

        #Convertir las cadenas a números
        num1N, num2N = 0, 0

        num1N = int(num1Cad);
        num2N = int(num2Cad);


        #Evaluar la operacion según el signo que tenga la expresion
        if("+" in expresion):
            resultado = num1N + num2N

            print(resultado)
        elif("-" in expresion):
            resultado = num1N - num2N

            print(resultado)
        elif("*" in expresion):
            resultado = num1N * num2N

            print(resultado)
        elif("/" in expresion):
            resultado = num1N / num2N

            print(resultado)

    print("Desea terminar con el programa? [S/N]:")
    terminar = input()
