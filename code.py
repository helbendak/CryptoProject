def read_file(code_param):
    with open(code_param, "r") as f:  # Opens code.param file and stores its text into data variable
        data = f.readlines()

    main_list = []
    for line in data:  # Splits the code.param file line by line and appends each line into main_list array
        words = line.split()
        main_list.append(words)

    # Splits the main_array into different arrays and then stores each value in its appropriate variable and type
    numbers_list = main_list[0]
    p = int(numbers_list[0])
    q = int(numbers_list[1])
    e = int(numbers_list[2])
    text1 = main_list[1]
    text1 = text1[0]
    text2 = main_list[2]
    text2 = text2[0]
    return p, q, e, text1, text2

def text2_toArray(text2):
    """
    Converts contents of text2 into an array that has each character of the text file as an element
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


    #with open(text2) as f:
    #  while True:
    #    char = f.read(1)
    #    if not char:
    #      break
    #    text2_array.append(char)
    #return text2_array

if __name__ == '__main__':
    p , q, e, text1, text2 = read_file("code.param.txt")
    text2_array = text2_toArray(text2)
    print text2_array