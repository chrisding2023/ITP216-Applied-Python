# Wencan Ding chrisdin@usc.edu
# ITP 216, Fall 2022
# Section: 32080
# Lab 4
# Description:
# create a class called Arthropod which has the attributes and methods
# described in the requirements
#   Class Attributes
#   1.arthropod_count
#   a.The number of arthropods created.
import random
class Arthropod(object):
    arthropod_count = 0
    def __init__(self,name_param,limbs_count_param,color_param):
        self.name = name_param
        self.limbs = limbs_count_param
        self.color = color_param
        Arthropod.arthropod_count += 1
# Instance Attributes
# 1. self.name
# a. The name of the arthropod (string)
# 2. self.limbs
# a. The number of limbs the arthropod has (int)
# 3. self.color
# a. The color of the arthropod (String)
# 1. __init__()
# a. Description: Constructs a new arthropod object
# b. Parameters: 3
# i. name_param (String)
# ii. color_param (String)
# iii. limbs_count_param (int)
# c. Returns 0
# d. Assigns parameters to instance attributes. Increases arthropod arthropod_count by 1.
    def get_name(self):
        return self.name
# 2. get_name()
# a. Description: Retrieves arthropod name.
# b. Parameters: 0
# c. Returns: 1
# i. self.name instance attribute
    def get_color(self):
        return self.color
# 3. get_color()
# a. Description: Retrieves arthropod color.
# b. Parameters: 0
# c. Returns: 1
# i. self.color instance attribute
    def get_limbs_count(self):
        return self.limbs
# 4. get_limbs_count()
# a. Description: Retrieves arthropod limbs count.
# b. Parameters: 0
# c. Returns: 1
# i. self.limbs_count instance attribute
    def set_color(self,color_param):
        self.color = color_param
# 5. set_color()
# a. Description: Changes arthropod color.
# b. Parameters: 1
# i. A color (String)
# c. Returns: 0
    def lose_fight(self):
        random_num_limbs_to_lose = random.randint(0, self.limbs+1)
        self.limbs = self.limbs - random_num_limbs_to_lose
# 6. lose_fight()
# a. Description: arthropod potentially loses limbs.
# b. Parameters: 0
# c. Returns: 0
# d. Based on the number of existing limbs, randomly generate a number and lose that number of
# limbs. update self.limbs_count instance attribute.
def main():
    bug1 = Arthropod("bug1",6,"red")
    bug2 = Arthropod("bug2",8,"green")
    

main()