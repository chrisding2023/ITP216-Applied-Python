# Wencan Ding
# ITP 216, Fall 2022
# Section: 32080
# Lab 2 (there is no lab 1)
# Description:
# Describe what this program does in your own words such as:
# This program convert a sentence into different data types such as string, list, tuple, set, and dictionary
def convert(list):
    return tuple(i for i in list)
def main():
    # create an input
    sentence = input("Please enter an input to be converted: ")
    print("string: ", end="")
    for i in range(len(sentence)):
        print(sentence[i], end=", ")
    list = []
    dict = {}
    # convert strings into list and tuple
    for i in range(len(sentence)):
        list.append(sentence[i])
        if sentence[i] in dict.keys():
            dict[sentence[i]] += 1
        else:
            dict[sentence[i]] = 1
    print("\nlist: ",  end="")
    for i in list:
        print(i, end=', ')
    print("\ntuple: ", end ="")
    for i in convert(list):
        print(i, end=", ")
    # convert string into a set
    set1 = set(sentence)
    print("\nset: ", end="")
    for i in set1:
        print(i, end=", ")
    print("\n dictionary: ")
    for i in dict:
        print(i + ':' + str(dict[i]))

main()

