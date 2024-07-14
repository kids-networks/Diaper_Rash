from tkinter import messagebox, simpledialog
message = None
def strrev(message) :
    return message[::-1]
while True :
    message = simpledialog.askstring("Cryptography", "Enter your message to reverse it.")
    reverse = strrev(message)
    messagebox.showinfo("Cryptography", reverse)