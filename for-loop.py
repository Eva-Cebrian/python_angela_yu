listaNumeros = [1, 150, 300, 1500, 20]
num = 0
# CALCULA EL MAXIMO NUMERO DE UNA LISTA USANDO LOOP FOR

for i in listaNumeros:
    if i > num:
        num = i
    else: print(num)

""" for i in range(1,11):
    print(i) """

maximo = max(listaNumeros)

print(maximo)
