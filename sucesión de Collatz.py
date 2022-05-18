n = int(input('ingresa un numeros: '))
print('='*20)
print(n)
while n != 0:
    cantDeVueltas = 0
    sumaProme = 0
    mayBandera = True
    if n > 0 and n != 1:
        while n != 1:
            if n % 2 != 0:
                n = n * 3 + 1
            else:
                n = n // 2
            if mayBandera or may < n:
                may = n
                mayBandera = False
            print(n)
            sumaProme += n
            cantDeVueltas += 1
        print('='*20)
        print('la cantidad de vueltas fue: ', (sumaProme/cantDeVueltas))
        print(f'longitud de la vuelta: {cantDeVueltas+1}')
        print('el numero mayor fue: ', may)
    else:
        print('porfavor selecciona un numero que sea mayor a 1')
    print('='*20)
    n = int(input('ingresa un nuevo numeros o finaliza con 0:'))