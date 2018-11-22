from tests.finiteAutomate_tests.afTestCase import AfTestCase


class InputTest(AfTestCase):

    def setUp(self):
        super().setUp()
        self.af.set_initial_state('middle')
        self.assertEqual(self.af.current_state.name, 'middle')

    def test_input_reset(self):
        self.af.set_input('101')
        self.assertEqual(self.af.current_state.name, 'start')
        self.assertEqual(self.af.max_length, 0)
        self.assertListEqual(self.af.history, list())

    def test_input_seq(self):
        self.af.set_input('101')
        self.assertEqual(self.af.input_seq, '101')
        self.af.set_input('')
        self.assertEqual(self.af.input_seq, '')
        self.af.set_input('1.0')
        self.assertEqual(self.af.input_seq, '1.0')

    def tearDown(self):
        super().tearDown()
        self.af.set_initial_state('start')
        self.assertEqual(self.af.current_state.name, 'start')


class GetterTest(AfTestCase):

    def test_get_states_names(self):
        self.assertSequenceEqual(self.af.get_states_names(), ['start', 'middle', 'end'])

    def test_get_transitions(self):
        self.assertSequenceEqual(self.af.get_transitions(),
                                 ['start --(0)--> start',
                                  'start --(1)--> start',
                                  'start --(2)--> start',
                                  'start --(3)--> start',
                                  'start --(4)--> start',
                                  'start --(5)--> start',
                                  'start --(6)--> start',
                                  'start --(7)--> start',
                                  'start --(8)--> start',
                                  'start --(9)--> start',
                                  'start --(.)--> middle',
                                  'middle --(0)--> end',
                                  'middle --(1)--> end',
                                  'middle --(2)--> end',
                                  'middle --(3)--> end',
                                  'middle --(4)--> end',
                                  'middle --(5)--> end',
                                  'middle --(6)--> end',
                                  'middle --(7)--> end',
                                  'middle --(8)--> end',
                                  'middle --(9)--> end',
                                  'end --(0)--> end',
                                  'end --(1)--> end',
                                  'end --(2)--> end',
                                  'end --(3)--> end',
                                  'end --(4)--> end',
                                  'end --(5)--> end',
                                  'end --(6)--> end',
                                  'end --(7)--> end',
                                  'end --(8)--> end',
                                  'end --(9)--> end'])

    def test_get_alphabet(self):
        self.assertSequenceEqual(self.af.get_alphabet(),
                                 ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."])

    def test_get_final_states(self):
        self.assertSequenceEqual(self.af.get_final_states(), ['start', 'end'])
