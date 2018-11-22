from tests.finiteAutomate_tests.afTestCase import AfTestCase


class SetupTestCase(AfTestCase):
    def test_setup_default(self):
        self.assertEqual(self.af.current_state.name, 'start')
        self.assertEqual(self.af.max_length, 0)
        self.assertListEqual(self.af.history, list())

    def test_setup_init_state(self):
        self.af.set_initial_state('middle')
        self.assertEqual(self.af.current_state.name, 'middle')
        self.af.set_initial_state('start')
        self.assertEqual(self.af.current_state.name, 'start')
