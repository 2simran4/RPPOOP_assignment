import tkinter as tk

def file_menu():
    print("File menu selected")

def edit_menu():
    print("Edit menu selected")

root = tk.Tk()

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=file_menu)
file_menu.add_command(label="Open", command=file_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=edit_menu)
edit_menu.add_command(label="Copy", command=edit_menu)
edit_menu.add_command(label="Paste", command=edit_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=menu_bar)
root.mainloop()
