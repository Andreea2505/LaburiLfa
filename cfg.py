#S → NP VP

#NP → John | Mary | The cat

#VP → runs | eats | sleeps
import random

# Context-Free Grammar
grammar = {
    "S": [["NP", "VP"]],

    "NP": [
        ["John"],
        ["Mary"],
        ["The", "cat"]
    ],

    "VP": [
        ["runs"],
        ["eats"],
        ["sleeps"]
    ]
}


def generate(symbol):
    """
    Recursively expands a non-terminal symbol
    until only terminal symbols remain.
    """

    # Terminal symbol
    if symbol not in grammar:
        return [symbol]

    # Randomly choose one production rule
    production = random.choice(grammar[symbol])

    result = []

    # Expand each symbol in the production
    for sym in production:
        result.extend(generate(sym))

    return result


# Generate 10 random sentences
print("=== CFG Sentence Generator ===")

for i in range(10):
    sentence = generate("S")
    print(" ".join(sentence))