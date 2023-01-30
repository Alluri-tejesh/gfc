import tkinter as tk
import webbrowser
from flask import request
from google.oauth2.credentials import Credentials
from tkinter import messagebox
def authenticate():
    credentials = Credentials.from_authorized_user_info(info=request.environ)
    if credentials is None:
        webbrowser.open(credentials.authorization_url(), new=2)
    else:
        messagebox.showinfo("Authentication", "Successfully authenticated with Google.")
root = tk.Tk()
root.title("Google Authentication")
frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame, 
text="Authenticate with Google", 
command=authenticate)
button.pack()
root.mainloop()
