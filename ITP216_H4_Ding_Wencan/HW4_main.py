# main
import random
# from file import class
from Arthropod import Arthropod
from Arachnid import Arachnid
from Insect import Insect
# fight fuction: decide who is the winner or tie
def fight(arthropod1,arthropod2,Tier):
    winner = random.choice([arthropod1,arthropod2,Tier])
    return winner
def main():
    arthropod1 = Arachnid("wolf spider", 8,"gray",False)
    arthropod2 = Insect("mosquito",6,"silver",2)
    print("Your contenders:")
    print(Arachnid.__str__(self=arthropod1))# print the information of arthropod1
    print(Insect.__str__(self=arthropod2))# print the information of arthropod2
    print("\n")
    cont = True
    count = 0
    tier = "tie"
    while cont == True:# while loop to continue the fight
        count += 1
        winner = fight(arthropod1.name,arthropod2.name,tier)# use fight function
        if winner == arthropod1.name:# the first situation
            print("Round",count, ": The", winner, "wins this round!")
            Insect.lose_fight(arthropod2)# use class lose fight
            print(Insect.__str__(self=arthropod2))
        if winner == arthropod2.name:# the second situation
            print("Round",count, ": The", winner, "wins this round!")
            Arachnid.lose_fight(arthropod1)# use class lose fight
            print(Arachnid.__str__(self=arthropod1))
        if arthropod1.get_limbs_count() == 0:# to see limbs count is below 0 to stop fight
            print("\nThere is a winner!")
            print(Insect.__str__(self=arthropod2))
            cont = False
        if arthropod2.get_limbs_count() ==0 and arthropod2.get_wings_count() == 0:# to see limbs and wings count is below to stop fight
            print("\nThere is a winner!")
            print(Arachnid.__str__(self=arthropod1))
            cont = False
        if winner == tier:# the third situation tie
            print("Round",count,":    This round was a tie!")

main()
