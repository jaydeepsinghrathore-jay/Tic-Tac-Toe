# Championship Tic-Tac-Toe AI
### *Fundamentals of AI and ML (CSA2001) Project*

Welcome to **Championship Tic-Tac-Toe**! This project moves beyond a simple 3x3 grid to create a professional "Best of Five" tournament experience. Built with Python, it features a custom-coded AI that uses logic to challenge the player at multiple difficulty levels.

---

## Project Details
* **Author:** Jaydeep Singh Rathore
* **Reg No:** 25BCE11117
* **Subject:** Fundamentals of AI and ML (CSA2001)
* **Faculty:** Dr. Vinesh Kumar
* **Institution:** VIT Bhopal University

---

## Key Features

* **Championship Mode:** The game doesn't end in one round. It tracks scores across multiple games until a player reaches **3 wins** to become the ultimate champion.
* **Dynamic AI Difficulty:**
    * **Easy:** The AI picks moves randomly (great for a quick win).
    * **Medium:** A mix of smart moves and human-like mistakes.
    * **Hard:** Uses the **Minimax Algorithm** to play perfectly. On this mode, the AI cannot be defeated; it can only be drawn.
* **Modern UI/UX:** A sleek "Dark Mode" interface using a #1A1C20 color palette to reduce eye strain and look professional.
* **Interactive Canvas:** Instead of using basic buttons, symbols are drawn dynamically on a digital canvas for a smoother visual feel.
* **Human-Like Interaction:** Includes a 400ms "thinking delay" for the AI, making the gameplay feel natural rather than instantaneous.

---

## The "Brain" of the AI: Minimax Logic
The core intelligence of this project is the **Minimax Algorithm**, a recursive strategy used in game theory.

1.  **Look-Ahead:** When it is the AI's turn, it simulates every possible move left on the board.
2.  **Scoring:** It assigns a score to every outcome (+10 for an AI win, -10 for a human win).
3.  **Optimal Choice:** It chooses the path that maximizes its own score while assuming the human player will try to minimize it.
4.  **Efficiency:** I implemented **depth-weighted scoring**, meaning the AI prefers to win in 2 moves rather than 5 moves, making it a very aggressive opponent.

---

## Tech Stack
* **Language:** Python 3.x
* **GUI Library:** Tkinter (Standard Python Library)
* **Logic:** Recursive Backtracking (Minimax)
* **Math Utilities:** Standard Math & Random modules

---

## How to Run the Game

1.  **Install Python:** Ensure you have Python 3 installed on your computer.
2.  **Download Script:** Save the project code as `championship_ttt.py`.
3.  **Run via Terminal:**
    ```bash
    python championship_ttt.py
    ```
4.  **Play:** Choose your difficulty and try to beat the AI to reach 3 wins!

---

## Reflections & Learning
Through this project, I learned:
* How to translate human intuition into mathematical logic.
* How to manage "Game States" across multiple rounds (Tournament Logic).
* The importance of UI delays to make an AI feel more "human."
* The power of recursion in solving complex decision-making trees.

---
