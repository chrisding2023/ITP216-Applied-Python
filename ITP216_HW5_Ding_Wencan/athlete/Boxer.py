# Class Boxer
from Athlete import Athlete
class Boxer(Athlete):
    boxer_count = 0
# Represents a boxer athlete.
# Class Attributes
# All inherited class attributes, plus:
# 1. boxer_count
# a. The number of boxers created.
# Instance Attributes
# All inherited class attributes, plus:
# 1. self.weight_class
# a. the weight class of the boxer (String)
# 2. self.record
# a. the fight record of the boxer (list with two items: [wins (int), losses (int)] )
    def __init__(self,name_param,dob_param,origin_param,medals_param,weight_class,record_param):
        super().__init__(name_param,dob_param,origin_param,medals_param) # super method to inherit class attributes
        self.weight_class = weight_class # string
        self.record = record_param # list(int(win),int(lose)
        Boxer.boxer_count += 1 # boxer count increase by 1 every time use class
# Instance Methods
# All inherited instance methods, plus:
# 1. __init__()
# a. Description: Constructs a new Boxer object.
# b. Parameters: 5
# i. name_param (String)
# ii. dob_param (String)
# iii. origin_param (String)
# iv. medals_param (list)
# v. weight_class (String)
    def __str__(self):
        return self.name + " is a " + self.weight_class + " boxer from " + self.origin + " born on " + self.dob + ". " + \
               self.name + " has a " + str(self.record[0]) + "-" + str(self.record[1]) + " record, and has won " + \
               str(len(self.medals)) + " medals: " + str(self.medals)
# 2. __str__()
# a. Description: retrieves data about the boxer when printing.
# b. Parameters: 0
# c. Returns: 1
# i. Data about the boxer. (String)
    def get_weight_class(self):
        return self.weight_class # get weight class
    def get_record(self):
        return self.record # get record of boxer
# 3. Getters for the two new instance attributes (weight_class, record)
# a. Description: retrieves an attribute
# b. Parameters: 0
# c. Returns: 1
# i. self.attribute
    def set_weight_class(self,weight_class_param):
        self.weight_class = weight_class_param
        return self.weight_class # set new weight class
# 4. set_weight_class()
# a. Description: sets an attribute
# b. Parameters: 1
# i. weight_class_param (String)
# c. Returns: 0
    def win_fight(self):
        self.record[0] += 1 # add one win to record
# 5. win_fight()
# a. Description: adds one to the wins of the boxer's record
# b. Parameters: 0
# c. Returns: 0
    def lose_fight(self):
        self.record = self.record[1] + 1 # add one lose to record
        if self.record[1] >= 10: # check if the boxer needs to retire when the losses of the boxer's record is larger than 10
            return "This boxer has retired."
        else:
            return "The number of fights left before retirement for this boxer:", str(10-self.record[1])
# 6. lose_fight()
# a. Description: adds one to the losses of the boxer's record, then checks to see if the boxer needs to
# retire (after 10 losses)
# b. Parameters: 0
# c. Returns: 1:
# i. A message about the number of fights left before retirement, or 'This boxer has retired.'
# (String)



