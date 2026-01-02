import customtkinter as ctk
import json

def load_options():
    global nameuser

    with open("options.json","r") as f:
        options = json.load(f)

        nameuser = options[0]["name"]

load_options()

app = ctk.CTk()
app.geometry("500x500")
app.title("VisualV")

label_principal1 = ctk.CTkLabel(master=app,text=f"Welcome to Visual Version of the app, {nameuser}!",font=("Ubuntu",15))
label_principal1.pack()

app.mainloop()