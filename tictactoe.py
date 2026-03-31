import tkinter as tk
from tkinter import messagebox
import random
import math

class ChampionshipTicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe: First to 3 Wins")
        self.root.configure(bg="#1A1C20")
        
       
        self.size = 300
        self.cell = self.size // 3
        self.board = [" " for _ in range(9)]
        self.difficulty = tk.StringVar(value="Hard")
        self.game_active = True
        
        
        self.player_score = 0
        self.ai_score = 0
        self.target_wins = 3
        self.diff_buttons = {}
        self.setup_ui()
        self.update_button_colors()

    def setup_ui(self):
        
        self.header = tk.Label(self.root, text=f"FIRST TO {self.target_wins} WINS", 
                               font=("Arial", 14, "bold"), bg="#1A1C20", fg="#FFFFFF")
        self.header.pack(pady=(20, 5))

        
        self.score_frame = tk.Frame(self.root, bg="#1A1C20")
        self.score_frame.pack(pady=10)
        
        self.p_label = tk.Label(self.score_frame, text=f"YOU: {self.player_score}", 
                                font=("Arial", 12), bg="#1A1C20", fg="#8AB4F8")
        self.p_label.pack(side=tk.LEFT, padx=30)
        
        self.ai_label = tk.Label(self.score_frame, text=f"AI: {self.ai_score}", 
                                 font=("Arial", 12), bg="#1A1C20", fg="#F28B82")
        self.ai_label.pack(side=tk.LEFT, padx=30)

        
        self.diff_frame = tk.Frame(self.root, bg="#1A1C20")
        self.diff_frame.pack(pady=5)
        for level in ["Easy", "Medium", "Hard"]:
            rb = tk.Radiobutton(self.diff_frame, text=level, variable=self.difficulty, 
                                value=level, font=("Arial", 9, "bold"),
                                indicatoron=0, width=10, pady=5, cursor="hand2", 
                                borderwidth=0, command=self.update_button_colors)
            rb.pack(side=tk.LEFT, padx=3)
            self.diff_buttons[level] = rb

        
        self.canvas = tk.Canvas(self.root, width=self.size, height=self.size, 
                                bg="#1A1C20", highlightthickness=0)
        self.canvas.pack(pady=15)
        self.draw_grid()
        self.canvas.bind("<Button-1>", self.handle_click)

        
        self.status = tk.Label(self.root, text="Click to start", font=("Arial", 11), 
                               bg="#1A1C20", fg="#9AA0A6")
        self.status.pack(pady=5)

        self.action_btn = tk.Button(self.root, text="Next Round", font=("Arial", 10, "bold"),
                                    bg="#3C4043", fg="white", relief="flat", padx=20,
                                    command=self.next_round)
        self.action_btn.pack(pady=15)

    def update_button_colors(self):
        current = self.difficulty.get()
        for level, btn in self.diff_buttons.items():
            if level == current:
                btn.config(bg="#8AB4F8", fg="#1A1C20", selectcolor="#8AB4F8")
            else:
                btn.config(bg="#303134", fg="#9AA0A6", selectcolor="#303134")

    def draw_grid(self):
        line_color = "#3C4043"
        p = 20
        self.canvas.create_line(self.cell, p, self.cell, self.size-p, fill=line_color, width=2)
        self.canvas.create_line(self.cell*2, p, self.cell*2, self.size-p, fill=line_color, width=2)
        self.canvas.create_line(p, self.cell, self.size-p, self.cell, fill=line_color, width=2)
        self.canvas.create_line(p, self.cell*2, self.size-p, self.cell*2, fill=line_color, width=2)

    def handle_click(self, event):
        if not self.game_active: return
        col, row = event.x // self.cell, event.y // self.cell
        idx = row * 3 + col
        if 0 <= idx < 9 and self.board[idx] == " ":
            self.make_move(idx, "X")
            if " " in self.board and self.game_active:
                self.root.after(400, self.ai_move)

    def make_move(self, i, player):
        self.board[i] = player
        r, c = divmod(i, 3)
        cx, cy = c * self.cell + self.cell // 2, r * self.cell + self.cell // 2
        
        if player == "X":
            s = 25
            self.canvas.create_line(cx-s, cy-s, cx+s, cy+s, fill="#8AB4F8", width=4, capstyle="round")
            self.canvas.create_line(cx+s, cy-s, cx-s, cy+s, fill="#8AB4F8", width=4, capstyle="round")
        else:
            self.canvas.create_oval(cx-25, cy-25, cx+25, cy+25, outline="#F28B82", width=4)
        
        win = self.check_winner(self.board)
        if win:
            self.game_active = False
            self.process_win(win)
        elif " " not in self.board:
            self.game_active = False
            self.status.config(text="It's a Draw!", fg="#FFFFFF")

    def process_win(self, winner):
        if winner == "X":
            self.player_score += 1
            self.status.config(text="You won the round!", fg="#8AB4F8")
        else:
            self.ai_score += 1
            self.status.config(text="AI won the round!", fg="#F28B82")
        
        self.p_label.config(text=f"YOU: {self.player_score}")
        self.ai_label.config(text=f"AI: {self.ai_score}")

        if self.player_score >= self.target_wins:
            self.end_championship("🏆 YOU ARE THE CHAMPION!")
        elif self.ai_score >= self.target_wins:
            self.end_championship("🤖 AI WINS THE TOURNAMENT!")

    def end_championship(self, message):
        self.header.config(text=message, fg="#FFD700") 
        self.status.config(text="Championship Over")
        self.action_btn.config(text="Start New Tournament", bg="#4285F4")
        messagebox.showinfo("Tournament End", message)

    def ai_move(self):
        if not self.game_active: return
        move = self.get_best_move() if self.difficulty.get() == "Hard" else \
               random.choice([i for i, x in enumerate(self.board) if x == " "])
        if move is not None: self.make_move(move, "O")

    def get_best_move(self):
        best_val, best_move = -math.inf, None
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                score = self.minimax(self.board, 0, False)
                self.board[i] = " "
                if score > best_val: best_val, best_move = score, i
        return best_move

    def minimax(self, board, depth, is_max):
        win = self.check_winner(board)
        if win == "O": return 10 - depth
        if win == "X": return depth - 10
        if " " not in board: return 0
        
        scores = []
        for i in range(9):
            if board[i] == " ":
                board[i] = "O" if is_max else "X"
                scores.append(self.minimax(board, depth + 1, not is_max))
                board[i] = " "
        return max(scores) if is_max else min(scores)

    def check_winner(self, b):
        lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for s in lines:
            if b[s[0]] == b[s[1]] == b[s[2]] != " ": return b[s[0]]
        return None

    def next_round(self):
        if self.player_score >= self.target_wins or self.ai_score >= self.target_wins:
            
            self.player_score = self.ai_score = 0
            self.p_label.config(text="YOU: 0")
            self.ai_label.config(text="AI: 0")
            self.header.config(text=f"FIRST TO {self.target_wins} WINS", fg="#FFFFFF")
            self.action_btn.config(text="Next Round", bg="#3C4043")
        
        self.board = [" " for _ in range(9)]
        self.game_active = True
        self.canvas.delete("all")
        self.draw_grid()
        self.status.config(text="Your turn", fg="#9AA0A6")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x680")
    ChampionshipTicTacToe(root)
    root.mainloop()
