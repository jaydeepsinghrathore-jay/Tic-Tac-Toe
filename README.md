# 🎮 Championship Tic-Tac-Toe

A sleek, dark-themed Tic-Tac-Toe game built with Python and Tkinter — featuring an unbeatable AI, three difficulty levels, and a **first-to-3-wins** championship format.

---

## ✨ Features

- **Championship Mode** — First player to win 3 rounds takes the tournament
- **Three Difficulty Levels**
  - `Easy` — AI plays randomly
  - `Medium` — AI plays randomly (same as Easy; extendable)
  - `Hard` — Unbeatable AI powered by the **Minimax algorithm**
- **Live Scoreboard** — Tracks your wins vs. AI wins across rounds
- **Clean Dark UI** — Google-inspired dark theme with smooth canvas rendering
- **Instant Replay** — Start a new tournament without restarting the app

---

## 🖼️ Preview

| Your turn | AI wins the round | Champion crowned |
|-----------|-------------------|-----------------|
| Blue `X` marks | Red `O` marks | Gold trophy header |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- `tkinter` (included in the standard library for most Python installs)

### Run the Game

```bash
git clone https://github.com/your-username/championship-tictactoe.git
cd championship-tictactoe
python tictactoe.py
```

> On some Linux systems, install Tkinter separately:
> ```bash
> sudo apt-get install python3-tk
> ```

---

## 🧠 How the AI Works

On **Hard** difficulty, the AI uses the **Minimax algorithm** — a recursive decision-tree search that evaluates every possible future game state and picks the optimal move. It is mathematically unbeatable; the best outcome against it is a draw.

```
AI win  → score: +10 (minus depth)
AI loss → score: -10 (plus depth)
Draw    → score: 0
```

---

## 🗂️ Project Structure

```
championship-tictactoe/
│
├── tictactoe.py   # All game logic and UI in a single file
└── README.md
```

---

## 🕹️ How to Play

1. Choose a difficulty — **Easy**, **Medium**, or **Hard**
2. Click any cell to place your `X`
3. The AI responds with `O`
4. Win 3 rounds before the AI does to become **Champion**
5. Click **Next Round** between games, or **Start New Tournament** after a championship ends

---
