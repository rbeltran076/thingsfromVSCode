from math import log, factorial
def aritmetica_solver(an, a1, d, n):
    print('-------------------------------------ARIT_SOLVER------------------------------------------------')    
    if an == 'None':
        an = a1 + (n - 1) * d
        print('El termino enesimo es {}'.format(round(an)))

    elif a1 == 'None':
        a1 = an - (n - 1) * d
        print('El primer termino es {}'.format(round(a1)))

    elif d == 'None':
        d = (an - a1)/(n - 1)
        print('La diferencia es {}'.format(d))

    elif n == 'None':
        n = ((an - a1) / d) + 1
        print('El numero de terminos entre esos numeros es {}'.format(round(n)))
    
    elif an == 'solo tengo 2 terminos' and a1 == False and d == False and n == False:
        print('escribe 2 terminos no necesariamente consecutivos:')
        x = int(input('Numero x = '))
        n_x = int(input('lugar del termino x: '))
        y = int(input('Numero y = '))
        n_y = int(input('lugar del termino y: '))
        d = (x - y)/( - n_y + n_x) 
        a1 = x - (n_x - 1) * d
        print('La diferencia es: {}'.format(d))
        print('El primer termino es: {}'.format(a1))
        print('La ecuacion del termino general es: an =', a1 - d, ' + (', float(d), '* n )')
        n = int(input('ingrese el lugar del termino enesimo  '))
        an = a1 + (n - 1) * d 
        print('el valor del termino enesimo es:', an)

    elif an == 'serie' and a1 == False and d == False and n == False:
        an = input('Escribe el an: ')
        a1 = int(input('Escribe el a1: '))
        n = int(input('Escribe el lugar enesimo (n): '))
        if an == 'None':
            print('Para determinar \'an\' escribe 2 terminos no necesariamente consecutivos: ')
            x = int(input('Numero x = '))
            n_x = int(input('lugar del termino x: '))
            y = int(input('Numero y = '))
            n_y = int(input('lugar del termino y: '))
            d = (x - y)/( - n_y + n_x) 
            a1 = x - (n_x - 1) * d
            print('La diferencia es: {}'.format(d))
            print('El primer termino es: {}'.format(a1))
            print('La ecuacion del termino general es: an =', a1 - d, ' + (', float(d), '* n )')
            n = int(input('ingrese el lugar del termino enesimo  '))
            an = a1 + (n - 1) * d 
            print('el valor del termino enesimo es:', an)
        else:
            an = int(input('OK, vuelve a escribir el an, me olvide xd '))
        S = ((a1 + an) * n) / (2)
        print('La sumatoria de aquellos terminos es: {}'.format(S))

def geometrica_solver(an, a1, r, n):
    print('------------------------------------GEOM_SOLVER-------------------------------------------------')
    if an == 'None':
        an = (a1 * r) ** (n - 1)
        print('El termino enesimo es {}'.format(round(an)))

    elif a1 == 'None':
        a1 = an / (r ** (n - 1))
        print('El primer termino es {}'.format(round(a1)))

    elif r == 'None':
        r = (an / a1) ** (1 / (n - 1))
        print('La razon es {}'.format(r))

    elif n == 'None':
        n = ((log(int(an / a1), 10)) / (log(int(r), 10))) + 1
        print('El numero de terminos entre esos numeros es {}'.format(round(n)))

    elif an == 'solo tengo 2 terminos' and a1 == False and r == False and n == False:
        print('escribe 2 terminos no necesariamente consecutivos:')
        x = int(input('Numero x = '))
        n_x = int(input('lugar del termino x: '))
        y = int(input('Numero y = '))
        n_y = int(input('lugar del termino y: '))
        r = (y / x) ** (1 / ((n_y - 1) - (n_x - 1)))
        a1 = x / (r ** (n_x - 1))
        print('La razon es: {}'.format(r))
        print('El primer termino es: {}'.format(a1))
        print('La ecuacion del termino general es: an =', a1, '* (', r, '^ (n - 1) )')
        n = int(input('ingresa el lugar del termino enesimo: '))
        an = a1 * (r ** (n - 1))
        print('el valor del termino enesimo es:', an)

    elif an == 'serie' and a1 == False and r == False and n == False:
        a1 = int(input('Escribe el a1: '))
        n = int(input('Escribe el lugar enesimo (n): '))
        r = int(input('Escribe la razon (r): '))
        if r == 1:
            print('Habria un error matematico, no pongas el 1, no puede ser...')
        else:
            S = (a1 * ((r ** n) - 1)) / (r - 1)
        print('La sumatoria de aquellos terminos es: {}'.format(S))

aritmetica_solver('None', 240, 4, 10)