import unittest
from lexical_analyser.core.finiteAutomate import AF, StateType


class JsonImportTest(unittest.TestCase):
    af = None

    def setUp(self):
        self.af = AF()

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
