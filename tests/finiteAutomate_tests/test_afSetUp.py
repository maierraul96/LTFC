from tests.finiteAutomate_tests.afTestCase import AfTestCase


class MyTestCase(AfTestCase):
    def test_setup(self):
        self.assertEqual(self.af.current_state.name, 'start')
        self.assertEqual(self.af.max_length, 0)
        self.assertListEqual(self.af.history, list())
