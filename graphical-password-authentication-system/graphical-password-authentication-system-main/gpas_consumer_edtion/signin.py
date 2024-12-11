from customtkinter import *
import requests
from CTkMessagebox import CTkMessagebox
from tkinter import *
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")

def signin_handler(email,password_entry):
    # global email_value
    email_value = email.get()
    password_value = password_entry.get()
    print(email_value)
   
    input_data = {
        "email": email_value,
        "password": password_value,
        "returnSecureToken": True
    }
    response = requests.post(f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_API_KEY}",json=input_data)

    response_data = response.json()

    if response.status_code==200:
        token = response_data["idToken"]
        CTkMessagebox(icon="check", message="Sign in successful")
        print("Sign in successfull")
        
        # bkndrandom_choices()
    else:
        error_message = response_data["error"]["message"]
        print(response_data["error"]["message"])
        CTkMessagebox(icon="cancel", message=error_message)