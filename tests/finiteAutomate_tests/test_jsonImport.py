from lexical_analyser.core.finiteAutomate import StateType
from tests.finiteAutomate_tests.afTestCase import AfTestCase


class JsonImportTest(AfTestCase):

    def test_count_states(self):
        self.assertEqual(len(self.af.states), 3)

    def test_states_name(self):
        self.assertSequenceEqual(list(self.af.states.keys()),
                             ['start', 'middle', 'end'])
        self.assertEqual(self.af.states['start'].name, 'start')
        self.assertEqual(self.af.states['middle'].name, 'middle')
        self.assertEqual(self.af.states['end'].name, 'end')

    def test_transitions(self):
        self.assertListEqual(self.af.states['start'].transitions[0].conditions,
                             ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        self.assertListEqual(self.af.states['start'].transitions[1].conditions,
                             ["."])
        self.assertListEqual(self.af.states['middle'].transitions[0].conditions,
                             ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        self.assertListEqual(self.af.states['end'].transitions[0].conditions,
                             ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

        self.assertEqual(self.af.states['start'].transitions[0].next_state, 'start')
        self.assertEqual(self.af.states['start'].transitions[1].next_state, 'middle')
        self.assertEqual(self.af.states['middle'].transitions[0].next_state, 'end')
        self.assertEqual(self.af.states['end'].transitions[0].next_state, 'end')

    def test_states_type(self):
        self.assertListEqual(self.af.states['start'].state_type, [StateType.INITIAL, StateType.TERMINAL])
        self.assertListEqual(self.af.states['middle'].state_type, [])
        self.assertListEqual(self.af.states['end'].state_type, [StateType.TERMINAL])


class MyTestCase(AfTestCase):
    def test_setup(self):
        self.assertEqual(self.af.current_state.name, 'start')
        self.assertEqual(self.af.max_length, 0)
        self.assertListEqual(self.af.history, list())
