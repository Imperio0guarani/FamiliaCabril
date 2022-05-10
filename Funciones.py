def quiz():
    pregunta = input('introduzca su pregunta: ')
    R1 = input('introduzca su respuesta Correcta:  ')
    R2 = input('introduzca su respuesta Incorrecta:  ')
    R3 = input('introduzca su respuesta Incorrecta:  ')
    RC = "A"
    # Rc = respuesta correcta

    print(pregunta)
    print(" A: " + R1 + "\n B: " + R2 + "\n C: " + R3)
    RD = input('Cual es la respuesta correcta: ')
    # RD = respuesta dada por el usuario
    if RD == RC:
        print("bien hecho")
    else:
        print("pelotudo")
