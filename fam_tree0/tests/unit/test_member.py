from unittest import TestCase
from src.member import Member, Gender


class TestMember(TestCase):
    def setUp(self):
        self.member = Member(1, "Zim", "Male")

    def test_initialization(self):
        self.assertEqual(isinstance(self.member, Member), True)

        self.assertEqual(self.member.id, 1)
        self.assertEqual(self.member.name, 'Zim')
        self.assertEqual(self.member.gender, Gender.male)
        self.assertEqual(self.member.mother, None)
        self.assertEqual(self.member.mother, None)
        self.assertEqual(self.member.father, None)
        self.assertEqual(self.member.spouse, None)
        self.assertEqual(self.member.children, [])

        # edge case for gender
        self.assertRaises(ValueError, Member, 1, "SomeOtherGuys", "Queer")

    def test_set_mother(self):
        mother_demo1 = 'mother_demo1'
        mother_demo2 = Member(2, 'motherdenm3', "Male")
        mother_demo3 = Member(3, "Mom", "Female")

        # Error Cases
        self.assertRaises(ValueError, self.member.set_mother, mother_demo1)
        self.assertRaises(ValueError, self.member.set_mother, mother_demo2)

        # 
        self.member.set_mother(mother_demo3)
        self.assertEqual(self.member.mother.name, "Mom")
        self.assertEqual(self.member.mother.gender, Gender.female)
    
    def test_set_father(self):
        father_demo1 = 'father_demo1'
        father_demo2 = Member(2, 'fatherdenm3', "Female")
        father_demo3 = Member(3, "Dad", "Male")

        # Error Cases
        self.assertRaises(ValueError, self.member.set_father, father_demo1)
        self.assertRaises(ValueError, self.member.set_father, father_demo2)

        # 
        self.member.set_father(father_demo3)
        self.assertEqual(self.member.father.name, "Dad")
        self.assertEqual(self.member.father.gender, Gender.male)

