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


if __name__ == '__main__':
    p, q, e, text1, text2 = read_file("decode.param.txt")
    print p, q, e, text1, text2
    
    array_to_decode = text1_toArray(text1)

    n = p*q
    phi = (p-1)*(q-1)
    d = helper.modinv(e, phi)
