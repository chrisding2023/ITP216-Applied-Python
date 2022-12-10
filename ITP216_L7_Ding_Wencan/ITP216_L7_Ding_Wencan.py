# Wencan Ding chrisdin@usc.edu
# ITP 216, Fall 2022
# Section: 32080
# Lab 7
# 1. Write a decorator function validator_decorator which will validate the decorated function's input:
# a. All the decorated function's args should be strings.
# b. All the decorated function's kwargs values should be dictionaries with two key:value pairs.
# c. Display a message informing the user of whether or not the decorated function's arguments pass the test.
# 2. Write a function to be decorated called print_all_the_things() which prints out the args all on one line, and
# the kwargs' key:value pairs on separate, indented lines. You will use this to test your validator decorator.
# 3. Decorate the function from #2 with the decorator from #1.
def validator_decorator(func):
    def wrapper(*args, **kwargs):
        print("Testing arguments:")
        isString = ""
        for s in args:
            if type(s) is not str:
                isString = " not"
                break
        twokeys = ""
        for k, v in kwargs.items():
            if len(v)!= 2:
                twokeys = " not"
        print("Arguments accepted:"+isString+" all args are Strings, and"+twokeys+" all kwargs have two key:value pairs.")
        print("Printing args:")
        for s in args:
            print('\t',s)
        print("Printing kwargs:")
        for k, v in kwargs.items():
            print('\t',k,":", v)
        func(*args, **kwargs)
    return wrapper


@validator_decorator
def print_all_the_things(*args, **kwargs):
    print("Running function: ")
    print("This will print all the things:")
    for s in args:
        print(s, end=" ")
    print("")
    for k, v in kwargs.items():
        for key, value in v.items():
            print('\t',key,":",value)

def main():
    print_all_the_things('Another', "Lab", "involving", "animals.", animal={"cat":True, "dog":False})
    print("-----------------")
    print_all_the_things('Never', "eat", "Shregded", "meat.", animal={"cat": True, "dog": False, "hamster": "never"})

if __name__ == '__main__':
    main()
