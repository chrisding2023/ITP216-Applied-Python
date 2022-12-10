# Class Swimmer
# Represents a swimmer athlete.
# Class Attributes
# All inherited class attributes, plus:
# 1. swimmer_count
# a. The number of swimmers created.
# Instance Attributes
# All inherited class attributes, plus:
# 1. self.strokes
# a. the strokes that the swimmer knows (list)
# Instance Methods
# All inherited instance methods, plus:
# 1. __init__()
# a. Description: Constructs a new Swimmer object.
# b. Parameters: 5
from Athlete import Athlete
class Swimmer(Athlete):
    swimmer_count = 0
    def __init__(self,name_param,dob_param,origin_param,medals_param,strokes):
        super().__init__(name_param,dob_param,origin_param,medals_param)
        self.strokes = strokes # list
        Swimmer.swimmer_count += 1
# i. name_param (String)
# ii. dob_param (String)
# iii. origin_param (String)
# iv. medals_param (list)
# v. strokes (list)
# c. Returns: 0
# d. Assigns parameters to instance attributes. Increases swimmer_count by 1
    def __str__(self):
        return self.name + " is a swimmer from " + self.origin + " born on " + self.dob + ". " + self.name + \
               " knows " + str(self.strokes) + ", and has won " + str(len(self.medals)) + " medals: " + str(self.medals) + "."
# 2. __str__()
# a. Description: retrieves data about the swimmer when printing.
# b. Parameters: 0
# c. Returns: 1
# i. Data about the swimmer. (String)
    def get_strokes(self):
        return self.strokes # get strokes
# 3. get_strokes()
# a. Description: retrieves the strokes attribute
# b. Parameters: 0
# c. Returns: 1
# i. self.strokes
    def add_stroke(self,new_stroke):
        if new_stroke not in self.strokes: # if the stroke is not already in the list, add a new stroke to stroke list
            self.strokes.append(new_stroke)
# 4. add_stroke()
# a. Description: adds a new stroke to the swimmer's repertoire. Checks to make sure the stroke is
# not already in the list
# b. Parameters: 1
# c. Returns: 0
