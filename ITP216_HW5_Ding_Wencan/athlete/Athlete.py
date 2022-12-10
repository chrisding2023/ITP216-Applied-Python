# Class Athlete
class Athlete(object):
    athlete_count = 0
# Represents a generic athlete.
# Class Attributes
# 1. athlete_count
# a. The number of athletes created.
# Instance Attributes
# 1. self.name
# a. the name of the athlete (String)
# 2. self.dob
# a. the date of birth of the athlete (String)
# 3. self.origin
# a. the country of origin of the athlete (String)
# 4. self.medals
# a. a list of medals the athlete has won (list)
    def __init__(self, name_param, dob_param, origin_param, medals_param):
        self.name = name_param # string
        self.dob = dob_param # string
        self.origin = origin_param # string
        self.medals = medals_param # list
        Athlete.athlete_count += 1 # athlete count increases by 1 everytime add a more athlete
# Instance Methods
# 1. __init__()
# a. Description: Constructs a new Athlete object.
# b. Parameters: 4
# i. name_param (String)
# ii. dob_param (String)
# iii. origin_param (String)
# iv. medals_param (list)
# c. Returns: 0
# d. Assigns parameters to instance attributes. Increases athlete_count by 1.
    def get_name(self):
        return self.name # get name
    def get_dob(self):
        return self.dob # get dob
    def get_origin(self):
        return self.origin # get origin
    def get_medals(self):
        return self.medals # get medals
# 2. Getters for all four instance attributes (name, dob, origin, medals)
# a. Description: retrieves an attribute
# b. Parameters: 0
# c. Returns: 1
# i. self.attribute
    def add_medal(self,medal_param):
        self.medals.append(medal_param) # add medals information to medal list
# 3. add_medal()
# a. Description: adds a new medal to the medal list
# b. Parameters: 1
# i. medal_param (String)
# c. Returns: 0