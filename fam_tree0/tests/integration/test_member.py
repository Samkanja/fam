from unittest import TestCase
from src.member import Member, Gender


class TestMember(TestCase):
    def setUp(self):
        self.member = Member(1, "kanja", "Male")
        self.mother = Member(2, "Mother", "Female")
        self.father = Member(3, "Dad", "Male")
        self.mother_sis_1 = Member(4, "maternalAunt1", "Female")
        self.mother_sis_2 = Member(5, "MaternalAunt2", "Female")
        self.mother_bro_1 = Member(5, "MaternalUncle1", "Male")
        self.mother_bro_2 = Member(5, "MaternalUncle2", "Male")
        self.father_sis_1 = Member(4, "paternalAunt1", "Female")
        self.father_sis_2 = Member(5, "paternalAunt2", "Female")
        self.father_bro_1 = Member(5, "paternalUncle1", "Male")
        self.father_bro_2 = Member(5, "paternalUncle2", "Male")
        self.spouse = Member(12, "Wife", "Female")
        self.brother = Member(20, "Bro", "Male")
        self.brother1 = Member(21, "Bro1", "Male")
        self.sister = Member(23, "Sister", "Female")
        self.sister1 = Member(23, "Sister1", "Female")
        self.son = Member(25, "Son", "Male")
        self.son1 = Member(25, "Son1", "Male")
        self.daughter = Member(30, "Daughter", "Female")
        self.daughter1 = Member(32, "Daughter1", "Female")
        self.paternal_grandmother = Member(40, "Grandmother", "Female")
        self.maternal_grandmother = Member(40, "Grandmother1", "Female")

        self.member.set_mother(self.mother)
        self.member.set_father(self.father)
        self.father.add_child(self.brother)
        self.father.add_child(self.brother1)
        self.father.add_child(self.member)
        self.mother.add_child(self.brother)
        self.mother.add_child(self.member)
        self.mother.add_child(self.brother1)
        self.father.add_child(self.sister)
        self.father.add_child(self.sister1)
        self.mother.add_child(self.sister)
        self.mother.add_child(self.sister1)

        self.member.set_spouse(self.spouse)
        self.spouse.set_spouse(self.member)

        self.paternal_grandmother.add_child(self.father_bro_2)
        self.paternal_grandmother.add_child(self.father_bro_1)
        self.paternal_grandmother.add_child(self.father_sis_1)
        self.paternal_grandmother.add_child(self.father_sis_2)
        self.paternal_grandmother.add_child(self.father)
        self.father.set_mother(self.paternal_grandmother)

        self.maternal_grandmother.add_child(self.mother_bro_2)
        self.maternal_grandmother.add_child(self.mother_bro_1)
        self.maternal_grandmother.add_child(self.mother_sis_1)
        self.maternal_grandmother.add_child(self.mother_sis_2)
        self.maternal_grandmother.add_child(self.mother)
        self.mother.set_mother(self.maternal_grandmother)

        self.member.add_child(self.son)
        self.member.add_child(self.son1)
        self.member.add_child(self.daughter)
        self.member.add_child(self.daughter1)

    def test_set_method(self):

        self.assertEqual(self.member.mother.name, "Mother")
        self.assertEqual(self.member.father.name, "Dad")
        self.assertEqual(self.member in self.father.children, True)
        self.assertEqual(self.member in self.mother.children, True)
        self.assertEqual(self.member in self.member.mother.children, True)
        self.assertEqual(self.member in self.member.father.children, True)

        # testing paternal/maternal aunt and uncles
        self.assertEqual(len(self.member.mother.mother.children), 5)
        self.assertEqual(self.mother_bro_1 in self.member.mother.mother.children, True)
        self.assertEqual(self.mother_bro_2 in self.member.mother.mother.children, True)
        self.assertEqual(self.mother_sis_1 in self.member.mother.mother.children, True)
        self.assertEqual(self.mother_sis_2 in self.member.mother.mother.children, True)
        self.assertEqual(len(self.member.father.mother.children), 5)
        self.assertEqual(self.father_bro_2 in self.member.father.mother.children, True)
        self.assertEqual(self.father_bro_1 in self.member.father.mother.children, True)
        self.assertEqual(self.father_sis_2 in self.member.father.mother.children, True)
        self.assertEqual(self.father_sis_1 in self.member.father.mother.children, True)

        # testing spouse
        self.assertEqual(self.member.spouse.name, "Wife")

        ## test siblings
        self.assertEqual(len(self.member.mother.mother.children), 5)
        self.assertEqual(self.brother in self.member.mother.children, True)
        self.assertEqual(self.brother1 in self.member.mother.children, True)
        self.assertEqual(self.sister in self.member.mother.children, True)
        self.assertEqual(self.sister1 in self.member.mother.children, True)
        self.assertEqual(len(self.member.mother.mother.children), 5)
        self.assertEqual(self.brother in self.member.father.children, True)
        self.assertEqual(self.brother1 in self.member.father.children, True)
        self.assertEqual(self.sister in self.member.father.children, True)
        self.assertEqual(self.sister1 in self.member.father.children, True)

        # test children
        self.assertEqual(len(self.member.children), 4)
        self.assertEqual(self.son in self.member.children, True)
        self.assertEqual(self.son1 in self.member.children, True)
        self.assertEqual(self.daughter in self.member.children, True)
        self.assertEqual(self.daughter1 in self.member.children, True)

    def test_get_relationship(self):

        self.assertEqual(len(self.member.get_relationship("paternal_aunt")), 2)
        self.assertEqual(len(self.member.get_relationship("paternal_uncle")), 2)
        self.assertEqual(len(self.member.get_relationship("maternal_aunt")), 2)
        self.assertEqual(len(self.member.get_relationship("maternal_uncle")), 2)
        self.assertEqual(len(self.member.get_relationship("siblings")), 4)
        self.assertEqual(len(self.member.get_relationship("son")), 2)
        self.assertEqual(len(self.member.get_relationship("daughter")), 2)
        # import pdb

        # pdb.set_trace()
        self.assertEqual(len(self.member.spouse.get_relationship("brother_in_law")), 2)
        self.assertEqual(len(self.member.spouse.get_relationship("sister_in_law")), 2)
