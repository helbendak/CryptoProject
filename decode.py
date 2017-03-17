import helper
def read_file(decode_param):
    with open(decode_param, "r") as f:  # Opens decode.param file and stores its text into data variable
        data = f.readlines()

    main_list = []
    for line in data:  # Splits the decode.param file line by line and appends each line into main_list array
        words = line.split()
        main_list.append(words)

    # Splits the main_array into different arrays and then stores each value in its appropriate variable and type
    # TODO: Rewrite this comment properly
    p = int(main_list[0][0])
    q = int(main_list[0][1])
    e = int(main_list[0][2])
    text1 = main_list[1][0]
    text2 = main_list[2][0]
    return p, q, e, text1, text2

def text1_toArray(text1):
    text1_array = []
    with open(text1) as f:
        data = f.readlines()
    for line in data:
        numbers = map(int, line.split())
        text1_array.append(numbers)
    return text1_array

def text2_toArray(text2):
    """
    Converts contents of text2 into an array that has each character of the text file as an element
    """
    # TODO: Rewrite this comment properly
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
    decoded_array = []

    for letter in encoded_list:

        decoded_number_pair = []
        for number in letter:
            decoded_number_pair.append(helper.fast(number, d, n))
        decoded_array.append(decoded_number_pair)
    return decoded_array


if __name__ == '__main__':
    p, q, e, text1, text2 = read_file("decode.param.txt")


    #TODO: read out_code

    n = p*q
    phi = (p-1)*(q-1)
    d = helper.modinv(e, phi)
    encoded_list = text1_toArray(text1)

    decoded_array = decode(encoded_list, n, d)
    print decoded_array

    file = open("decoded.txt","w")
    text2array = text2_toArray(text2)

    print(len(text2array))

    print(decoded_array)
    for i in range(0, len(decoded_array) ):
        for j in range(0, len(decoded_array[i]) - 1):

            char = text2array[decoded_array[i][j]][decoded_array[i][j+1]]
            print char
            file.write(char)
    file.close()