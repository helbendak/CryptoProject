import random
import helper

def read_file(code_param):
    """
    Function that takes in the code.param text file as input,
    stores the p, q, e values and file names in separate variables and returns them
    """
    main_list = []
    with open(code_param, "r") as f:
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
    Converts contents of text1 into an array of the following form:
    [ characters of text1 ]
    A 1D array that can later be iterated over to find the characters need to be encoded
    """
    text1_array = []
    with open(text1) as f:
      while True:
        char = f.read(1)
        if not char:
          break
        text1_array.append(char)
    return text1_array

def text2_toArray(text2):
    """
    Converts contents of text2 into an array of the following form:
    [ [characters of line1], [characters of line2], ... ]
    A 2D array that can later be used to return the position of a particular character
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

def encode(final_list, n, e):
    """
    Takes a 2D array of 'coordinates' and encodes each number using the 'fast' function provided
    Writes the encoded numbers to the output file
    """
    file = open("code.out.txt", "w")
    for letter in final_list:
        for number in letter:
            file.write(' ')
            file.write(str(helper.fast(number, e, n)))
        file.write('\n')
    file.close()

if __name__ == '__main__':
    p, q, e, text1, text2 = read_file("code.param.txt")
    text2_array = text2_toArray(text2)
    text1_array = text1_toArray(text1)
    final_list = []
    for char in text1_array:
        # Adds all possible 'coordinates' of a character to a temporary array
        temp_array = []
        for i in range(0, len(text2_array) ):
            for j in range(0, len(text2_array[i]) ):
                if char == text2_array[i][j]:
                    temp_array.append([i,j])
        length = len(temp_array)
        if length != 0: # Sanity check
            # Picks a random 'coordinate' from all possible ones and adds it to the final list
            rand = random.randint(0, length - 1)
            final_list.append(temp_array[rand])
    # RSA encoding:
    n = p*q
    encoded = encode(final_list, n, e)