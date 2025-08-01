import random

# AI Predictor Game
# This program learns from user-provided binary data to predict the next symbol in a sequence.
# It collects training data, calculates probabilities of binary triads, and then plays a game
# where it attempts to predict user input, updating its knowledge and tracking user's balance.

# Opening statement to commence the "game"
print(f"Please provide AI some data to learn...\nThe current data length is {0}, {100} symbols left")

""" Stage 1 """
# Data Collection and Cleaning:
# Prompt user to input a string containing only '0' and '1'.
# Filter out any invalid characters, ensuring only binary symbols remain.
def get_binary_string():
    user_string = input("Print a random string containing 0 or 1:\n\n")
    return ''.join(char for char in user_string if char in '01')

user_string_filtered = get_binary_string()

# Continue collecting input until we have at least 100 valid binary symbols
while len(user_string_filtered) < 100:
    print(f"The current data length is {len(user_string_filtered)}, {100 - len(user_string_filtered)} symbols left")
    # Get new input and concatenate it with existing filtered string
    user_string_filtered += get_binary_string()

# Print the final training data string
print(f"Final data string:\n{user_string_filtered}\n")

# Dictionary to store counts of next symbols following each triad (3-symbol sequence)
triad_counts = {}

# Extract triads and count the occurrence of '0' and '1' following each triad in the training data
for i in range(len(user_string_filtered) - 3):
    triad = user_string_filtered[i:i+3]
    next_char = user_string_filtered[i+3]

    # Initialize count dictionary for unseen triads
    if triad not in triad_counts:
        triad_counts[triad] = {'0': 0, '1': 0}

    # Increment count of the symbol that follows the triad
    triad_counts[triad][next_char] += 1


""" Stage 2 """
# Calculate the probability of '0' and '1' following each triad based on counts
triad_probs = {}

for triad, counts in triad_counts.items():
    c0 = counts.get('0', 0)
    c1 = counts.get('1', 0)
    total = c0 + c1

    if total == 0:
        # No data for this triad; assume equal probability
        p0 = p1 = 0.5
    else:
        # Compute probability of '0' and '1' given the triad
        p0 = c0 / total
        p1 = c1 / total

    triad_probs[triad] = {'0': p0, '1': p1}

print('You have $1000. Every time the system successfully predicts your next press, you lose $1.\n'
      'Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!')

""" Stage 3 """
balance = 1000

while True:
    # Prompt user for new input to predict
    user_string_two = input("Print a random string containing 0 or 1:\n\n")

    if user_string_two.lower() == "enough":
        print("Game over!")
        break

    # Filter input to keep only '0' and '1'
    user_string_two_filtered = ''.join(char for char in user_string_two if char in '01')

    # Ensure input length is sufficient for prediction (at least 4 symbols)
    while len(user_string_two_filtered) < 4:
        user_string_two = input("Print a random string containing 0 or 1:\n\n")
        if user_string_two.lower() == "enough":
            print("Game over!")
            exit()
        user_string_two_filtered = ''.join(char for char in user_string_two if char in '01')

    predictions = []
    correct = 0
    s = user_string_two_filtered

    # Predict next symbol for each triad in the input string
    for i in range(len(s) - 3):
        triad = s[i:i+3]
        actual_next = s[i+3]
        # Retrieve probabilities for this triad; default to 0.5 if unseen
        probs = triad_probs.get(triad, {'0': 0.5, '1': 0.5})
        p0 = probs['0']
        p1 = probs['1']

        # Predict the next symbol based on higher probability; random choice if equal
        if p1 > p0:
            predicted = '1'
        elif p0 > p1:
            predicted = '0'
        else:
            predicted = random.choice(['0', '1'])

        predictions.append(predicted)
        # Count correct predictions
        if predicted == actual_next:
            correct += 1

    predicted_string = ''.join(predictions)
    print(f"predictions:\n{predicted_string}\n")

    total_predictions = len(predictions)
    accuracy = correct / total_predictions if total_predictions else 0.0

    print(f"Computer guessed {correct} out of {total_predictions} symbols right ({accuracy:.2%})")

    # Update triad_counts with new user input to learn and improve future predictions
    for i in range(len(s) - 3):
        triad = s[i:i+3]
        next_char = s[i+3]

        if triad not in triad_counts:
            triad_counts[triad] = {'0': 0, '1': 0}
        triad_counts[triad][next_char] += 1

    # Recalculate triad probabilities based on updated counts
    triad_probs = {}
    for triad, counts in triad_counts.items():
        c0 = counts.get('0', 0)
        c1 = counts.get('1', 0)
        total = c0 + c1

        if total == 0:
            p0 = p1 = 0.5
        else:
            p0 = c0 / total
            p1 = c1 / total

        triad_probs[triad] = {'0': p0, '1': p1}

    # Adjust user's balance: lose $1 for each correct prediction, gain $1 otherwise
    balance += (total_predictions - 2 * correct)
    print(f"Your balance is now ${balance}\n")
