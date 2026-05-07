#pda laborator pentru limbajul L = {0^n 1^n | n >= 0}
class PushdownAutomaton:
    def __init__(self):
        self.stack = []
        self.initial_stack_symbol = '$'
        
    def reset(self):
        """Resetează stiva pentru un nou cuvânt."""
        self.stack = [self.initial_stack_symbol]

    def is_accepted(self, input_string):
        self.reset()
        current_state = 'q0'
        
        print(f"Procesare șir: '{input_string}'")
        print(f"Stare inițială: {current_state}, Stivă: {self.stack}")

        for char in input_string:
            # Tranziția din q0: citim '0', facem PUSH
            if current_state == 'q0' and char == '0':
                self.stack.append('0')
                # Rămânem în q0 sau trecem în q1 conform logicii tale
                # De obicei, q0 e pentru citit 0, q1 pentru citit 1
                print(f"Citit {char}: PUSH, Stivă: {self.stack}")

            # Tranziția către starea de procesare '1'
            elif (current_state == 'q0' or current_state == 'q1') and char == '1':
                current_state = 'q1'
                if len(self.stack) > 0 and self.stack[-1] != self.initial_stack_symbol:
                    self.stack.pop()
                    print(f"Citit {char}: POP,  Stivă: {self.stack}")
                else:
                    print(f"Eroare: Încercare de POP pe stivă goală sau simbol incorect!")
                    return False
            else:
                print(f"Eroare: Caracter neașteptat '{char}' sau secvență invalidă!")
                return False

        # Verificare finală (Golierea stivei de simbolul de bază $)
        if len(self.stack) == 1 and self.stack[-1] == self.initial_stack_symbol:
            # Trecem simbolic în starea de acceptare q_final
            print("Final: Stiva este curată. Șir ACCEPTAT.")
            return True
        else:
            print(f"Final: Stiva nu este goală corespunzător: {self.stack}. Șir RESPINS.")
            return False

# --- Testarea codului ---
pda = PushdownAutomaton()

test_strings = ["0011", "000111", "01", "001", "011"]

for s in test_strings:
    result = pda.is_accepted(s)
    print(f"Rezultat pentru '{s}': {'VALID' if result else 'INVALID'}")
    print("-" * 30)