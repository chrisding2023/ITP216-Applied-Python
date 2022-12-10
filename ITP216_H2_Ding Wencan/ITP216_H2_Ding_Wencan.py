# Wencan Ding chrisdin@usc.edu
# ITP 216, Fall 2022
# Section: 32080
# Assignment 2
# Description:
# Describe what this program does in your own words.
# This program display setup for pet collections
# cats_names = ('Cassandra', 'Sir Whiskington', 'Truck')
# dogs_names = {'Barkey McBarkface', 'Leeloo Dallas', 'Taro'}
# parrots_names = ['Squawk', 'Squawk 2: the Squawkquel', 'Larry']
# names = ['peter', 'paul', 'mary']
# animals = ('cat', 'cat', 'hamster')
def main():
# dict = {"cat":["Cassandra", "Sir Whiskington", "Truck", "peter", "paul"],"dog":["Barkey McBarkface", "Leeloo Dallas","Taro"],
# "parrot":["Squawk","Squawk 2: the Squawkquel", "Larry"],"hamster":["mary"]}
    # list of collections
    cats_names = ('Cassandra', 'Sir Whiskington', 'Truck')
    dogs_names = {'Barkey McBarkface', 'Leeloo Dallas', 'Taro'}
    parrots_names = ['Squawk', 'Squawk 2: the Squawkquel', 'Larry']
    names = ['peter', 'paul', 'mary']
    animals = ('cat', 'cat', 'hamster')
    # change the set into set
    ani = list(animals)
    # put the collections into different lists
    catlist = []
    doglist = []
    parrotlist = []
    dogs_list = list(dogs_names)
    for i in range(0,len(cats_names)):
        catlist.append(cats_names[i])
    for i in range(0,len(dogs_list)):
        doglist.append(dogs_list[i])
    for i in range(0,len(parrots_names)):
        parrotlist.append(parrots_names[i])
    # create the dictionary
    dict = {"cat": catlist, "dog": doglist, "parrot": parrotlist}
    # append the animal name according to their category into the dictionary
    for i in range(0, len(ani)):
        if ani[i] not in dict.keys():
            namel= []
            namel.append(names[i])
            dict[ani[i]] = namel
        else:
            dict[ani[i]].append(names[i])
    # while loop condition
    print("Hi, Kristof!")
    F = True
    while F == True:
        print("\nPlease choose from the following options:")
        print("1. See all your pets' names.")
        print("2. Add a pet.")
        print("3. Exit.")
        answer = input("What would you like to do? (1, 2, 3): ")
        if answer == "1":# count the total number of pets
            count = 0
            for i in dict:
                count += len(dict[i])
            print("You have " + str(count) + " pets")
            animallist = list(dict.keys())
            namelist = list(dict.values())
            # print all the pets
            for i in range(0,len(animallist)):
                print(animallist[i] + ": " + str(namelist[i]))
        # add pet into collection
        elif answer == "2":
            animal = input("\nWhat kind of animal is this?")
            name = input("\nWhat is the name of the " + animal + "?")
            print("\nGreat! " + name + " the " + animal + " is added to your pets.")
            if animal not in dict.keys():
                namelist1 = []
                namelist1.append(name)
                dict[animal] = namelist1
            else:
                dict[animal].append(name)
        # exit
        elif answer == "3":
            print ("Goodbye!")
            F = False
        else:
            print("\nThat's not a number.")
main()



