import tkinter as tk

class TTT(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Tic Tao Toe")
        self.btns = []
        self.turn = True # always starts with "X" = True
        self.count = 0
        self.game_over = False  # Add a flag to track if the game is over
        self.resizable(False, False)
        self.Start()
         
    def Start(self):
        for i in range(0, 3):
            row = []
            for j in range(0, 3):
                btn = tk.Button(
                    height=10, width=10, font=("oldtimesroman", 16),
                    bg="#33ffa8", fg="#000000",
                    command=lambda x=i, y=j: self.clicked(x, y)
                )
                row.append(btn)
                btn.grid(row=i, column=j)
            self.btns.append(row)    
        tk.Button(
            self, text="Restart", bg='blue', fg='white',
            activebackground='blue3', activeforeground='white',
            command=self.Restart
        ).grid(row=3, column=1)

    def clicked(self, x, y):
        if self.game_over:  # Prevent further moves after game ends
            return
        if self.btns[x][y]["state"] == tk.DISABLED:
            return
        char = "X"
        if self.turn:
            self.btns[x][y]["text"] = "X"
            char = "X"
        else:
            self.btns[x][y]["text"] = "O"
            char = "O"
        self.btns[x][y].config(state=tk.DISABLED)
        self.turn = not self.turn
        self.count += 1
        self.checkWinner(char)

    def checkWinner(self, char):
        # horizontal
        if (
            ((self.btns[0][0]["text"] == char) and (self.btns[0][1]["text"] == char) and (self.btns[0][2]["text"] == char)) or
            ((self.btns[1][0]["text"] == char) and (self.btns[1][1]["text"] == char) and (self.btns[1][2]["text"] == char)) or  
            ((self.btns[2][0]["text"] == char) and (self.btns[2][1]["text"] == char) and (self.btns[2][2]["text"] == char)) or  
            # vertical
            ((self.btns[0][0]["text"] == char) and (self.btns[1][0]["text"] == char) and (self.btns[2][0]["text"] == char)) or
            ((self.btns[0][1]["text"] == char) and (self.btns[1][1]["text"] == char) and (self.btns[2][1]["text"] == char)) or
            ((self.btns[0][2]["text"] == char) and (self.btns[1][2]["text"] == char) and (self.btns[2][2]["text"] == char)) or
            # diagonal
            ((self.btns[0][0]["text"] == char) and (self.btns[1][1]["text"] == char) and (self.btns[2][2]["text"] == char)) or
            ((self.btns[0][2]["text"] == char) and (self.btns[1][1]["text"] == char) and (self.btns[2][0]["text"] == char))
        ):
            self.Winner(char)
        elif self.count == 9:
            self.Winner("DRAW")

    def Winner(self, char):
        self.game_over = True  # Set flag so no more moves are possible
        # Disable all buttons so user can't play after game ends
        for row in self.btns:
            for btn in row:
                btn.config(state=tk.DISABLED)
        top = tk.Toplevel(self)
        top.title("Congratulations!")
        if char == "DRAW":
            topText = tk.Label(top, text=f"Its a DRAW !", font="Verdana 12 bold")
        else:
            topText = tk.Label(top, text=f"{char} is the WINNER !", font="Verdana 12 bold")
        topButton = tk.Button(top, text="Restart", bg='blue', fg='white', activebackground='blue3', activeforeground='white', command=self.Restart)
        topText.grid(row=0, column=0, padx=10, pady=10)
        topButton.grid(row=1, column=0)

    def Restart(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.btns = []
        self.turn = True
        self.count = 0
        self.game_over = False
        self.Start()

if __name__ == "__main__":
    T = TTT()
    T.mainloop()