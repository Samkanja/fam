from unittest import TestCase
from src.member import Member


class TestMember(TestCase):
    def setUp(self):
        self.member = Member()

    def test_initialization(self):
        self.assertEqual(isinstance(self.member, Member), True)