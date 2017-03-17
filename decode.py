def read_file(decode_param):
    with open(decode_param, "r") as f:  # Opens code.param file and stores its text into data variable
        data = f.readlines()

    main_list = []
    for line in data:  # Splits the code.param file line by line and appends each line into main_list array
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


if __name__ == '__main__':
    p, q, e, text1, text2 = read_file("decode.param.txt")
    print p, q, e, text1, text2