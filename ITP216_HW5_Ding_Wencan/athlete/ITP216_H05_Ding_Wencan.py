
from Swimmer import Swimmer
from Boxer import Boxer

def main():
    swimmer1 = Swimmer("Dave Thomas", "1932/07/02", "USA", ['Silver (1992)', 'Gold (1996)'],
                           ['freestyle', 'breaststroke'])
    boxer1 = Boxer("Mary Berry", "1935/03/24", "the UK", ['Gold (2012)', 'Gold (2016)'], "Light Flyweight", [14, 0])
    print(boxer1)  # print the information of boxer1
    print(swimmer1)  # print the information of boxer2


if __name__ == "__main__":
    main()