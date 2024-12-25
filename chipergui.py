import tkinter as tk
from tkinter import ttk

def enkripsi(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

def dekripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plain_text += char
    return plain_text

def process_text():
    try:
        shift = int(shift_value.get())
        text = input_text.get("1.0", "end-1c")
        if mode.get() == "encrypt":
            result = enkripsi(text, shift)
        else:
            result = dekripsi(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
    except ValueError:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter a valid shift value.")

# GUI setup
root = tk.Tk()
root.title("Cipher Encryption Machine")
root.geometry("500x400")
root.config(bg="#1abc9c")  # Latar belakang hijau terang

# Styling
title_font = ("Arial", 16, "bold")
label_font = ("Arial", 12, "bold")
button_font = ("Arial", 12, "bold")

# Title Label
title_label = tk.Label(root, text="Cipher Machine", font=title_font, bg="#16a085", fg="white")
title_label.pack(pady=10, fill="x")

# Shift Value Frame
shift_frame = tk.Frame(root, bg="#1abc9c")
shift_frame.pack(pady=10)
tk.Label(shift_frame, text="Set Shift Value:", font=label_font, bg="#1abc9c", fg="white").grid(row=0, column=0, padx=10, pady=5)
shift_value = tk.Entry(shift_frame, width=5, font=label_font, bg="#ecf0f1", fg="#2c3e50")
shift_value.grid(row=0, column=1, padx=5, pady=5)

# Input Text Frame
input_frame = tk.Frame(root, bg="#1abc9c")
input_frame.pack(pady=10)
tk.Label(input_frame, text="Input Text to Encrypt/Decrypt:", font=label_font, bg="#1abc9c", fg="white").grid(row=0, column=0, padx=10, pady=5)
input_text = tk.Text(input_frame, height=5, width=40, font=("Arial", 10), bg="#fdfefe", fg="#2c3e50")
input_text.grid(row=1, column=0, padx=10, pady=5)

# Mode selection
mode_frame = tk.Frame(root, bg="#1abc9c")
mode_frame.pack(pady=10)
mode = tk.StringVar(value="encrypt")
ttk.Style().configure("TRadiobutton", background="#1abc9c", foreground="white", font=label_font)
ttk.Radiobutton(mode_frame, text="Encrypt", variable=mode, value="encrypt", style="TRadiobutton").grid(row=0, column=0, padx=20)
ttk.Radiobutton(mode_frame, text="Decrypt", variable=mode, value="decrypt", style="TRadiobutton").grid(row=0, column=1, padx=20)

# Process Button
process_button = tk.Button(root, text="Process Text", command=process_text, font=button_font, bg="#e67e22", fg="white", activebackground="#f39c12", activeforeground="white", relief="raised")
process_button.pack(pady=10)

# Output Text Frame
output_frame = tk.Frame(root, bg="#1abc9c")
output_frame.pack(pady=10)
tk.Label(output_frame, text="Output:", font=label_font, bg="#1abc9c", fg="white").grid(row=0, column=0, padx=10, pady=5)
output_text = tk.Text(output_frame, height=5, width=40, font=("Arial", 10), bg="#fdfefe", fg="#2c3e50")
output_text.grid(row=1, column=0, padx=10, pady=5)

root.mainloop()
