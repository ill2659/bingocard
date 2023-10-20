import tkinter as tk
import random

def generate_bingo_card():
    # 数字初期化
    bingo_card = []

    # B列 (1-15)
    bingo_card.append(random.sample(range(1, 16), 5))

    # I列 (16-30)
    bingo_card.append(random.sample(range(16, 31), 5))

    # N列 (31-45)
    n_column = random.sample(range(31, 46), 5)
    n_column[2] = 'X'  # 真ん中のマスは"X"
    bingo_card.append(n_column)

    # G列 (46-60)
    bingo_card.append(random.sample(range(46, 61), 5))

    # O列 (61-75)
    bingo_card.append(random.sample(range(61, 76), 5))

    return bingo_card

def disable_cell(event):
    event.widget.config(state=tk.DISABLED)#非活性化のためのコード

def main():
    app = tk.Tk()
    app.title("Bingo Card")

    bingo_card = generate_bingo_card()

    for i in range(5):
        for j in range(5):
            cell_value = bingo_card[j][i]
            cell = tk.Button(app, text=str(cell_value), width=5, height=2, state=tk.NORMAL)
            cell.grid(row=i, column=j)
            cell.bind("<Button-1>", disable_cell)  # マウスクリックでセルを非活性化

    app.mainloop()

if __name__ == "__main__":
    main()
