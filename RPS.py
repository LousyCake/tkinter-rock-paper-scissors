import random
import tkinter as tk

player_wins = 0
player_losses = 0
ties = 0

window = tk.Tk()
window.title("RPS: The Challenge Begins")
window.geometry("400x350")

def play_game(player_choice):
    global player_wins, player_losses, ties
    
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = ''
    if player_choice == computer_choice:
        result = "It's a Tie!"
        ties += 1
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        player_wins += 1
    else:
        result = "You Lose!"
        player_losses += 1
    
    result_label.config(text=result)
    computer_choice_label.config(text=f"Computer Chose: {computer_choice}")
    score_label.config(text=f"Wins: {player_wins} | Losses: {player_losses} | Ties: {ties}")

def change_theme(theme):
    if theme == "Purple":
        window.config(bg="#E6E6FA")
        title_label.config(bg="#E6E6FA", fg="black")
        computer_choice_label.config(bg="#E6E6FA", fg="black")
        result_label.config(bg="#E6E6FA", fg="black")
        score_label.config(bg="#E6E6FA", fg="black")
        button_frame.config(bg="#E6E6FA")
    elif theme == "Dark":
        window.config(bg="#333333")
        title_label.config(bg="#333333", fg="white")
        computer_choice_label.config(bg="#333333", fg="white")
        result_label.config(bg="#333333", fg="white")
        score_label.config(bg="#333333", fg="white")
        button_frame.config(bg="#333333")
    elif theme == "Pastel Blue":
        window.config(bg="#ADD8E6")
        title_label.config(bg="#ADD8E6", fg="black")
        computer_choice_label.config(bg="#ADD8E6", fg="black")
        result_label.config(bg="#ADD8E6", fg="black")
        score_label.config(bg="#ADD8E6", fg="black")
        button_frame.config(bg="#ADD8E6")

title_label = tk.Label(window, text="RPS: The Challenge Begins", font=("Helvetica", 20))
title_label.pack(pady=10)

computer_choice_label = tk.Label(window, text="", font=("Helvetica", 14))
computer_choice_label.pack(pady=5)

result_label = tk.Label(window, text="", font=("Helvetica", 16))
result_label.pack(pady=10)

score_label = tk.Label(window, text="Wins: 0 | Losses: 0 | Ties: 0", font=("Helvetica", 14))
score_label.pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Crush", font=("Helvetica", 14), command=lambda: play_game("Rock"))
rock_button.grid(row=0, column=0, padx=10)
paper_button = tk.Button(button_frame, text="Envelop", font=("Helvetica", 14), command=lambda: play_game("Paper"))
paper_button.grid(row=0, column=1, padx=10)
scissors_button = tk.Button(button_frame, text="Slice", font=("Helvetica", 14), command=lambda: play_game("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

settings_menu = tk.Menu(window)
window.config(menu=settings_menu)

theme_menu = tk.Menu(settings_menu, tearoff=0)
settings_menu.add_cascade(label="Themes", menu=theme_menu)
theme_menu.add_command(label="Purple", command=lambda: change_theme("Purple"))
theme_menu.add_command(label="Dark", command=lambda: change_theme("Dark"))
theme_menu.add_command(label="Pastel Blue", command=lambda: change_theme("Pastel Blue"))

window.mainloop()