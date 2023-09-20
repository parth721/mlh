from twilio.rest import Client
from tkinter import *
from tkinter import messagebox
import random

class  Otp_verification(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.title("OTP Verification")
        self.resizable(False,False)
        
    def Labels(self):
        self.c = Canvas(self, bg="blue", height=250, width=300)
        self.c.place(x=100,y=50)
        
        self.login_Title = Label(self, text="OTP Verification", font=("Arial", 30, "bold"), fg="black")
        self.login_Title.place(x=200,y=100)
        
    def button(self):
        ...
        
    def checkOTP(self):
        ...
    
    def resendOTP(self):
        ...
        
if __name__ == "__main__":
    window=Otp_verification()
    window.mainloop()