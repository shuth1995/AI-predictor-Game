# AI Binary Sequence Predictor 🎯

This is a simple Python-based AI game where the computer attempts to **learn and predict binary sequences** (`0`s and `1`s) based on user-provided input. The program uses **probability models of binary triads** (sequences of 3 symbols) to predict the next symbol in a sequence and updates its predictions as it learns more from the user's input.

---

## 🚀 How It Works

1. **Training Phase**  
   The AI asks the user to input a binary string (`0`s and `1`s) until it collects at least 100 valid symbols.  
   This data is used to calculate the **probability** of a `'0'` or `'1'` following each triad (3-character sequence).

2. **Prediction Phase**  
   The user provides a new binary string.  
   The AI uses its learned probabilities to **predict the next symbol** after each triad and checks how many it got right.

3. **Learning Phase**  
   The AI uses the new data to update its probability model and become smarter with each round.

4. **Scoring**  
   The user starts with `$1000`.  
   - **Lose $1** if the AI predicts correctly.  
   - **Gain $1** if the AI is wrong.  
   The game continues until the user types `"enough"`.

---

## 🧠 Concepts Used

- Triad-based prediction model
- Probabilistic reasoning
- String filtering and processing
- Loop control and user interaction
- Dictionary-based frequency counting
- AI learning from user data

---

## 🏁 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/shuth1995/AI-predictor-Game.git
   cd AI-predictor-Game
   ```

2. Run the program
   ```bash
   python predictor.py
   ```

## 📁 File Structure
```text
AI-predictor-Game/
├── predictor.py      # Main game logic and prediction model
├── README.md         # Project documentation
├── requirements.txt  # Requirements
```

## ✍️ Example Session

```text
Please provide AI some data to learn...
The current data length is 0, 100 symbols left
Print a random string containing 0 or 1:

> 010100100101010101000010001010101010100100100101001
The current data length is 51, 49 symbols left
Print a random string containing 0 or 1:

> 011010001011111100101010100011001010101010010001001010010011

Final data string:
010100100101010101000010001010101010100100100101001011010001011111100101010100011001010101010010001001010010011

You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!

Print a random string containing 0 or 1:

> 0111001001
predictions:
0101011

Computer guessed 4 out of 7 symbols right.
Your balance is now $999

Print a random string containing 0 or 1:

> 0101001001
predictions:
1011011

Computer guessed 5 out of 7 symbols right.
Your balance is now $996

Print a random string containing 0 or 1:

> enough
Game over!
```
