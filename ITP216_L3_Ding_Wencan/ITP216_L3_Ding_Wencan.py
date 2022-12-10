# Wencan Ding chrisdin@usc.edu
# ITP 216, Fall 2022
# Section: 32080
# Lab 3
# Description:
# read the contents of a text file into header and data variables
# file_read_header()
def file_read_header(file_name ="oscar_age_female.csv"):
    f_in = open(file_name,"r")
    # param file_name: the file to read
    # return: the header row(first line)
    headerLine = f_in.readline()
    f_in.close()
    return headerLine
def file_read_data(file_name="oscar_age_female.csv"):
    # param file_name: the file name to read
    # return: all the data in this file except for the header/first line/row as a list
    listOfLines = []
    f_in = open(file_name,"r")
    headerLine = f_in.readline() # skipping the header row
    for line in f_in:
        line = line.strip()
        listOfLines.append(line)
    f_in.close()
    return listOfLines
def main():
    header_line = file_read_header()
    print("Header:")
    print(header_line)
    filedata = file_read_data()
    print("Data:")
    for line in filedata:
        print(line)
main()