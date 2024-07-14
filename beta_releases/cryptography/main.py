from tkinter import messagebox, simpledialog
def userInput() :
    todo = simpledialog.askstring("Cryptography", "Do you want to encrypt or decrypt?")
    return todo
def message() :
    message = simpledialog.askstring("Message", "Input your message.")
    return message
def encrypt() :
    pass
def decrypt() :
    pass
while True :
    todo = userInput()
    if todo.upper() = "ENCRYPT" :
        encrypt()
    elif todo.upper() = "DECRYPT" :
        decrypt()
    else :
        break
