# DFA Room Navigation Game

# States (rooms)
START_ROOM = "A"
FINAL_ROOM = "D"

# DFA transitions:
# (current_state, input_symbol) -> next_state
transitions = {
    "A": {
        "e": "B",
        "s": "C"
    },
    "B": {
        "w": "A",
        "s": "D"
    },
    "C": {
        "n": "A",
        "e": "D"
    },
    "D": {
        "n": "B",
        "w": "C"
    }
}

current_room = START_ROOM

print("=== DFA Adventure Game ===")
print("Reach room D to win!")
print("Commands: n, s, e, w")
print()

while True:
    print(f"You are in room {current_room}")

    # Check accepting state
    if current_room == FINAL_ROOM:
        print("Congratulations! You found the treasure room!")
        break

    move = input("Choose direction: ").lower()

    # Check if transition exists
    if move in transitions[current_room]:
        current_room = transitions[current_room][move]
    else:
        print("Invalid move! No door in that direction.")