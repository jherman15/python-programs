import cmath
if __name__ == '__main__':

    print

    # calculate the discriminant

    w = (y ** 2) - (4 * x * z)

    # find two solutions

    sol1 = (-y - cmath.sqrt(w)) / (2 * x)

    sol2 = (-y + cmath.sqrt(w)) / (2 * x)

    print('The solution are {0} and {1}'.format(sol1, sol2))