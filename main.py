import tkinter as tk
import random
import string
window = tk.Tk()
window.title("Random Password Generator")
window.geometry('300x300')
label = tk.Label(window, text="", font=("Arial" , 24))
label.pack(pady=20)

def generate_password():
    pwd_words = ["fish" , "shark" , "dog" , "apple" , "star" , "elephant" , "carrot" , "supercalifragilisticexpialidocious"]
    basePWD = random.choice(pwd_words)
    symbols = ''.join(random.choice(string.ascii_letters) for i in range(5))
    text = f"{basePWD} {symbols}"
    label.config(text=text)
button = tk.Button(window, text="Generate", command=generate_password)
button.pack()
window.mainloop()
