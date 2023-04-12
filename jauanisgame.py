import tkinter as tk
import random



root = tk.Tk()
root.title("Nims")
serkocini = 12
serkocinu_daudz = tk.Label(root, text="Sērkociņu daudzums: " + str(serkocini))
serkocinu_daudz.pack()

gajiens = tk.Label(root, text="Spēlētāja gājiens")
gajiens.pack()

def player_turn():
    global serkocini
    global gajiens
    
    try:
        atnemsana = int(ievade.get())
        if atnemsana < 1 or atnemsana > 3 or atnemsana > serkocini:
            raise ValueError(text ="kļūda")
    except ValueError:
        ievade.delete(0, tk.END)
        return
    
    serkocini -= atnemsana
    
    serkocinu_daudz.config(text="Sērkociņu daudzums: " + str(serkocini))
    
    if serkocini == 0:
        gajiens.config(text="Tu uzvarēji")
        rest_poga.config(state='normal')
        return
    
    gajiens.config(text="Datora gājiens")
    
    computer_remove = None
    best_value = float("-inf")
    for i in range(1, min(serkocini, 3) + 1):
        value = minimax(serkocini - i, False)
        if value > best_value:
            computer_remove = i
            best_value = value
    
    serkocini -= computer_remove
    
    serkocinu_daudz.config(text="Sērkociņu daudzums: " + str(serkocini))

    if serkocini == 0:
        gajiens.config (text="Dators uzvarēja")
        ievade.config(state="disabled")
        rest_poga.config(state='normal')
        return
   
    gajiens.config(text="Tavs gājiens")

ievade = tk.Entry(root)
ievade.pack()

gajiena_poga = tk.Button(root, text="Veic gājienu", command=player_turn)
gajiena_poga.pack()
gajiena_poga.config(state='disabled')

def player_first():
    gajiens.config(text="Spēlētāja gājiens")
    ievade.config(state="normal")
    speletaja_poga.pack_forget()
    datora_poga.pack_forget()
    gajiena_poga.config(state='normal')

def computer_first():
    global serkocini
    gajiens.config(text="Datora gājiens")
    computer_remove = random.randint(1, min(serkocini, 3))
    serkocini -= computer_remove
    serkocinu_daudz.config(text="Sērkociņu daudzumus: " + str(serkocini))
    gajiens.config(text="Dators veic gājienu")
    ievade.config(state="normal")
    speletaja_poga.pack_forget()
    datora_poga.pack_forget()
    gajiena_poga.config(state='normal')
    
speletaja_poga = tk.Button(root, text="Spēlētājs", command=player_first)
speletaja_poga.pack()

datora_poga = tk.Button(root, text="Dators", command=computer_first)
datora_poga.pack()

def reset_game():
    global serkocini
    serkocini = 12
    serkocinu_daudz.config(text="Sērkociņu daudzumus: " + str(serkocini))
    gajiens.config(text="Veic gājienu")
    ievade.config(state="normal")
    speletaja_poga.pack()
    datora_poga.pack()

rest_poga = tk.Button(root, text="Restartēt", command=reset_game)
rest_poga.pack()
rest_poga.config(state='disabled')

def minimax(remaining, is_maximizing):
    if remaining == 0:
        return -1 if is_maximizing else 1
    
    best_value = float("-inf") if is_maximizing else float("inf")
    for i in range(1, min(remaining, 3) + 1):
        value = minimax(remaining - i, not is_maximizing)
        if is_maximizing:
            best_value = max(best_value, value)
        else:
            best_value = min(best_value, value)
    
    return best_value
    
root.mainloop()

