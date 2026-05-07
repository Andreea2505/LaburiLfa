#dfa care accepta siruri de 0 si 1 care se termina in 1 
# stari
#qo->ultima cifra citita este 0
#q1->ultima cifra citita e 1 (starea finala)
states = ["q0", "q1"]

# alfabet
alphabet = ["0", "1"]

# tranzitii
transitions = {
    ("q0", "0"): "q0",
    ("q0", "1"): "q1",
    ("q1", "0"): "q0",
    ("q1", "1"): "q1"
}

# stare initiala
start_state = "q0"

# stari finale
final_states = ["q1"]


def dfa(word):
    current_state = start_state

    for char in word:

        # verificam daca simbolul exista in alfabet
        if char not in alphabet:
            return False

        # schimbam starea
        current_state = transitions[(current_state, char)]

    # verificam daca starea finala e acceptata
    if current_state in final_states:
        return True
    else:
        return False


# teste
words = ["101", "100", "111", "000"]

for word in words:
    if dfa(word):
        print(word, "-> ACCEPTAT")
    else:
        print(word, "-> RESPINS")