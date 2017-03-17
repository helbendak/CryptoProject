import random
import helper

def read_file(code_param):
    with open(code_param, "r") as f:  # Opens code.param file and stores its text into data variable
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

def text1_toArray(text1):
    text1_array = []
    with open(text1) as f:
      while True:
        char = f.read(1)
        if not char:
          break
        text1_array.append(char)
    print text1_array
    print len(text1_array)
    return text1_array


def encode(final_list, n, e):
    #encoded = []
    file = open("out_code.txt", "w")
    for letter in final_list:
        #encoded_numbers = []
        for number in letter:
        #    encoded_numbers.append(helper.fast(number, e, n))
            file.write(' ')
            file.write(str(helper.fast(number, e, n)))
        #encoded.append(encoded_numbers)
        file.write('\n')
    file.close()
    #return encoded

if __name__ == '__main__':
    p, q, e, text1, text2 = read_file("code.param.txt")
    text2_array = text2_toArray(text2)
    text1_array = text1_toArray(text1)
    final_list = []
    for char in text1_array:
        temp_array = []
        for i in range(0, len(text2_array) ):
            for j in range(0, len(text2_array[i]) ):
                if char == text2_array[i][j]:

                    temp_array.append([i,j])
                    #print "Character: " + char + " FOUND " + "[" + str(i) + "]" + "[" + str(j) + "]"
        length = len(temp_array)

        if length != 0: # Sanity check
            rand = random.randint(0, length - 1)
            final_list.append(temp_array[rand])
    print len(final_list)
    #print final_list

    #print ("\n\n")

    # RSA encoding
    n = p*q
    #print "n = %d" % n
    #print "e = %d" % e
    #encoded = encode(final_list, n, e)
    #file = open("out_code.txt", "w")
    #file.write(str(encoded))
    #file.close()
    encoded = encode(final_list, n, e)
    #print encoded