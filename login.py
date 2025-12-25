import customtkinter as ctk
import tkinter.messagebox as tkmb
import tkinter as tk

#Setting GUI theme 
ctk.set_appearance_mode("dark")

#Setting color theme
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x500")
app.title("Sign in")


def signin():
    username = "admin"
    password = "123"
    new_window = ctk.CTkToplevel(app)

    new_window.title("Xport")
    new_window.geometry("350x150")

    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo(title="Notify", message="Login Succesfull")
        ctk.CTkLabel(new_window, text="Welcome to Xport!").pack()
    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showwarning(title="Warning", message="Invalid usernam. Please check again!")
    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showwarning(title="Warning", message="Invalid password. Please check again!")
    else:
        tkmb.showerror(title="Error", message="Invalid username and password. Please check again!")


app_name_label = ctk.CTkLabel(app, text="Xport", font=("Calibri", 14, "bold"))
app_name_label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Sign in", font=("Calibri", 14, "bold"))
label.pack(pady=12, padx=10)

user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
user_entry.pack(pady=20, padx=10)

user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password")
user_pass.pack(pady=20, padx=10)

signin_button = ctk.CTkButton(master=frame, text="Sign in", command=signin)
signin_button.pack(pady=12, padx=10)

label1 = ctk.CTkLabel(master=frame, text="Don't have an account", font=("Calibri", 12, "underline"))
label1.pack(padx=10)

signup_button = ctk.CTkButton(master=frame, text="Sign up")
signup_button.pack(pady=12, padx=10)


app.mainloop()