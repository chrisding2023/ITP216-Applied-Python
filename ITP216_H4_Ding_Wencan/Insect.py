# Class Insect
import random
from Arthropod import Arthropod
class Insect(Arthropod):
    insect_count = 0
    def __init__(self,name_param,color_param,limbs_count_param,wings_count_param):
        super().__init__(name_param,color_param,limbs_count_param)
        self.wings_count = wings_count_param
        Insect.insect_count += 1

# Class Attributes
# All inherited class attributes, plus:
# 1. insect_count
# a. The number of insects created.
# Instance Attributes
# All Inherited instance attributes, plus:
# 1. self.wings_count
# a. The number of wings on the insect (int)
# Instance Methods
# All inherited instance methods, plus:
# 1. __init__()
# a. Description: Constructs a new Insect object.
# b. Parameters: 4
# i. name_param (String)
# ii. color_param (String)
# iii. limbs_count_param (int)
# iv. wings_count_param (int)
# c. Returns 0
# d. Inherits from Arthropod and extends functionality. Assigns parameters to instance attributes. Increases
# insect_count by 1.
    def __str__(self):
        return "The " + self.color + " " + self.name + " has " + str(self.limbs) + " limbs and " + str(self.wings_count) + " wings."
# 2. __str__()
# a. Description: retrieves data about the insect when printing.
# b. Parameters: 0
# c. Returns: 1
# i. Data about the arachnid, such as: "The silver mosquito has 6 limbs and 2
# wings." (String)
    def get_wings_count(self):
        return self.wings_count
# 3. get_wings_count()
# a. Description: Retrieves insect wings count.
# b. Parameters: 0
# c. Returns: 1
# i. self.wings_count instance attribute
    def get_power(self):
        return self.limbs + self.wings_count(int)
# 4. get_power()
# a. Description: retrieves the power of the insect
# b. Parameters: 0
# c. Returns: 1
# i. self.limbs_count + self.wings_count (int)
    def lose_fight(self):
        super().lose_fight()
        random_num_wings_to_lose = random.randint(0, self.wings_count)
        self.wings_count = self.wings_count - random_num_wings_to_lose
# 5. lose_fight()
# a. Description: insect potentially loses limbs and wings.
# b. Parameters: 0
# c. Returns: 0
# d. Inherits from Arthropod to potentially lose limbs. Additionally, based on the number of existing wings,
# randomly generate a number and lose that number of wings. update self.wings_count instance
# attribute.