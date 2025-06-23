import random
listado_palabras_adivinar = ["coche", "caca", "mesa", "pez"]

palabra_a_adivinar = random.choice(listado_palabras_adivinar)
print(palabra_a_adivinar)

palabra_a_adivinar_es_lista = list(palabra_a_adivinar)
print(palabra_a_adivinar_es_lista)

longitud_palabra_a_adivinar = len(palabra_a_adivinar_es_lista)
print("La longitud de la palabra a adiviar es: " + str(longitud_palabra_a_adivinar))

progreso = ["_"] * longitud_palabra_a_adivinar
print(progreso)
print()
contador = 6
while "_" in progreso and contador != 0:
    letra = input("Escribe una letra: ").lower()
    
    for i in range(longitud_palabra_a_adivinar):
        if palabra_a_adivinar_es_lista[i] == letra:
            progreso[i] = letra
    if letra not in palabra_a_adivinar_es_lista:
            contador = contador - 1
            print("La letra ' " + letra.upper() + " ' no esta en la palabra a adivinar, te quedan " + str(contador) + " intentos.")
    if contador == 0:
         print ("GAME OVER")
    print(" ".join(progreso))
 


print()
if contador != 0:
    print("FELICIDADES, la palabra es: " + palabra_a_adivinar.upper())



