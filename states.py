class State:
    def __init__(self, state_list):
        self.states = state_list
        self.state = self.states[0]

    def set_state(self, state):
        if type(state) == str:
            self.state = state

        if type(state) == int:
            self.state = self.states[state]
