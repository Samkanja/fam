from unittest import TestCase
from src.member import Member, Gender


class TestMember(TestCase):
    def setUp(self):
        self.member = Member(1, "Zim", "Male")

    def test_initialization(self):
        self.assertEqual(isinstance(self.member, Member), True)

        self.assertEqual(self.member.id, 1)
        self.assertEqual(self.member.name, "Zim")
        self.assertEqual(self.member.gender, Gender.male)
        self.assertEqual(self.member.mother, None)
        self.assertEqual(self.member.mother, None)
        self.assertEqual(self.member.father, None)
        self.assertEqual(self.member.spouse, None)
        self.assertEqual(self.member.children, [])

        # edge case for gender
        self.assertRaises(ValueError, Member, 1, "SomeOtherGuys", "Queer")

    def test_set_mother(self):
        mother_demo1 = "mother_demo1"
        mother_demo2 = Member(2, "motherdenm3", "Male")
        mother_demo3 = Member(3, "Mom", "Female")

        # Error Cases
        self.assertRaises(ValueError, self.member.set_mother, mother_demo1)
        self.assertRaises(ValueError, self.member.set_mother, mother_demo2)

        #
        self.member.set_mother(mother_demo3)
        self.assertEqual(self.member.mother.name, "Mom")
        self.assertEqual(self.member.mother.gender, Gender.female)

    def test_set_father(self):
        father_demo1 = "father_demo1"
        father_demo2 = Member(2, "fatherdenm3", "Female")
        father_demo3 = Member(3, "Dad", "Male")

        # Error Cases
        self.assertRaises(ValueError, self.member.set_father, father_demo1)
        self.assertRaises(ValueError, self.member.set_father, father_demo2)

        #
        self.member.set_father(father_demo3)
        self.assertEqual(self.member.father.name, "Dad")
        self.assertEqual(self.member.father.gender, Gender.male)

    def test_set_spouse(self):
        spouse_demo1 = "spouse_demo1"
        spouse_demo2 = Member(2, "spousedenm3", "Male")
        spouse_demo3 = Member(3, "Spouse", "Female")

        # Error Cases
        self.assertRaises(ValueError, self.member.set_spouse, spouse_demo1)
        self.assertRaises(ValueError, self.member.set_spouse, spouse_demo2)

        #
        self.member.set_spouse(spouse_demo3)
        self.assertEqual(self.member.spouse.name, "Spouse")
        self.assertEqual(self.member.spouse.gender, Gender.female)

    def test_add_child(self):
        child_demoa = "child_demoa"
        child_demob = Member(4, "Daughter", "Female")

        # error case
        self.assertRaises(ValueError, self.member.add_child, child_demoa)

        # success rate
        self.member.add_child(child_demob)
        self.assertEqual(len(self.member.children), 1)
        self.assertEqual(self.member.children[0].name, "Daughter")
        self.assertEqual(self.member.children[0].gender, Gender.female)

    def test_get_paternal_grandmother(self):
        member = Member(9, "Newmember", "Male")
        father = Member(10, "Newmeber2", "Male")
        grandmother = Member(11, "Newmember_grandmother", "Female")

        self.assertEqual(member.get_paternal_grandmother(), None)

        member.father = father
        self.assertEqual(member.get_paternal_grandmother(), None)

        member.father.mother = grandmother
        self.assertEqual(member.get_paternal_grandmother(), grandmother)
