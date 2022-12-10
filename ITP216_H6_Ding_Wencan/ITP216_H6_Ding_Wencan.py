# Wencan Ding chrisdin@usc.edu
# ITP 216, Fall 2022
# Section: 32080
# Assignment 6
# Description:
# use the data to calculate the average Robert
# Deniro movie score, and then use it to generate a list of all the movies which were rated above average.
# 1. file_reader()
# a. Description: Retrieves the entire contents of a text file.
# b. Parameters: 1
# i. File name (string)
# c. Returns: 2
# i. The header from the file (list)
# ii. All the rest of data from the file (list)
def file_reader(fn):
    file = open(fn, 'r')
    result = file.readlines()
    header = result[0].split(",")
    data = [row.split(",") for row in result[1:]]
    return header, data
# 2. calculate_mean()
# a. Description: calculates the average value of a collection of values.
# b. Parameters: 1
# i. A collection of integers (list)
# c. Returns: 1
# i. The mean score (float)
def calculate_mean(integerslist):
    sum = 0
    for i in integerslist:
        sum += int(i)
    aveg = sum/(len(integerslist))
    return str(aveg)
# 3. find_movies_above_score()
# a. Description: from an initial list, retrieves a list of all the movies with scores above a certain value.
# b. Parameters: 2
# i. A collection of movies (list)
# ii. A score (float)
# c. Returns: 1
# i. A collection of all movies - in the format of [year, score, title] - with a score above the given score
# (list)
def find_movies_above_scores(listofmovies, score):
    goodmovie = [movie for movie in listofmovies if int(movie[1]) > float(score)]
    return goodmovie
# 4. main()
# a. Description: Primary entrypoint to your codebase.
# b. Parameters: 0
# c. Returns: 0
# d. Loads the contents of the file into two variables, and then analyzes that data and presents the results on the
# console.
def main():
    header, data = file_reader("deniro.csv")
    listofscore = [row[1] for row in data]
    average = calculate_mean(listofscore)
    good_movies = find_movies_above_scores(data, average)
    count = len(data)
    countoftotal = len(good_movies)
    # for i in data:
    #     countoftotal += 1# count of movies
    # for i in good_movies:
    #     count += 1# count of good movies
    print("I love Robert Deniro!")
    print("The average Rotten Tomatoes score for his movies is " + str(average) + ".")
    print("Of " + str(countoftotal) + " movies, " + str(count) + " are above average.")
    print("Here they are:")
    for i in header:
        print(i, end='')
    for movie in good_movies:
        for i in movie:
            print(i, end='')

main()