import helper

def prime_factorization(n):
# Brute-force prime factorization for n
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
            factors.append(n)
    return factors

if __name__ == '__main__':
    n = 32193613398841823 	# Public key n
    e = 17					# Public key e
    factors = prime_factorization(n)
    p = factors[0]
    q = factors[1]
    print "Value of n = " + str(n)
    print "Value of e = " + str(e)
    print "Value of p = %d" % p
    print "Value of q = %d" % q
    phi = (p-1)*(q-1)
    d = helper.modinv(e, phi)
    print "Value of private key, d = %d" % d # Private key d

