# Wencan Ding chrisdin@usc.edu
# ITP 216, Fall 2022
# Section: 32080
# Lab 6
# Description:
# to get comfortable with comprehensions and generators
# 1. Write a comprehension which creates a list (called sevens) consisting of all multiples of seven from 1 to
# 1000. For context: this list should be 142 items long.
def main():
    sevens = [i for i in range(1,1001) if i % 7 == 0]
# 2. Write a comprehension which creates a dictionary (called birdos) consisting of the following content
# (paired currently by index):
# name = ['Great potoo', 'Smew', 'Tundra bean goose', 'Southern pied
# babbler']
# genus_and_species = ['Nyctibius grandis', 'Mergellus albellus', 'Anser
# serrirostris', 'Turdoides bicolor']
    name = ['Great potoo', 'Smew', 'Tundra bean goose', 'Southern pied babbler']
    genus_and_species = ['Nyctibius grandis', 'Mergellus albellus', 'Anserserrirostris', 'Turdoides bicolor']
    my_dict = {name:genus_and_species for name,genus_and_species in zip(name,genus_and_species)}
# 3.Write a generator expression which creates a generator (called square_gen) which will yield two values:
# a number and its square. You can test it by running the following code:
# for number, square in square_gen:
# print(number, 'squared:', square)
    square_gen = ((number, number*number)for number in range(10))
    for number, square in square_gen:
        print(number, 'squared:', square)
if __name__ == "__main__":
    main()