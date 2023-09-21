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
     
    #above code is for the GUI using frontend
    #below code is for the backend
    def sendOTP(self):
        #this part from __init(self) function
        self.n = random.randint(1000,9999)
        self.client = Client("AC157a3deced6810930de61fcd331c090d", "22a173d4fad92dedf5ba699ca09fea7e")
        self.client.messages.create(to=["+91"+self.phone_numbe], from_="+15178360990", body=f'Your OTP is : {self.n}')
  
    def resendOTP(self):
        self.n = random.randint(1000,9999)
        self.client = Client("AC157a3deced6810930de61fcd331c090d", "22a173d4fad92dedf5ba699ca09fea7e")
        self.client.messages.create(to=["+91"+self.phone_numbe], from_="+15178360990", body=f'Your OTP is : {self.n}')
  
                 
    def checkOTP(self):
        try:
            self.userInput = int(self.User_Name.get(1.0, "end-1c"))
            if self.userInput == self.n:
                messagebox.showinfo("Success", "OTP Verified")
                self.n = "done"
                
            elif self.n == "done":
                messagebox.showinfo("showinfo", "OTP already used")
            else:
                messagebox.showinfo("showinfo", "Wrong OTP")
        except:
            messagebox.showinfo("showinfo", "Invalid OTP")
        
if __name__ == "__main__":
    window=Otp_verification()
    window.mainloop()
    
    #+15178360990     22a173d4fad92dedf5ba699ca09fea7e      AC157a3deced6810930de61fcd331c090d