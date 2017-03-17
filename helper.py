def fast(x, e, m): # function for fast computation of Y = x**e % m
    X = x
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E/2
        else:
            Y = (X * Y) % m
            E = E-1
    return Y

def egcd(a, b):
    """
    Euclid's greatest common divisor
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(e, phi):
    """
    Returns modular multiplicative inverse d such that
    d = e^-1 mod( phi(n) )
     """
    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % phi


print modinv(7,40)
print fast(55,7,23)