import subprocess
import threading
import tkinter
import customtkinter  # <- import the CustomTkinter module
from tkinter import filedialog
from PIL import Image, ImageTk  # <- import PIL for the images
import os

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

#Replace <command=example> with <command=threading.Thread(target=example).start>

root_tk = customtkinter.CTk()  # create CTk window like you do with the Tk window (you can also use normal tkinter.Tk window)
root_tk.geometry("1250x700")
root_tk.title("Realtime Meeting Summarizer")


def button_function():
    p2=subprocess.Popen(["python","Rec.py"],shell=True)
    p2.wait()

def sumbutton():
    p3 = subprocess.Popen(["python", "sumpart.py"], shell=True)
    p3.wait()




y_padding = 13

frame_1 = customtkinter.CTkFrame(master=root_tk, corner_radius=15)
frame_1.pack(pady=20, padx=30, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1,text="Realtime Meeting Summarizer",width=220,height=55,text_font=("Times New Roman",28))
label_1.pack(pady=y_padding, padx=30)

#Right part
radiobutton_var = tkinter.IntVar(value=1)

label_2 = customtkinter.CTkLabel(master=frame_1,text="Upload File",width=220,height=55,text_font=("Times New Roman",20))
label_2.pack(pady=y_padding, padx=30)
label_2.place(relx=0.67,rely=0.20)

radiobutton_1 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=1,text="Text")
radiobutton_1.pack(pady=15, padx=15)
radiobutton_1.place(relx=0.725,rely=0.35)

radiobutton_2 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=2,text="Audio")
radiobutton_2.pack(pady=y_padding, padx=10)
radiobutton_2.place(relx=0.725,rely=0.4)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Filepath...")
entry_1.pack(pady=y_padding, padx=10)
entry_1.place(relx=0.675,rely=0.50)

button_2 = customtkinter.CTkButton(master=frame_1, corner_radius=8,text="Upload File", command=button_function)
button_2.pack(pady=y_padding, padx=30)
button_2.place(relx=0.79,rely=0.50)

#################

#Left part

label_3 = customtkinter.CTkLabel(master=frame_1,text="Start Meeting",width=220,height=55,text_font=("Times New Roman",20))
label_3.pack(pady=y_padding, padx=30)
label_3.place(relx=0.15,rely=0.20)

image_size=175
mic_image = ImageTk.PhotoImage(Image.open(r"guistuff/mic.png").resize((image_size, image_size)))

button_img = customtkinter.CTkButton(master=frame_1, corner_radius=8,image=mic_image,text="",fg_color="White", command=threading.Thread(target=button_function).start,width=250,height=250,text_font=("Sans",18))
button_img.pack(pady=300, padx=10)
button_img.place(relx=0.13,rely=0.30)

#############
button_1 = customtkinter.CTkButton(master=frame_1, corner_radius=8,text="Summarize", command=threading.Thread(target=sumbutton).start,width=150,height=45,text_font=("Sans",18))
button_1.pack(pady=300, padx=10)
button_1.place(relx=0.45,rely=0.8)

s_var = tkinter.StringVar(value="on")


root_tk.mainloop()