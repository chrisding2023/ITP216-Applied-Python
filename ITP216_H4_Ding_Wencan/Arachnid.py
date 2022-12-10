# Wencan Ding chrisdin@usc.edu
# ITP 216, Fall 2022
# Section: 32080
# Assignment 4
# Description:
# use arthopod, arachnid, insect class to create a very bad ripoff
# of Pokémon
from Arthropod import Arthropod
class Arachnid(Arthropod):
    arachnid_count = 0
    def __init__(self,name_param,color_param,limbs_count_param,venomous_param):
        super().__init__(name_param,color_param,limbs_count_param)
        self.venomous = venomous_param
        Arachnid.arachnid_count += 1
# Class Attributes
# All inherited class attributes, plus:
# 1. arachnid_count
# a. The number of arachnids created.
# Instance Attributes
# All Inherited instance attributes, plus:
# 1. self.venomous
# a. Whether or not the arachnid is venomous (Boolean)
# Instance Methods
# All inherited instance methods, plus:
# 1. __init__()
# a. Description: Constructs a new Arachnid object.
# b. Parameters: 4
# i. name_param (String)
# ii. color_param (String)
# iii. limbs_count_param (int)
# iv. venomous_param (bool)
# c. Returns: 0
# d. Inherits from Arthropod and extends functionality. Assigns parameters to instance attributes. Increases
# arachnid_count by 1.
    def __str__(self):
        if self.venomous == True:
            return "The " + self.color + " venomous " + self.name + " has " + str(self.limbs) + " limbs."
        else:
            return "The " + self.color + " non-venomous " + self.name + " has " + str(self.limbs) + " limbs."
# 2. __str__()
# a. Description: retrieves data about the arachnid when printing.
# b. Parameters: 0
# c. Returns: 1
# i. Data about the arachnid, such as: "The gray non-venomous wolf spider has 8
# limbs." (String)
    def get_venomous(self):
        return self.venomous(bool)

# 3. get_venomous()
# a. Description: retrieves whether or not the arachnid is venomous
# b. Parameters: 0
# c. Returns: 1
# i. self.venomous attribute (Boolean)
    def get_power(self):
        if self.venomous == True:
            return self.limbs*2
        else:
            return self.limbs
# 4. get_power()
# a. Description: retrieves the power of the arachnid
# b. Parameters: 0
# c. Returns: 1
# i. if the arachnid is venomous, then return self.limbs*2 ; otherwise, just return self.limbs

