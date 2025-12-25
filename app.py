import tkinter as tk
import customtkinter as ctk
from frames import DataFrame, SignUpFrame,  SignInFrame, HomeFrame, ChartFrame

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("700x500")
        self.title("Sign In")
        app_name = ctk.CTkLabel(self, text="Welcome to Xport!", font=("Calibri", 50, "bold"))
        app_name.pack(pady=25)

        self.signin_frame = None
        self.signup_frame = None
        self.data_frame = None
        self.chart_frame = None
        self.home_frame = None

        #Create the Sign In frame
        self.signin_frame = SignInFrame(self)
        self.signin_frame.pack(expand=True, fill="both")
        self.frames = {}

    def change_geometry(self, new_geometry):
        #Change the window geometry
        self.geometry(new_geometry)
    def change_title(self, new_title):
        #Change the window title
        self.title(new_title)
    
    def open_data_frame_from_home(self):
        #Shut the Home frame and open the Data frame
        self.home_frame.destroy()
        
        #Start Data frame
        self.data_frame = DataFrame(self)
        self.frames["data_frame"] = self.data_frame
        self.data_frame.pack(expand=True, fill="both")

    def open_data_frame_from_chart(self):
        #Shut the Chart frame and open the Data frame
        self.chart_frame.destroy()

        #Start Chart frame
        self.data_frame = DataFrame(self)
        self.frames["data_frame"] = self.data_frame
        self.data_frame.pack(expand=True, fill="both")

    def open_chart_frame_from_home(self):
        #Shut the Home frame and open the Chart frame
        self.home_frame.destroy()

        #Start Chart frame
        self.chart_frame = ChartFrame(self)
        self.frames["chart_frame"] = self.chart_frame
        self.chart_frame.pack(expand=True, fill="both")

    def open_chart_frame_from_data(self):
        #Shut the Data frame and open the Chart frame
        self.data_frame.destroy()

        #Start Chart frame
        self.chart_frame = ChartFrame(self)
        self.frames["chart_frame"] = self.chart_frame
        self.chart_frame.pack(expand=True, fill="both")

    def open_signin_frame(self):
        #Shut the Sign Up frame and open the SignIn frame
        self.signup_frame.destroy()

        #Back to SignIn frame
        self.signin_frame = SignInFrame(self)
        self.frames["signin_frame"] = self.signin_frame
        self.signin_frame.pack(expand=True, fill="both")
    
    def open_signup_frame(self):
        #Shut the Sign In frame and open the SignUp frame
        if hasattr(self, "signin_frame"):
            self.signin_frame.destroy()
        
        #Start signup frame
        self.signup_frame = SignUpFrame(self)
        self.change_title("Sign Up")
        self.frames["signup_frame"] = self.signup_frame
        self.signup_frame.pack(expand=True, fill="both")

    def open_home_frame_from_signin(self):
        #Shut the Sign In frame or Main frame and open the Home frame
        if hasattr(self, "signin_frame"):
            self.signin_frame.pack_forget()
            self.signin_frame.destroy()

        #Start Home frame
        self.home_frame = HomeFrame(self)
        self.frames["home_frame"] = self.home_frame
        self.home_frame.pack(expand=True, fill="both")

    def open_home_frame_from_data(self):
        if hasattr(self, "data_frame"):
            self.data_frame.pack_forget()
            self.data_frame.destroy()

        self.home_frame = HomeFrame(self)
        self.frames["home_frame"] = self.home_frame
        self.home_frame.pack(expand=True, fill="both")

    def open_home_frame_from_chart(self):
        if hasattr(self, "chart_frame"):
            self.chart_frame.pack_forget()
            self.chart_frame.destroy()

        self.home_frame = HomeFrame(self)
        self.frames["home_frame"] = self.home_frame
        self.home_frame.pack(expand=True, fill="both")
    
    # def open_main_frame(self):
    #     self.destroy_all_frames()
    #     self.change_title("Xport")
    #     self.main_frame = MainFrame(self)
    #     self.main_frame.pack(expand=True, fill="both")

    def destroy_all_frames(self):
        #Destroy all frames
        for frame_name, frame in self.frames.items():
            frame.destroy()
        self.frames = {}

    