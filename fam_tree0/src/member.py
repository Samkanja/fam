from enum import Enum, auto, StrEnum
class Gender(StrEnum):
    male = 'Male'
    female  = 'Female'



class Member:
    def __init__(self,id, name, gender):
        self.id = id
        self.name = name
        self.gender = Gender(gender)
        self.mother = None
        self.father = None
        self.spouse = None
        self.children = []


    def set_mother(self, mother):
        if not isinstance(mother, Member):
            raise ValueError('Invalid value for mother')
        if mother.gender != Gender.female:
            raise ValueError('ivnalid gender value for mother,\
                 mother should be female')
        self.mother = mother

    def set_father(self, father):
        if not isinstance(father, Member):
            raise ValueError('Invalid value for father')
        if father.gender != Gender.male:
            raise ValueError('ivnalid gender value for father,\
                 mother should be male')
        self.father = father

    




