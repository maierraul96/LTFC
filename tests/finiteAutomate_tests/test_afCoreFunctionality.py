from tests.finiteAutomate_tests.afTestCase import AfTestCase


class CoreTests(AfTestCase):
    def test_step_c1(self):
        self.af.set_input('101')
        self.assertEqual(self.af.current_state.name, 'start')
        self.assertListEqual(self.af.history, [])

        self.assertEqual(self.af.step(), True)
        self.assertEqual(self.af.input_seq, '01')
        self.assertEqual(self.af.current_state.name, 'start')
        self.assertListEqual(self.af.history, ['start'])

        self.assertEqual(self.af.step(), True)
        self.assertEqual(self.af.input_seq, '1')
        self.assertEqual(self.af.current_state.name, 'start')
        self.assertListEqual(self.af.history, ['start', 'start'])

        self.assertEqual(self.af.step(), True)
        self.assertEqual(self.af.input_seq, '')
        self.assertEqual(self.af.current_state.name, 'start')
        self.assertListEqual(self.af.history, ['start', 'start', 'start'])

    def test_step_c2(self):
        self.af.set_input('1.1')
        self.assertEqual(self.af.current_state.name, 'start')
        self.assertListEqual(self.af.history, [])

        self.assertEqual(self.af.step(), True)
        self.assertEqual(self.af.input_seq, '.1')
        self.assertEqual(self.af.current_state.name, 'start')
        self.assertListEqual(self.af.history, ['start'])

        self.assertEqual(self.af.step(), True)
        self.assertEqual(self.af.input_seq, '1')
        self.assertEqual(self.af.current_state.name, 'middle')
        self.assertListEqual(self.af.history, ['start', 'start'])

        self.assertEqual(self.af.step(), True)
        self.assertEqual(self.af.input_seq, '')
        self.assertEqual(self.af.current_state.name, 'end')
        self.assertListEqual(self.af.history, ['start', 'start', 'middle'])

    def test_step_c3(self):
        self.af.set_input('1.1.1')

        self.assertEqual(self.af.step(), True)
        self.assertEqual(self.af.input_seq, '.1.1')
        self.assertEqual(self.af.current_state.name, 'start')
        self.assertListEqual(self.af.history, ['start'])

        self.assertEqual(self.af.step(), True)
        self.assertEqual(self.af.input_seq, '1.1')
        self.assertEqual(self.af.current_state.name, 'middle')
        self.assertListEqual(self.af.history, ['start', 'start'])

        self.assertEqual(self.af.step(), True)
        self.assertEqual(self.af.input_seq, '.1')
        self.assertEqual(self.af.current_state.name, 'end')
        self.assertListEqual(self.af.history, ['start', 'start', 'middle'])

        self.assertEqual(self.af.step(), False)
        self.assertEqual(self.af.input_seq, '.1')
        self.assertEqual(self.af.current_state.name, 'end')
        self.assertListEqual(self.af.history, ['start', 'start', 'middle'])

        self.assertEqual(self.af.step(), False)
        self.assertEqual(self.af.current_state.name, 'end')
        self.assertListEqual(self.af.history, ['start', 'start', 'middle'])

    def test_step_c4(self):
        self.af.set_input('i123')
        self.assertEqual(self.af.step(), False)
        self.assertEqual(self.af.input_seq, 'i123')

    def test_step_c5(self):
        self.af.set_input('0')
        self.assertEqual(self.af.step(), True)
        self.assertEqual(self.af.input_seq, '')

        with self.assertRaises(ValueError) as error:
            self.af.step()
        the_exception = error.exception
        self.assertEqual(str(the_exception), 'Input sequence terminated')
