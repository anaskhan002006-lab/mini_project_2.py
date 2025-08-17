import tkinter as tk
import random

# --- Simple Tkinter Logo ---
def draw_logo():
    logo_win = tk.Toplevel()
    logo_win.title("Deadly News")
    canvas = tk.Canvas(logo_win, width=300, height=150, bg="black")
    canvas.pack()
    canvas.create_text(150, 75, text="☠️ DEADLY NEWS", font=("Arial", 24, "bold"), fill="red")
    logo_win.after(2500, logo_win.destroy)  # Auto-close after 2.5 seconds

# --- Data ---
subjects = [
    "Unknown Virus", "Mysterious Shadow", "Robot Army", "Zombie Dog", "Secret Agent",
    "Haunted Clown", "Radioactive Lizard"
]

actions = [
    "destroys", "haunts", "explodes", "attacks", "infects", "captures", "takes over"
]

places = [
    "a secret lab", "Delhi Metro", "Parliament building", "Mumbai beach",
    "moon base", "underground tunnel", "cyber café"
]

# --- Set to keep headlines unique ---
shown_headlines = set()

# --- Function to generate deadly headlines ---
def generate_headlines():
    headlines_box.delete(0, tk.END)  # clear old headlines
    count = 0
    while count < 5:
        subject = random.choice(subjects)
        action = random.choice(actions)
        place = random.choice(places)

        headline = f"🔥 DEADLY NEWS: {subject} {action} {place}!"
        if headline not in shown_headlines:
            shown_headlines.add(headline)
            headlines_box.insert(tk.END, headline)
            count += 1
    headlines_box.insert(tk.END, "\nStay Safe! Thanks for using the Deadly News Generator.")

# --- Main GUI ---
root = tk.Tk()
root.title("Deadly News Generator")
root.geometry("500x400")
root.config(bg="black")

# Show logo splash
root.after(200, draw_logo)

# Title Label
title = tk.Label(root, text="☠️ Deadly News Generator ☠️", font=("Arial", 18, "bold"), fg="red", bg="black")
title.pack(pady=10)

# Listbox to show headlines
headlines_box = tk.Listbox(root, width=70, height=10, font=("Arial", 12), fg="white", bg="gray20")
headlines_box.pack(pady=10)

# Generate Button
btn = tk.Button(root, text="Generate Deadly Headlines", font=("Arial", 14, "bold"),
                fg="white", bg="red", command=generate_headlines)
btn.pack(pady=10)

root.mainloop()
