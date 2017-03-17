with open("code.param.txt","r") as f: #Opens code.param file and stores its text into data variable
    data = f.readlines()

main_list = []
for line in data: #Splits the code.param file line by line and appends each line into main_list array
    words = line.split()
    main_list.append(words)

#Splits the main_array into different arrays and then stores each value in its appropriate variable and type
numbers_list = main_list[0]
p = int(numbers_list[0])
q = int(numbers_list[1])
e = int(numbers_list[2])
text1 = main_list[1]
text1=text1[0]
text2 = main_list[2]
text2=text2[0]


print p,q,e
print text1
print text2