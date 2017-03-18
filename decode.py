import helper

def read_file(decode_param):
    """
    Function that takes in the decode.param text file as input,
    stores the p, q, e values and file names in separate variables and returns them
    """
    main_list = []
    with open(decode_param, "r") as f:
        data = f.readlines()
    for line in data:
        words = line.split()
        main_list.append(words)
    p = int(main_list[0][0])
    q = int(main_list[0][1])
    e = int(main_list[0][2])
    text1 = main_list[1][0]
    text2 = main_list[2][0]
    return p, q, e, text1, text2

def text1_toArray(text1):
    """
    Converts content of text2 (code.out) into a 2D array of integers, 
    each sub-array represents a line of text2 and 
    the elements of the sub-arrays represent the elements of text2 of such line
    """
    text1_array = []
    with open(text1) as f:
        data = f.readlines()
    for line in data:
        numbers = map(int, line.split())
        text1_array.append(numbers)
    return text1_array

def text2_toArray(text2):
    """
    Converts contents of text2 into an array of the following form:
    [ [characters of line1], [characters of line2], ... ]
    A 2D array that can later be used to return the character at a particular position
    """
    text2_array = []
    with open(text2, "r") as f:
        data = f.readlines()
    for line in data:
        line_array = []
        for char in line:
            line_array.append(char)
        text2_array.append(line_array)
    return text2_array

def decode(encoded_list, n, d):
    """
    Takes every element of the array and decode using the computation c**d % n,
    then append them into an array of the form:
    [ [characters of line1], [characters of line2], ... ]
    """
    decoded_array = []
    for letter in encoded_list:
        decoded_number_pair = []
        for number in letter:
            decoded_number_pair.append(helper.fast(number, d, n))
        decoded_array.append(decoded_number_pair)
    return decoded_array

if __name__ == '__main__':
    p, q, e, text1, text2 = read_file("decode.param.txt")
    # Computation of the variables for RSA algorithm's implementation
    n = p*q
    phi = (p-1)*(q-1)
    d = helper.modinv(e, phi)

    encoded_list = text1_toArray(text1)
    decoded_array = decode(encoded_list, n, d)

    # Converting the decoded array into a plain text file, using auxiliary text text2
    file = open("decoded.txt","w")
    text2array = text2_toArray(text2)
    for i in range(0, len(decoded_array) ):
        # Finds the character in text2 corresponding to each 'coordinate' and writes the character to the output file
        for j in range(0, len(decoded_array[i]) - 1):
            char = text2array[decoded_array[i][j]][decoded_array[i][j+1]]
            file.write(char)
    file.close()