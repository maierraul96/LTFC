from tests.finiteAutomate_tests.afTestCase import AfTestCase


class SetupTestCase(AfTestCase):
    def test_setup_default(self):
        self.assertEqual(self.af.current_state.name, 'start')
        self.assertEqual(self.af.max_length, 0)
        self.assertEqual(self.af.msg, '')
        self.assertEqual(self.af.acceptance, None)
        self.assertListEqual(self.af.history, list())

    def test_setup_init_state(self):
        self.af.set_initial_state('middle')
        self.assertEqual(self.af.current_state.name, 'middle')
        self.af.set_initial_state('start')
        self.assertEqual(self.af.current_state.name, 'start')

    def test_setup_reset(self):
        self.af.current_state = 'Test_data'
        self.af.max_length = 'Test_data'
        self.af.msg = 'Test_data'
        self.af.acceptance = 'Test_data'
        self.af.history = 'Test_data'

        self.af.setup()

        self.assertEqual(self.af.current_state.name, 'start')
        self.assertEqual(self.af.max_length, 0)
        self.assertEqual(self.af.msg, '')
        self.assertEqual(self.af.acceptance, None)
        self.assertListEqual(self.af.history, list())
