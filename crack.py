import helper

#def read_file(madrigal_code):
#    with open(madrigal_code, "r") as f:  # Opens code.param file and stores its text into data variable
#        data = f.readlines()
#
#    main_list = []
#    for line in data:  # Splits the code.param file line by line and appends each line into main_list array
#        words = line.split()
#        main_list.append(words)
#    return main_list

# TODO : Add comments for this file

def prime_factorization(n):
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
	n = 32193613398841823
	e = 17
	#main_list = read_file("madrigal.code.txt")
	factors = prime_factorization(n)
	p = factors[0]
	q = factors[1]
	print "p = %d" % p
	print "q = %d" % q
	phi = (p-1)*(q-1)
	print "phi = %d" % phi
	d = helper.modinv(e, phi)
	print "d = %d" % d
