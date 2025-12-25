import tkinter as tk
import customtkinter as ctk
import tkinter.messagebox as tkmb
from functions import check_signin, signup_user, is_valid_characters, is_valid_characters_space, toggle_password
import os
from tkinter import ttk, filedialog, Button, Frame, Label 
import pandas as pd
import json
import matplotlib.pyplot as plt
from PIL import Image, ImageTk


class SignInFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.setup_signin_frame()

    def setup_signin_frame(self):
        #Create sign in frame
        self.sigin_frame = ctk.CTkFrame(master=self, width=400, height=470)
        self.sigin_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #Sign in text
        self.signin_text = ctk.CTkLabel(master=self.sigin_frame, text="Sign In", font=("Calibri", 30, "bold"))
        self.signin_text.place(x=50, y=45)

        self.error_label = ctk.CTkLabel(master=self.sigin_frame, text="", font=("Calibri", 16), text_color="red")
        self.error_label.place(x=50, y=80)

        #Entry for username and password
        self.signin_username = ctk.CTkEntry(master=self.sigin_frame, placeholder_text="Username", width=300)
        self.signin_username.place(x=50, y=110)

        self.show_password = ctk.BooleanVar()
        self.signin_password = ctk.CTkEntry(master=self.sigin_frame, placeholder_text="Password", width=300, show="*")
        self.signin_password.place(x=50, y=150)

        #Checkbox to show or hide password
        self.show_password = ctk.CTkCheckBox(master=self.sigin_frame, text="Show password", font=("Calibri", 12), command=lambda: toggle_password(self.signin_password, self.show_password), variable=self.show_password)
        self.show_password.place(x=50, y=185)

        #Sign In and Sign Up button
        self.signin_button = ctk.CTkButton(master=self.sigin_frame, text="Sign In", width=100, fg_color="#3498db", text_color="#ffffff", hover_color="#2980b9", command=self.check_signin)
        self.signin_button.place(x=145, y=230)

        self.no_account_label = ctk.CTkLabel(master=self.sigin_frame, text="No account?", font=("Calibri", 12, "underline"))
        self.no_account_label.place(x=163, y=315)

        self.signup_button = ctk.CTkButton(master=self.sigin_frame, text="Sign Up", width=100, fg_color="#3498db", text_color="#ffffff", hover_color="#2980b9", command=self.master.open_signup_frame)
        self.signup_button.place(x=145, y=350)

    def check_signin(self):
        username = self.signin_username.get()
        password = self.signin_password.get()

        if check_signin(username, password):
            self.master.open_home_frame_from_signin()
        else:
            self.error_label.configure(text="Invalid username or password. Please check again!")


class SignUpFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.setup_signup_frame()

    def setup_signup_frame(self):
        #Create sign up frame
        self.signup_frame = ctk.CTkFrame(master=self, width=400, height=470)
        self.signup_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #Sign up text
        self.signup_text = ctk.CTkLabel(master=self.signup_frame, text="Sign Up", font=("Calibri", 20, "bold"))
        self.signup_text.place(x=50, y=45)

        #Entry for username and password
        self.signup_username = ctk.CTkEntry(master=self.signup_frame, placeholder_text="Username", width=300)
        self.signup_username.place(x=50, y=110)
        self.signup_password = ctk.CTkEntry(master=self.signup_frame, placeholder_text="Password", width=300, show="*")
        self.signup_password.place(x=50, y=150)

        #Sign up button
        self.signup_button = ctk.CTkButton(master=self.signup_frame, text="Sign up", width=100, fg_color="#3498db", text_color="#ffffff", hover_color="#2980b9", command=self.new_user_signup)
        self.signup_button.place(x=145, y=230)

        self.back_button = ctk.CTkButton(master=self.signup_frame, text="Back to sign in", width=100, fg_color="#3498db", text_color="#ffffff", hover_color="#2980b9", command=self.master.open_signin_frame)
        self.back_button.place(x=145, y=300)
    
    def new_user_signup(self):
        username = self.signup_username.get()
        password = self.signup_password.get()

        if not username or not password:
            print("Please enter all required information to sign up!")
            tkmb.showwarning("Warning", "Username and password must be filled")
        if not is_valid_characters(username) or not is_valid_characters(password):
            print("Username and password must only contain standard letters and numbers!")
            tkmb.showwarning("Warning", "Invalid letters or numbers")
        if signup_user(username, password):
            print("Sign up succesfully!")
            tkmb.showinfo("Notification", "Sign up was successful!")
            # self.signup_frame.place_forget()
            # self.master.open_signin_frame()
            return
        else:
            print("Username and password have been signed up.")
            tkmb.showerror("Error", "Account already exists.")
            return

class DataFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.setup_data_frame()

    def toggle_menu(self):
        def collapse_toggle_menu():
            self.toggle_menu_frame.destroy()
            self.toggle_button.config(text="☰")
            self.toggle_button.config(command=self.toggle_menu)
        
        #Create toggle frame
        self.toggle_menu_frame = Frame(master=self, background="#353535", bd=100)
        window_height = 750
        self.toggle_menu_frame.place(x=0, y=50, height=window_height, width=200) 
        self.toggle_button.config(command=collapse_toggle_menu)

        #Create button in toggle frame
        self.export_data_button = Button(master=self.toggle_menu_frame, text="Data", font=('bold', 20), bd=0, foreground="white", background="#353535")
        self.export_data_button.place(x=-50, y=-70)

        self.export_chart_button = Button(master=self.toggle_menu_frame, text="Chart", font=("bold", 20), bd=0, foreground="white", background="#353535", command=self.master.open_chart_frame_from_data)
        self.export_chart_button.place(x=-55, y=-5)

        self.home_button = Button(master=self.toggle_menu_frame, text="Home", font=("bold", 20), bd=0, foreground="white", background="#353535", command=self.master.open_home_frame_from_data)
        self.home_button.place(x=-55, y=50)

    def setup_data_frame(self):
        self.master.change_geometry("800x800")
        self.master.change_title("Xport")
        
        #Creat Data frame
        self.data_frame = ctk.CTkFrame(master=self, width=900, height=500)
        self.data_frame.place(relx=0.5, rely=0.5, y=-10, anchor=tk.CENTER)

        #Create toggle button
        self.toggle_button = Button(master=self, text="☰", font=('bold', 20), bd=0, foreground="white", background="#292c2c", command=self.toggle_menu)
        self.toggle_button.place(x=0, y=0)

        #Create Export label
        self.export_label = Label(master=self, text="Export", font=('bold', 20), bd=0, foreground="white", background="#292c2c")
        self.export_label.place(x=50, y=10)

    
        #Create Data text
        self.data_text = ctk.CTkLabel(master=self.data_frame, text="Export Data", font=("Calibri", 40, "bold"))
        self.data_text.place(x=350, y=20)

        #Create a label
        self.label_file_explorer = ctk.CTkLabel(master=self.data_frame, text="Let's choose a file", font=("Calibri", 20))
        self.label_file_explorer.place(x=375, y=80)

        #Create browse button
        self.browse_file_button = ctk.CTkButton(master=self.data_frame, text="Browse file", command=self.open_file)
        self.browse_file_button.place(x=375, y=140)

    def open_file(self):
        filepath = filedialog.askopenfilename(initialdir="/", 
                                              title="Select a file", 
                                              filetypes=[("Excel files", "*.xlsx *.xls"), 
                                                     ("All files", "*.*")])
        file_name = os.path.basename(filepath)
        self.label_file_explorer.configure(text="File opened: " + file_name)
        self.label_file_explorer.place(x=345, y=80)

        self.filepath = filepath

        self.label_export = ctk.CTkLabel(master=self.data_frame, text="Which type of file do you want to export to?", font=("Calibri", 20))
        self.label_export.place(x=280, y=220)

        self.file_choice = ctk.CTkComboBox(master=self.data_frame, values=["txt", "csv", "json"])
        self.file_choice.place(x=375, y=260)

        self.export_button = ctk.CTkButton(master=self.data_frame, text="Export", command=self.export)
        self.export_button.place(x=375, y=300)
    
    def export(self):
        #Export data 
        if self.filepath:
            try:
                df = pd.read_excel(self.filepath)

                export_format = self.file_choice.get()
                
                export_path = os.path.normpath(os.path.join(os.path.dirname(self.filepath), os.path.splitext(os.path.basename(self.filepath))[0] + '.' + export_format))

                print(f"Exporting to: {export_path}")

                if export_format == 'json':
                    #df.to_json(export_path, orient='records', lines=True)
                    #Format the dataframe to handle scientific notation and special characters
                    df = df.map(lambda x: f'{x:.10g}' if isinstance(x, float) else x)
                    
                    json_format_data = df.to_json(orient='records', indent=4, force_ascii=False)
                    with open(export_path, 'w', encoding='utf-8') as f:
                        f.write(json_format_data) 
                
                elif export_format == 'csv':
                    #df.to_csv(export_path, index=False)
                    #Format the dataframe to handle scientific notation and special characters
                    df = df.map(lambda x: f'{x:.10g}' if isinstance(x, float) else x)
                    csv_format_data = df.to_csv(index=False)
                    with open(export_path, 'w',encoding='utf-8') as f:
                        f.write(csv_format_data)
                
                elif export_format == 'txt':
                    #df.to_csv(export_path, index=False, sep='\t\t', header=True)
                    #Format the dataframe to handle scientific notation and special characters
                    df = df.map(lambda x: f'{x:.10g}' if isinstance(x, float) else x)
                    txt_format_data = df.to_string(index=False)
                    with open(export_path, 'w', encoding='utf-8') as f:
                        f.write(txt_format_data)

                self.label_file_explorer.configure(text=f"File exported to: {export_path}")
                self.label_file_explorer.place(x=200, y=350)

            except Exception as e:
                self.label_file_explorer.configure(text=f"Error: {e}")
                self.label_file_explorer.place(x=110, y=350)
        else:
            self.label_file_explorer.configure(text="No file selected.")
            self.label_file_explorer.place(x=375, y=350)


class ChartFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.setup_chart_frame()

    def toggle_menu(self):
        def collapse_toggle_menu():
            self.toggle_menu_frame.destroy()
            self.toggle_button.config(text="☰")
            self.toggle_button.config(command=self.toggle_menu)
        
        #Create toggle frame
        self.toggle_menu_frame = Frame(master=self, background="#353535", bd=100)
        window_height = 750
        self.toggle_menu_frame.place(x=0, y=50, height=window_height, width=200) 
        self.toggle_button.config(command=collapse_toggle_menu)

        #Create button in toggle frame
        self.export_data_button = Button(master=self.toggle_menu_frame, text="Data", font=('bold', 20), bd=0, foreground="white", background="#353535", command=self.master.open_data_frame_from_chart)
        self.export_data_button.place(x=-50, y=-70)

        self.export_chart_button = Button(master=self.toggle_menu_frame, text="Chart", font=("bold", 20), bd=0, foreground="white", background="#353535")
        self.export_chart_button.place(x=-55, y=-5)

        self.home_button = Button(master=self.toggle_menu_frame, text="Home", font=("bold", 20), bd=0, foreground="white", background="#353535", command=self.master.open_home_frame_from_chart)
        self.home_button.place(x=-55, y=50)

    def setup_chart_frame(self):
        self.master.change_title("Xport")

        #Creat Chart frame
        self.chart_frame = ctk.CTkFrame(master=self, width=900, height=500)
        self.chart_frame.place(relx=0.5, rely=0.5, y=-10, anchor=tk.CENTER)

        #Create toggle button
        self.toggle_button = Button(master=self, text="☰", font=('bold', 20), bd=0, foreground="white", background="#292c2c", command=self.toggle_menu)
        self.toggle_button.place(x=0, y=0)

        #Create Export label
        self.export_label = Label(master=self, text="Export", font=('bold', 20), bd=0, foreground="white", background="#292c2c")
        self.export_label.place(x=50, y=10)
    
        #Create Chart text
        self.chart_text = ctk.CTkLabel(master=self.chart_frame, text="Export Chart", font=("Calibri", 40, "bold"))
        self.chart_text.place(x=340, y=20)

        #Create a label
        self.label_file_explorer = ctk.CTkLabel(master=self.chart_frame, text="Let's choose a file", font=("Calibri", 20))
        self.label_file_explorer.place(x=370, y=80)

        #Create browse file button
        self.browse_file_button = ctk.CTkButton(master=self.chart_frame, text="Browse file", command=self.open_file)
        self.browse_file_button.place(x=375, y=120)

        #Create label for column selection
        self.label_column = ctk.CTkLabel(master=self.chart_frame, text="Choose column to plot", font=("Calibri", 20))
        self.label_column.place(x=360, y=180)

        #Create combobox for column selection
        self.column_combobox = ctk.CTkComboBox(master=self.chart_frame, values=[], state="disabled")
        self.column_combobox.place(x=375, y=220)

        #Create label for chart type selection
        self.label_chart_export = ctk.CTkLabel(master=self.chart_frame, text="Choose type of chart", font=("Calibri", 20))
        self.label_chart_export.place(x=360, y=260)

        #Create combobox for chart type selection
        self.chart_combobox = ctk.CTkComboBox(master=self.chart_frame, values=["Line Chart", "Bar Chart", "Pie Chart"])
        self.chart_combobox.place(x=375, y=300)

        #Create a plot button
        self.plot_button = ctk.CTkButton(master=self.chart_frame, text="Plot Chart", command=self.plot_chart)
        self.plot_button.place(x=375, y=340)

        #Create export button
        self.export_button = ctk.CTkButton(master=self.chart_frame, text="Export Plotted Chart", command=self.export_chart)
        self.export_button.place(x=270, y=400)

        #Create view button
        self.view_button = ctk.CTkButton(master=self.chart_frame, text="View Chart", command=self.view_chart)
        self.view_button.place(x=490, y=400)

    def open_file(self):
        global df
        filepath = filedialog.askopenfilename(initialdir="/", 
                                              title="Select a file", 
                                              filetypes=[("Excel files", "*.xlsx *.xls")])
        file_name = os.path.basename(filepath)
        self.label_file_explorer.configure(text="File opened: " + file_name)
        self.label_file_explorer.place(x=345, y=80)

        if filepath:
            df = pd.read_excel(filepath)
            numeric_columns = df.select_dtypes(include='number').columns.tolist()
            if numeric_columns:
                self.column_combobox.configure(values=numeric_columns)
                self.chart_combobox.configure(state='readonly')
                self.column_combobox.configure(state='readonly')
                # self.column_combobox.configure(state='normal')
                tkmb.showinfo("File Selected", "Select the file succesfully!")
            else:
                tkmb.showerror("Error", "No numeric column in the selected file!")

    def plot_chart(self):
        chart_type = self.chart_combobox.get()
        selected_column = self.column_combobox.get()

        if not chart_type or not selected_column:
            tkmb.showerror("Error", "Please select a chart type and a column to plot!")
            return
        
        #Plot based on selected type and column
        plt.figure(figsize=(6, 4))
        if chart_type == "Line Chart":
            df[selected_column].plot()
        elif chart_type == "Bar Chart":
            df[selected_column].plot(kind='bar')
        elif chart_type == "Pie Chart":
            df[selected_column].value_counts().plot(kind='pie')
        else:
            tkmb.showerror("Error", "Invalid chart type!")
            return
        
        #Save the plot to an image file
        plt.savefig('chart.png')
        plt.close()

        # #Enable the View and Export buttons
        # self.view_button['state'] = 'normal'
        # self.export_button['state'] = 'normal'
    
    def view_chart(self):
        new_window = ctk.CTkToplevel(master=self.chart_frame)
        new_window.title("Plotted Chart")

        img = Image.open('chart.png')
        img = ImageTk.PhotoImage(img)
        panel = ctk.CTkLabel(new_window, image=img)
        panel.image = img 
        panel.pack()       

    def export_chart(self):
        export_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if export_path:
            Image.open('chart.png').save(export_path)
            tkmb.showinfo("Export Success", "The chart has been exported successfully!")

class HomeFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.setup_home_frame()
    
    def toggle_menu(self):
        def collapse_toggle_menu():
            self.toggle_menu_frame.destroy()
            self.toggle_button.config(text="☰")
            self.toggle_button.config(command=self.toggle_menu)
        
        #Create toggle frame
        self.toggle_menu_frame = Frame(master=self, background="#353535", bd=100)
        window_height = 750
        self.toggle_menu_frame.place(x=0, y=50, height=window_height, width=200) 
        self.toggle_button.config(command=collapse_toggle_menu)

        #Create button in toggle frame
        self.export_data_button = Button(master=self.toggle_menu_frame, text="Data", font=('bold', 20), bd=0, foreground="white", background="#353535", command=self.master.open_data_frame_from_home)
        self.export_data_button.place(x=-50, y=-70)

        self.export_chart_button = Button(master=self.toggle_menu_frame, text="Chart", font=("bold", 20), bd=0, foreground="white", background="#353535", command=self.master.open_chart_frame_from_home)
        self.export_chart_button.place(x=-55, y=-5)


    def setup_home_frame(self):
        self.master.change_title("Xport")

        #Create Home frame
        self.home_frame = ctk.CTkFrame(master=self, width=900, height=500)
        self.home_frame.place(relx=0.5, rely=0.5, y=-10, anchor=tk.CENTER)
        
        #Create Home text
        self.home_text = ctk.CTkLabel(master=self.home_frame, text="Xport - Easily exporting", font=('Calibri', 50, 'bold'))
        self.home_text.place(x=210, y=150)

        #Create Home label
        self.home_button = ctk.CTkLabel(master=self.home_frame, text="Search Xport tools in the left", font=('Calibri', 20), text_color="#0080FF")
        self.home_button.place(x=324, y=240)

        #Create toggle button
        self.toggle_button = Button(master=self, text="☰", font=('bold', 20), bd=0, foreground="white", background="#292c2c", command=self.toggle_menu)
        self.toggle_button.place(x=0, y=0)

        #Create export label
        self.export_label = Label(master=self, text="Export", font=('bold', 20), bd=0, foreground="white", background="#292c2c")
        self.export_label.place(x=50, y=10)