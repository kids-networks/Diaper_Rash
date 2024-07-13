from tkinter import Tk, messagebox, simpledialog
data = {}
def fileopen() :
    with open ("data.txt") as text :
        for line in text :
            line = line.rstrip ("\n")
            line = line.rstrip (" ")
            word, define = line.split("<<")
            data[word] = define
def fileedit(nWord, nDefine) :
    with open ("data.txt", "a") as text :
        text.write("\n" + str(nWord) + "<<" + str(nDefine))
fileopen()
while True :
    querySelector = simpledialog.askstring ("Swears Dictionary", "Type the swear word you want to search. Please use single form of the words.").capitalize()
    if querySelector in data :
        messagebox.showinfo("Search Results", querySelector + "\n" + data[querySelector])
    elif querySelector == None or querySelector == "" or querySelector == "!" :
        messagebox.showinfo("Invalid Word", "That is not a word.")
    else :
        newdata = simpledialog.askstring("Teach Us", "Sorry, we don't have info on what " + querySelector + " means. Please tell it to us.")
        newdata = newdata.capitalize()
        fileedit(querySelector, newdata)
        fileopen()
