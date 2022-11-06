import cmath
if __name__ == '__main__':

    a = 5
    b = 6
    c = 1

    print ('\nEquation: ax^2 + bx + c = 0\n')

    delta = (b ** 2) - (4 * a * c)

    x1 = (-b - cmath.sqrt(delta)) / (2 * a)

    x2 = (-b + cmath.sqrt(delta)) / (2 * a)

    print('Solutions:\nx1: ', x1, '\nx2: ', x2)