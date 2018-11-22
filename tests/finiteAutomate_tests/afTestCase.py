from unittest import TestCase

from finite_automate.core.finiteAutomate import AF


class AfTestCase(TestCase):
    af = None

    def setUp(self):
        self.af = AF()
        self.af.load_states_from_file("resources/test_af.json")
