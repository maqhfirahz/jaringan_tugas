from tkinter import Tk, Label, Entry, Button, Text, END, messagebox
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt_text():
    plain_text = text_input.get("1.0", END).strip()
    key = key_entry.get()
    
    if len(key) != 8:
        messagebox.showerror("Error", "Kunci harus tepat 8 karakter!")
        return
    
    if not plain_text:
        messagebox.showerror("Error", "Teks tidak boleh kosong!")
        return
    
    try:
        des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
        padded_text = pad(plain_text.encode('utf-8'), DES.block_size)
        encrypted_text = base64.b64encode(des.encrypt(padded_text)).decode('utf-8')
        result_output.delete("1.0", END)
        result_output.insert("1.0", encrypted_text)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

def decrypt_text():
    encrypted_text = text_input.get("1.0", END).strip()
    key = key_entry.get()
    
    if len(key) != 8:
        messagebox.showerror("Error", "Kunci harus tepat 8 karakter!")
        return
    
    if not encrypted_text:
        messagebox.showerror("Error", "Teks tidak boleh kosong!")
        return
    
    try:
        des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
        decoded_text = base64.b64decode(encrypted_text)
        decrypted_text = unpad(des.decrypt(decoded_text), DES.block_size).decode('utf-8')
        result_output.delete("1.0", END)
        result_output.insert("1.0", decrypted_text)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")


app = Tk()
app.title("DES Encryption & Decryption")
app.geometry("800x600")  
app.resizable(False, False)
app.configure(bg="#FFF5E1")  # Background cream

Label(app, text="Kunci (8 Karakter):", font=("Arial", 14), fg="black", bg="#F4E1D2").pack(pady=10)  # Creamy Pink
key_entry = Entry(app, font=("Arial", 14), width=30)
key_entry.pack(pady=5)

Label(app, text="Masukkan Teks:", font=("Arial", 14), fg="black", bg="#F4E1D2").pack(pady=10)  # Creamy Pink
text_input = Text(app, font=("Arial", 14), height=8, width=60, wrap="word", bg="#F9F3E0", fg="black")  # Light Cream
text_input.pack(pady=5)

Button(app, text="Enkripsi", font=("Arial", 14), bg="#D4E157", fg="white", command=encrypt_text).pack(pady=10)  # Light Green
Button(app, text="Dekripsi", font=("Arial", 14), bg="#FF7043", fg="white", command=decrypt_text).pack(pady=10)  # Light Coral

Label(app, text="Hasil:", font=("Arial", 14), fg="black", bg="#F4E1D2").pack(pady=10)  # Creamy Pink
result_output = Text(app, font=("Arial", 14), height=8, width=60, wrap="word", bg="#F9F3E0", fg="black")  # Light Cream
result_output.pack(pady=5)

app.mainloop()
