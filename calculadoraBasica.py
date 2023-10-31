#Calculadora basica en Python

expresion = ""
terminar = ""
lista_operadores = []
lista_operandos = []
operando = ""
resultado = 0

#bucle que termina hasta que el usuario se lo indique:

while(terminar != "S" and terminar != "s"):
    print("Digita la expresion que quieres evaluar:")

    expresion = input()    

    #Recorremos la expresion caracter a caracter       
    for i in range(len(expresion)):

        """
        Si el caracter es un digito númerico, lo concatenamos a la variable operando que esta vacia. Esto es por si los operandos tienen mas de un digito.
        Si el caracter no es un digito numerico, se guarda el operando como un valor entero en la lista de operandos y guardamos el caracter que se tiene
        en ese momento (que es un operador), en la lista de operadores.
        """
        if(expresion[i].isnumeric()):
            operando += expresion[i]
        else:
            lista_operandos.append(int(operando))

            operando = "" #limpiamos la variable

            lista_operadores.append(expresion[i])

        if(i == len(expresion)-1): #Si nos encontramos en el ultimo caracter de la expresion, guardamos el ultimo operando en la lista
            lista_operandos.append(int(operando))
            operando = ""

    """
    Posteriormente recorremos la lista de operadores para realizar las operaciones correspondientes en la expresion.
    Esto es: si x es igual a +,-,* o /, toma los primeros elementos de la lista y realiza la operacion correspondiente. En caso de que la lista de operandos
    quede vacía, el bucle termina, de lo contrario se inserta al principio de la lista de operandos el resultado de los dos primeros.
    """
    for x in lista_operadores:

        if(x == '+'):
            num1 = lista_operandos.pop(0)
            num2 = lista_operandos.pop(0)
        
            resultado = num1+num2

            if(len(lista_operandos) == 0):
                break
            else:
                lista_operandos.insert(0,resultado)
        elif(x == '-'):
            num1 = lista_operandos.pop(0)
            num2 = lista_operandos.pop(0)
        
            resultado = num1-num2

            if(len(lista_operandos) == 0):
                break
            else:
                lista_operandos.insert(0,resultado)
        elif(x == '*'):
            num1 = lista_operandos.pop(0)
            num2 = lista_operandos.pop(0)
        
            resultado = num1*num2

            if(len(lista_operandos) == 0):
                break
            else:
                lista_operandos.insert(0,resultado)
        elif(x == '/'):
            num1 = lista_operandos.pop(0)
            num2 = lista_operandos.pop(0)
        
            resultado = num1/num2

            if(len(lista_operandos) == 0):
                break
            else:
                lista_operandos.insert(0,resultado)

    print(resultado)

    #Le preguntamos al usuario si quiere continuar con el programa
    print("Desea detener el programa? [S/N]:")

    terminar = input()

    if(terminar == "N" or terminar == "n"): #en caso de que diga 'No' limpiamos la lista de operadores, el resultado y la expresion.
        lista_operadores.clear()
        resultado = 0
        expresion = ""
    elif((terminar != "S" and terminar != "s") and (terminar != "N" and terminar != "N")): #si no se introduce 'N/n' o 'S/s' termina el programa.
        print("hubo un error inesperado")
        break;
