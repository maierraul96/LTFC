class StateType:
    INITIAL = "INITIAL"
    TERMINAL = "TERMINAL"


class State:
    state_type = list()
    name = None
    transitions = None

    def __init__(self, state_type, name, transitions):
        self.state_type = state_type
        self.name = name
        self.transitions = transitions


class Transition:
    def __init__(self, next_state, conditions):
        self.next_state = next_state
        self.conditions = conditions


class AF:
    def __init__(self):
        self.states = None
        self.current_state = None
        self.input_seq = None
        self.max_length = 0
        self.history = list()

    def load_states(self, states):
        self.states = states
        self.setup()

    def set_initial_state(self, state=None):
        if state is None:
            self.current_state = list(filter(lambda st: StateType.INITIAL in st.state_type, self.states.values()))[0]
        else:
            self.current_state = self.states[state]

    def setup(self):
        self.set_initial_state()
        self.max_length = 0
        self.history = list()

    @staticmethod
    def classify_json(states):
        output = dict()
        for state, values in states.items():
            transitions = list()
            for trans in values["transitions"]:
                transitions.append(Transition(trans["next_state"], trans["conditions"]))
            output[state] = (State(values["state_type"], state, transitions))
        return output

    def load_states_from_file(self, path):
        import json
        with open(path) as file:
            states = json.load(file)
            self.load_states(self.classify_json(states))

    def set_input(self, input_seq):
        self.input_seq = input_seq
        self.setup()

    def step(self):
        if len(self.input_seq):
            valid_transition = list(filter(lambda x: self.input_seq[0] in x.conditions, self.current_state.transitions))
            if len(valid_transition):
                self.input_seq = self.input_seq[1:]
                self.current_state = self.states[valid_transition[0].next_state]
                self.max_length += 1
                return 0
            else:
                return 1
        else:
            raise ValueError("Input sequence terminated")

    def digest(self):
        while len(self.input_seq):
            if self.step() == 1:
                return False, "Max valid sequence length: {}".format(self.max_length)
        if StateType.TERMINAL in self.current_state.state_type:
            return True, "Valid sequence"
        else:
            return False, "Left in non-terminal state. Length: {}".format(self.max_length)

    def get_max_length(self):
        return self.max_length

    def get_states_names(self):
        return self.states.keys()

    def get_transitions(self):
        transitions = list()
        for state in self.states.keys():
            for state_trans in self.states[state].transitions:
                for element in state_trans.conditions:
                    transitions.append(str(state + " --(" + element + ")--> " + state_trans.next_state))
        return transitions

    def get_alphabet(self):
        alphabet = list()
        for state in self.states.keys():
            for state_trans in self.states[state].transitions:
                for element in state_trans.conditions:
                    if element not in alphabet:
                        alphabet.append(element)
        return alphabet

    def get_final_states(self):
        states = list()
        for state in self.states.keys():
            if StateType.TERMINAL in self.states[state].state_type:
                states.append(state)
        return states
