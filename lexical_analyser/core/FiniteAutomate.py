class StateType:
    INITIAL = "INITIAL"
    TERMINAL = "TERMINAL"


class State:
    state_type = list()
    name = None
    transitions = None

    def __init__(self, state_type, transitions):
        self.state_type = state_type
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

    def load_states(self, states):
        self.states = states
        self.current_state = self.states[[state for state, value in states.items() if StateType.INITIAL in value.state_type][0]]

    @staticmethod
    def classify_json(states):
        output = dict()
        for state, values in states.items():
            transitions = list()
            for trans in values["transitions"]:
                transitions.append(Transition(trans["next_state"], trans["conditions"]))
            output[state] = (State(values["state_type"], transitions))
        return output

    def load_states_from_file(self, path):
        import json
        with open(path) as file:
            states = json.load(file)
            self.load_states(self.classify_json(states))

    def set_input(self, input_seq):
        self.input_seq = input_seq
        self.max_length = 0

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
                print("Max valid sequence length: {}".format(self.max_length))
                return False
        if StateType.TERMINAL in self.current_state.state_type:
            print("Valid sequence")
            return True
        else:
            print("Left in non-terminal state. Length: {}".format(self.max_length))
            return False

