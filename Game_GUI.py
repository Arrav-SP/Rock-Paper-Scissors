from tkinter import *
import random

humanPoints = 0
compPoints = 0


root = Tk()
root.title("Rock🪨,Paper📄,Scissors✂️")
root.configure(bg="black")  # Set window background to black

# Entry for showing moves/results
e = Entry(root, width=40, fg="yellow", bg="black", borderwidth=5, insertbackground="red")
e.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

# Entry for user to input points needed to win
win_entry = Entry(root, width=10, fg="yellow", bg="black", borderwidth=3, insertbackground="blue")
win_entry.grid(row=1, column=0, padx=10, pady=10)
win_entry.insert(0, "3")  # Default value

# Computer move label (moved to row 2)
comp_label = Label(root, text="Computer chose: ", font=("Helvetica", 12), bg="black", fg="white")
comp_label.grid(row=2, column=0, columnspan=3)

score_label = Label(root, text="Your points: 0 | Computer points: 0", font=("Helvetica", 12), bg="black", fg="white")
score_label.grid(row=3, column=0, columnspan=3)

result_label = Label(root, text="", font=("Helvetica", 12, "bold"), bg="black", fg="yellow")
result_label.grid(row=4, column=0, columnspan=3)

def start_game():
    global points_to_win, humanPoints, compPoints
    try:
        points_to_win = int(win_entry.get())
        humanPoints = 0
        compPoints = 0
        score_label.config(text="Your points: 0 | Computer points: 0")
        e.delete(0, END)
        e.insert(0, "Game started! First to " + str(points_to_win))
        # Enable buttons
        rock_button.config(state=NORMAL)
        paper_button.config(state=NORMAL)
        scissors_button.config(state=NORMAL)
        result_label.config(text="")
        comp_label.config(text="Computer chose: ")
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Please enter a valid number.")

def play(move):
    global humanPoints, compPoints, points_to_win
    e.delete(0, END)
    e.insert(0, move)
    
    compTurn = random.choice(['Rock', 'Paper', 'Scissors'])
    comp_label.config(text="Computer chose: " + compTurn) 

    # Determine winner
    if move == compTurn:
        result_label.config(text="It's a tie!")
    elif (move == 'Rock' and compTurn == 'Scissors') or \
         (move == 'Paper' and compTurn == 'Rock') or \
         (move == 'Scissors' and compTurn == 'Paper'):
        humanPoints += 1
        result_label.config(text="You win this round!")
    else:
        compPoints += 1
        result_label.config(text="Computer wins this round!")
    score_label.config(text="Your points: " + str(humanPoints) + " | Computer points: " + str(compPoints))

    # Check for game over
    if humanPoints == points_to_win or compPoints == points_to_win:
        if humanPoints > compPoints:
            result_label.config(text="Congratulations!!!\nYou Won!!!🥳")
        else:
            result_label.config(text="Better Luck Next Time 😊")
        # Disable buttons
        rock_button.config(state=DISABLED)
        paper_button.config(state=DISABLED)
        scissors_button.config(state=DISABLED)

def reset_game():
    global humanPoints, compPoints
    humanPoints = 0
    compPoints = 0
    e.delete(0, END)
    comp_label.config(text="Computer chose: ")
    score_label.config(text="Your points: 0 | Computer points: 0")
    result_label.config(text="")
    rock_button.config(state=DISABLED)
    paper_button.config(state=DISABLED)
    scissors_button.config(state=DISABLED)
    win_entry.delete(0, END)
    win_entry.insert(0, str(points_to_win))

button_style = {'bg': 'black', 'fg': 'white', 'activebackground': 'gray20', 'activeforeground': 'yellow'}

start_button = Button(root, text="Start Game", padx=20, pady=10, command=start_game, **button_style)
start_button.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

rock_button = Button(root, text="Rock", padx=40, pady=20, command=lambda: play("Rock"), state=DISABLED, **button_style)
paper_button = Button(root, text="Paper", padx=40, pady=20, command=lambda: play("Paper"), state=DISABLED, **button_style)
scissors_button = Button(root, text="Scissors", padx=40, pady=20, command=lambda: play("Scissors"), state=DISABLED, **button_style)
reset_button = Button(root, text="Reset Game", padx=20, pady=10, command=reset_game, **button_style)

rock_button.grid(row=5, column=0)
paper_button.grid(row=5, column=1)
scissors_button.grid(row=5, column=2)
reset_button.grid(row=6, column=0, columnspan=3, pady=10)

root.mainloop()
