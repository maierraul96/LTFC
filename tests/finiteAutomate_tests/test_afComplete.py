import unittest

from finite_automate.core.finiteAutomate import AF


class TestAf(unittest.TestCase):
    af = AF()

    def setUp(self):
        self.af.load_states_from_file("resources/test_af.json")

    def test_something(self):
        self.assertEqual(self.af.verify('10001')[0], True)


