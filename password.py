import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
simbolos = ["!", "%", "€", "$", "&"]
numeros = list(range(0,10))

numeroLetrasCliente = int(input("LETRAS: Escribe un numero del 1 al 5:"))
numeroSimbolosCliente = int(input("LETRAS: Escribe un numero del 1 al 3:"))
numeroNumerosCliente = int(input("LETRAS: Escribe un numero del 1 al 5:"))

pass_5letras = "".join(random.choice(letras) for i in range(numeroLetrasCliente))
pass_2simbolos = "".join(random. choice(simbolos) for i in range(numeroSimbolosCliente))
pass_5numeros = "".join(str(random.choice(numeros)) for i in range(numeroNumerosCliente))

contraCompleta = pass_5letras + pass_2simbolos + pass_5numeros

listaContra =  list(contraCompleta)


random.shuffle(listaContra)

contraSegura = "".join(listaContra)

print(contraSegura)


