menu = """ Bienvenido a la interfaz del codigo de Automatizacion de redes.
a continuacion que es lo que quiere realizar:
[1] Producto
[2] Division
[3] Tablas de multiplicar
[4] Cuadrado y cubo
[5] Factorial
[6] Promedio
"""
print(menu)

opcion = input('Seleciona una opcion del 1 al 8:')

if opcion == '1': 
    meconsol1 = """Seleccionaste la opcion 1, porfavor elige un numero:
    """
    print(meconsol1)
    def prod(sub):
        res = 1
        for ele in sub:
            res = ele * res
        return res
    test_list = [5, 6, 2, 1, 7, 5, 3]
    print('La lista original es: ' + str(test_list))
    k = 3
    res = []
    for idx in range(len(test_list) - k + 1):
        res.append(prod(test_list [idx: idx + k]))
    print('Productos calculados: ' + str(res))
    print = input(menu)

elif opcion == '2':
    meconsol2 = """Seleccionaste la opcion 2, porfavor elige un numero.
    """
    print(meconsol2)
    print('Ingrese el primer valor: ')
    n1 = float(input())
    print('Ingrese el segundo valor: ')
    n2 = float(input())
    div = n1 / n2
    print('El resultado es: ', div)
    print = input(menu)

elif opcion == '3':
    meconsol3 = """Seleccionaste la opcion 3.
    """
    print(meconsol3)
    tabla_desde = 1
    tabla_hasta = 10
    desde = 1
    hasta = 10

    for factor1 in range(tabla_desde,  tabla_hasta, + 1):
        print(f'Tabla de multiplicar del {factor1}:')
        for factor2 in range(desde, hasta + 1):
            print(f'{factor1} x {factor2} = {factor1 * factor2}')
    print = input(menu)

elif opcion == '4':
    meconsol4 = """Seleccionaste la opcion 4. 
    """
    print(meconsol4)
    n = int(input("Selecciona el valor que desea elevar :"))
    print("El cuadrado de",n,"es:",n*n)
    print("El cubo de",n,"es:",n*n*n)

elif opcion == '5':
    meconsol5 = """Seleccionaste la opcion 5
    """
    print(meconsol5)
    numero=int(input('Numero'))
    factorial=1
    if numero!=0:
        for i in range(1, numero+1):
            factorial*factorial*i
            print('Factorial: ', factorial)

elif opcion == '6':
    meconsol6 = """Seleccionaste la opcion 6.
    """
    n = 0
    c= 0
    suma = 0
    while n >= 0:
        n = int(input('Ingresa un numero: '))
        if n > 0:
            c = c = 1
            suma = suma + n
    print('El total de numeros positivos es: ', c)
    print('El total de numeros negativos es: ', suma/c)
    print(menu)
else:
    print('Porfavor selecciona un numero del 1 al 6')
    print('=='*25)