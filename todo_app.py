import customtkinter
from tkinter import *
from tkinter import messagebox

# Function to add a task to the list


def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showerror("Warning", "Please enter a task.")

# Function to remove a selected task


def remove_task():
    selected = task_list.curselection()
    if selected:
        task_list.delete(selected[0])
    else:
        messagebox.showerror("Warning", "Please select a task to remove.")


# Creating main window
todo = customtkinter.CTk()
todo.title("To-Do List")
todo.geometry('450x560')
todo.config(bg='#1E1F21')
todo.resizable(False, False)

# setting app icon
icon_path = "image/todo.ico"
todo.iconbitmap(icon_path)

# labels
titel_label = customtkinter.CTkLabel(todo, font=(
    'Inter', 24, 'normal'), text="Today's", text_color='#FFFFFF', bg_color='#1E1F21')
titel_label.place(x=33, y=27)
titel_label = customtkinter.CTkLabel(todo, font=(
    'Inter', 40, 'bold'), text='Task', text_color='#FFFFFF', bg_color='#1E1F21')
titel_label.place(x=33, y=56)

# buttons
add_button = customtkinter.CTkButton(todo, command=add_task, font=('Inter', 20, 'bold'), text='Add', text_color='#FFFFFF',
                                     fg_color='#244554', hover_color='#0D7AFF', bg_color='#1E1F21', cursor='hand2', corner_radius=10, width=80, height=40)
add_button.place(x=340, y=396)

remove_button = customtkinter.CTkButton(todo, command=remove_task, font=('Inter', 20, 'bold'), text='Remove Task', text_color='#FFFFFF',
                                        fg_color='#244554', hover_color='#0D7AFF', bg_color='#1E1F21', cursor='hand2', corner_radius=10, width=390, height=40)
remove_button.place(x=30, y=455)

# entrybox
task_entry = customtkinter.CTkEntry(todo, font=(
    'Inter', 16, 'normal'), text_color='#000000', fg_color='#D9EBD7', border_color='#D9EBD7', width=293, height=40)
task_entry.place(x=30, y=396)

# listbox
Frame1 = customtkinter.CTkFrame(
    todo, width=390, height=236, fg_color='#FFFFFF', bg_color='#1E1F21')
Frame1.place(x=30, y=130)

task_list = Listbox(Frame1, font=('Inter', 16, 'normal'), width=31, height=9, bg='#1E1F21',
                    fg='#FFFFFF', highlightthickness=0, borderwidth=0, selectbackground='#244554', activestyle='none')
task_list.pack(side=LEFT, fill=BOTH)

# add scrollbar
scrollbar1 = Scrollbar(Frame1)
scrollbar1.pack(side=RIGHT, fill=BOTH)

task_list.config(yscrollcommand=scrollbar1.set)
scrollbar1.config(command=task_list.yview)

# Start the GUI app
todo.mainloop()
