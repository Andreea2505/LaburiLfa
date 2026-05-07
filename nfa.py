#nfa pe alfabetul {0,1} care accepta siruri care contin 101 sau se termina in 11
#avem o ramura care verifica daca contine 101
#o alta ramura verifica daca se termina in 11
class NFA:
    def __init__(self):
        self.start_state = "q0"
        self.accept_states = {"qF"}

        self.transitions = {

            # q0
            ("q0", "0"): {"q0"},
            ("q0", "1"): {"q0", "q1", "q3"},

            # cauta 101
            ("q1", "0"): {"q2"},
            ("q2", "1"): {"qF"},

            # se termina in 11
            ("q3", "1"): {"qF"},
        }

    def accepts(self, string):
        current_states = {self.start_state}

        for ch in string:
            next_states = set()

            for state in current_states:
                if (state, ch) in self.transitions:
                    next_states.update(
                        self.transitions[(state, ch)]
                    )

            current_states = next_states

        return any(
            state in self.accept_states
            for state in current_states
        )


nfa = NFA()

tests = [
    "101",
    "00101",
    "111",
    "10011",
    "10010",
    "000",
    "11",
]

for t in tests:
    print(f"{t}: {nfa.accepts(t)}")