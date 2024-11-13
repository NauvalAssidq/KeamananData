import tkinter as tk
from tkinter import messagebox
from utils import caesar_encrypt, caesar_decrypt

def process_text():
    text = text_entry.get()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return

    if mode.get() == "Encrypt":
        result = caesar_encrypt(text, shift)
    else:
        result = caesar_decrypt(text, shift)

    result_label.config(text=f"Result: {result}")

window = tk.Tk()
window.title("Caesar Cipher - Dark Mode")
window.geometry("500x350")
window.configure(bg="#1E1E1E")

title_label = tk.Label(window, text="Caesar Cipher", font=("Helvetica", 16, "bold"), bg="#1E1E1E", fg="#F5F5F5")
title_label.pack(pady=15)

tk.Label(window, text="Enter Text:", font=("Helvetica", 10), bg="#1E1E1E", fg="#F5F5F5").pack(pady=5)
text_entry = tk.Entry(window, width=50, font=("Helvetica", 10), bg="#2A2A2A", fg="#E0E0E0", insertbackground="#E0E0E0", relief="flat")
text_entry.pack(pady=5)

tk.Label(window, text="Shift Value:", font=("Helvetica", 10), bg="#1E1E1E", fg="#F5F5F5").pack(pady=5)
shift_entry = tk.Entry(window, width=10, font=("Helvetica", 10), bg="#2A2A2A", fg="#E0E0E0", insertbackground="#E0E0E0", relief="flat")
shift_entry.pack(pady=5)

mode = tk.StringVar(value="Encrypt")
frame = tk.Frame(window, bg="#1E1E1E")
frame.pack(pady=10)

encrypt_button = tk.Radiobutton(frame, text="Encrypt", variable=mode, value="Encrypt", bg="#1E1E1E", fg="#F5F5F5", selectcolor="#333333", activebackground="#333333", activeforeground="#FFFFFF", font=("Helvetica", 10))
decrypt_button = tk.Radiobutton(frame, text="Decrypt", variable=mode, value="Decrypt", bg="#1E1E1E", fg="#F5F5F5", selectcolor="#333333", activebackground="#333333", activeforeground="#FFFFFF", font=("Helvetica", 10))
encrypt_button.pack(side="left", padx=15)
decrypt_button.pack(side="left", padx=15)

process_button = tk.Button(window, text="Process", command=process_text, font=("Helvetica", 10, "bold"), bg="#007ACC", fg="#FFFFFF", activebackground="#005A99", activeforeground="#FFFFFF", relief="flat", padx=10, pady=5)
process_button.pack(pady=15)

result_label = tk.Label(window, text="Result: ", font=("Helvetica", 12), bg="#1E1E1E", fg="#F5F5F5")
result_label.pack(pady=10)

window.mainloop()
