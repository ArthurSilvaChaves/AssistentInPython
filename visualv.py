import customtkinter as ctk
import json
import pyautogui
import requests
from datetime import datetime
import webbrowser
import gameins
import speech_recognition as sr
import pyttsx3

def load_data():
    global audioptions_music
    global audio_music_special
    global audioptionsquit
    global audioptionstime
    global audioptionstraining
    global linkinpark
    global oldmusics
    global himymmusics
    global progmetal
    global baroesdapisadinha
    global movies
    global muscular_groups
    global youtube_channels
    global urls
    global coins
    global cities
    
    with open("data.json", "r") as f:
        data = json.load(f)
    
    audioptions_music = data["options"]["audioptions_music"]
    audio_music_special = data["options"]["audioptions_musics_special"]
    audioptionsquit = data["options"]["audioptionsquit"]
    audioptionstime = data["options"]["audioptionstime"]
    audioptionstraining = data["options"]["audioptionstraining"]
    linkinpark = data["data"]["linkinpark"]
    oldmusics = data["data"]["oldmusics"]
    himymmusics = data["data"]["himymmusics"]
    progmetal = data["data"]["progmetal"]
    baroesdapisadinha = data["data"]["baroesdapisadinha"]
    movies = data["data"]["movies"]
    muscular_groups = data["data"]["muscular_groups"]
    youtube_channels = data["data"]["youtube_channels"]
    urls = data["urls"]["url"]
    coins = data["coins"]["coin"]
    cities = data["locais"]

def load_options():
    global nameuser
    global round
    global language

    with open("options.json","r") as f:
        options = json.load(f)

        nameuser = options[0]["name"]
        round = options[1]["round"]
        language = options[2]["language"]

load_data()
load_options()

def open_app():
    app_selection = main_entry.get()

    if app_selection:
        pyautogui.hotkey("ctrl", "alt", "t")
        pyautogui.PAUSE = 0.7
        pyautogui.write(app_selection)
        pyautogui.PAUSE = 0.7
        pyautogui.press("enter")
    else:
        mainlabel1.configure(text="Please select an app to open.")

def microphone_function():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        mainlabel1.configure(text="Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="pt-br")
            mainlabel1.configure(text=f"You said: {text}")
            main_entry.configure(placeholder_text=text)
        except sr.UnknownValueError:
            mainlabel1.configure(text="Sorry, I could not understand your voice.")

def get_cotation_coins():
    coin = second_entry.get()
    coin_to = third_entry.get()
    value_coin = main_entry.get()

    if not coin and not value_coin and not third_entry.get():
        mainlabel1.configure(text="Please enter a value and a coin.")
    else:
        if coin in coins:
            url_cotation = urls[0]
            url_bitcoin = urls[1]
            
            #dollar to brl
            if (coin == coins[0] and coin_to == coins[8] ) or (coin == coins[4] and coin_to == coins[8]) or (coin == coins[4].lower() and coin_to == coins[8]):
                paramsdollar = {
                    "from":"USD",
                    "to":"BRL",
                    "amount":value_coin
                }
                response = requests.get(url_cotation, params=paramsdollar)
                data = response.json()

                mainlabel1.configure(text=f"{value_coin} USD = {data['rates']['BRL']} BRL")

                main_entry.delete(0,"end")
                second_entry.delete(0,"end")
                third_entry.delete(0,"end")
            
            #brl to dollar
            elif (coin == coins[8] and coin_to == coins[0]) or (coin == coins[8] and coin_to == coins[4]) or (coin == coins[8] and coin_to == coins[4].lower()):
                paramsreal = {
                    "from":"BRL",
                    "to":"USD",
                    "amount":value_coin
                }
                response = requests.get(url_cotation, params=paramsreal)
                data = response.json()

                mainlabel1.configure(text=f"{value_coin} BRL = {data['rates']['USD']} USD")

                main_entry.delete(0,"end")
                second_entry.delete(0,"end")
                third_entry.delete(0,"end")
           
            #euro to brl
            elif (coin == coins[1] and coin_to == coins[8]) or (coin == coins[5] and coin_to == coins[8]) or (coin == coins[5].lower() and coin_to == coins[8]):
                paramseuro = {
                    "from":"EUR",
                    "to":"BRL",
                    "amount":value_coin
                }
                response = requests.get(url_cotation, params=paramseuro)
                data = response.json()

                mainlabel1.configure(text=f"{value_coin} EUR = {data['rates']['BRL']} BRL")
            
                main_entry.delete(0,"end")
                second_entry.delete(0,"end")
                third_entry.delete(0,"end")

            #brl to euro
            elif (coin == coins[8] and coin_to == coins[1]) or (coin == coins[8] and coin_to == coins[5]) or (coin == coins[8] and coin_to == coins[5].lower()):
                paramsreal_to_euro = {
                    "from":"BRL",
                    "to":"EUR",
                    "amount":value_coin
                }
                response = requests.get(url_cotation, params=paramsreal_to_euro)
                data = response.json()

                mainlabel1.configure(text=f"{value_coin} BRL = {data['rates']['EUR']} EUR")

                main_entry.delete(0,"end")
                second_entry.delete(0,"end")
                third_entry.delete(0,"end")

            #yene to brl
            elif (coin == coins[2] and coin_to == coins[8]) or (coin == coins[6] and coin_to == coins[8]) or (coin == coins[6].lower() and coin_to == coins[8]):
                paramsyen = {
                    "from":"JPY",
                    "to":"BRL",
                    "amount":value_coin
                }
                response = requests.get(url_cotation, params=paramsyen)
                data = response.json()

                mainlabel1.configure(text=f"{value_coin} YEN = {data['rates']['BRL']} BRL")

                main_entry.delete(0,"end")
                second_entry.delete(0,"end")
                third_entry.delete(0,"end")

            #brl to yene
            elif (coin == coins[8] and coin_to == coins[2]) or (coin == coins[8] and coin_to == coins[6]) or (coin == coins[8] and coin_to == coins[6].lower()):
                paramsreal_to_yen = {
                    "from":"BRL",
                    "to":"JPY",
                    "amount":value_coin
                }
                response = requests.get(url_cotation, params=paramsreal_to_yen)
                data = response.json()

                mainlabel1.configure(text=f"{value_coin} BRL = {data['rates']['JPY']} YEN")

                main_entry.delete(0,"end")
                second_entry.delete(0,"end")
                third_entry.delete(0,"end")

            #btc to brl
            elif coin == coins[3] or coin == coins[7] or coin == coins[7].lower():
                paramsbitcoin = {
                    "ids":"bitcoin",
                    "vs_currencies":"brl"
                }
                res = requests.get(url_bitcoin, params=paramsbitcoin)
                databitcoin = res.json()

                btc_brl = databitcoin["bitcoin"]["brl"]

                mainlabel1.configure(text=f"1 BTC = {btc_brl} BRL")

                main_entry.delete(0,"end")
                second_entry.delete(0,"end")
                third_entry.delete(0,"end")

            #dollar to euro
            elif coin == coins[0].upper() and coin_to == coins[1]:
                paramsdollar_to_euro = {
                    "from":"USD",
                    "to":"EUR",
                    "amount":value_coin
                }

                response = requests.get(url_cotation,params=paramsdollar_to_euro)
                data = response.json()
                mainlabel1.configure(text=f"{value_coin} USD = {data['rates']['EUR']} EUR")

                main_entry.delete(0,"end")
                second_entry.delete(0,"end")
                third_entry.delete(0,"end")

            #euro to dollar
            elif coin == coins[1].upper() and coin_to == coins[0]:
                paramseuro_to_dollar = {
                    "from":"EUR",
                    "to":"USD",
                    "amount":value_coin
                }
                response = requests.get(url_cotation,params=paramseuro_to_dollar)
                data = response.json()

                mainlabel1.configure(text=f"{value_coin} EUR = {data['rates']['USD']} USD")

                main_entry.delete(0,"end")
                second_entry.delete(0,"end")
                third_entry.delete(0,"end")

            #dollar to yene
            elif coin == coins[0].upper() and coin_to == coins[2]:
                paramsdollar_to_yen = {
                    "from":"USD",
                    "to":"JPY",
                    "amount":value_coin
                }
                response = requests.get(url_cotation,params=paramsdollar_to_yen)
                data = response.json()
                mainlabel1.configure(text=f"{value_coin} USD = {data['rates']['JPY']} YEN")

                main_entry.delete(0,"end")
                second_entry.delete(0,"end")
                third_entry.delete(0,"end")

            #yene to dollar
            elif coin == coins[2].upper() and coin_to == coins[0]:
                paramsyen_to_dollar = {
                    "from":"JPY",
                    "to":"USD",
                    "amount":value_coin
                }
                response = requests.get(url_cotation,params=paramsyen_to_dollar)
                data = response.json()
                mainlabel1.configure(text=f"{value_coin} YEN = {data['rates']['USD']} USD")

                main_entry.delete(0,"end")
                second_entry.delete(0,"end")
                third_entry.delete(0,"end")

            #euro to yene
            elif coin == coins[1].upper() and coin_to == coins[2]:
                paramseuro_to_yen = {
                    "from":"EUR",
                    "to":"JPY",
                    "amount":value_coin    
            }
                response = requests.get(url_cotation,params=paramseuro_to_yen)
                data = response.json()
                mainlabel1.configure(text=f"{value_coin} EUR = {data['rates']['JPY']} YEN")

                main_entry.delete(0,"end")
                second_entry.delete(0,"end")
                third_entry.delete(0,"end")

            #yene to euro
            elif coin == coins[2].upper() and coin_to == coins[1]:
                paramsyen_to_euro = {
                    "from":"JPY",
                    "to":"EUR",
                    "amount":value_coin
                }

                response = requests.get(url_cotation,params=paramsyen_to_euro)
                data = response.json()
                mainlabel1.configure(text=f"{value_coin} YEN = {data['rates']['EUR']} EUR")

                main_entry.delete(0,"end")
                second_entry.delete(0,"end")
                third_entry.delete(0,"end")

            else:
                mainlabel1.configure(text="Please enter a valid coin.")
            

def convertion_tool():
    amount = main_entry.get()
    value1 = second_entry.get()
    value2 = third_entry.get()

    #bagunça total (arrumar dps)|(fix this later)
    if not amount or not value1 or not value2:
        mainlabel1.configure(text=" Please enter all the necessary values.")
    else:
        #temperature conversion conditions (if & else)
        if value1.lower() == "celsius" and value2.lower() == "fahrenheit":
            fahrenheit = (float(amount) * 1.8) + 32
            mainlabel1.configure(text=f"{amount} Celsius = {fahrenheit} Fahrenheit")
            
            main_entry.delete(0,"end")
            second_entry.delete(0,"end")
            third_entry.delete(0,"end")

        elif value1.lower() == "fahrenheit" and value2.lower() == "celsius":
            celsius = (float(amount) - 32) / 1.8
            mainlabel1.configure(text=f"{amount} Fahrenheit = {celsius:.2f} Celsius")
            
            main_entry.delete(0,"end")
            second_entry.delete(0,"end")
            third_entry.delete(0,"end")

        #distance conversion conditions (if & else)
        elif value1.lower() == "km" and value2.lower() == "miles":
            miles = float(amount) * 0.621371
            mainlabel1.configure(text=f"{amount} Kilometers = {miles:.2f} Miles")
            
            main_entry.delete(0,"end")
            second_entry.delete(0,"end")
            third_entry.delete(0,"end")

        elif value1.lower() == "miles" and value2.lower() == "km":
            kilometers = float(amount) / 0.621371
            mainlabel1.configure(text=f"{amount} Miles = {kilometers:.2f} Kilometers")
            
            main_entry.delete(0,"end")
            second_entry.delete(0,"end")
            third_entry.delete(0,"end")

        #weight conversion conditions (if & else)
        elif value1.lower() == "kg" and value2.lower() == "pounds":
            pounds = float(amount) * 2.20462
            mainlabel1.configure(text=f"{amount} Kilograms = {pounds:.2f} Pounds")
            
            main_entry.delete(0,"end")
            second_entry.delete(0,"end")
            third_entry.delete(0,"end")

        elif value1.lower() == "pounds" and value2.lower() == "kg":
            kilograms = float(amount) / 2.20462
            mainlabel1.configure(text=f"{amount} Pounds = {kilograms:.2f} Kilograms")
            
            main_entry.delete(0,"end")
            second_entry.delete(0,"end")
            third_entry.delete(0,"end")

        #if user no enter a valid value or measure
        else:
            mainlabel1.configure(text="Please enter valid measures.")
def atualizar_relogio():
    now = datetime.now().strftime("%H:%M")
    relogio.configure(text=now)
    relogio.after(1000, atualizar_relogio)

janela = ctk.CTk()
width_janela = janela.winfo_screenwidth()
height_janela = janela.winfo_screenheight()
janela.geometry(f"{width_janela}x{height_janela}+0+0")
janela.title("VisualV")

relogio = ctk.CTkLabel(janela, text="00:00", font=("Arial", 30))
relogio.pack(pady=5)

dia = ctk.CTkLabel(janela, text=f"{datetime.now().strftime('%d/%m/%Y')}", font=("Arial", 20))
dia.pack(pady=5)

dia_semana = ctk.CTkLabel(janela, text=f"{datetime.now().strftime('%A')}", font=("Arial", 20))
dia_semana.pack(pady=5)

mainlabel1 = ctk.CTkLabel(janela, text=f"Welcome, {nameuser}!", font=("Arial", 20))
mainlabel1.pack(pady=5)

main_entry = ctk.CTkEntry(janela, placeholder_text="Main Entry",font=("Arial", 20),width=400)
main_entry.pack(pady=10)

second_entry = ctk.CTkEntry(janela, placeholder_text="Second Entry",font=("Arial", 20),width=400)
second_entry.pack(pady=10)

tolabel = ctk.CTkLabel(janela, text="To", font=("Arial", 20))
tolabel.pack(pady=5)

third_entry = ctk.CTkEntry(janela, placeholder_text="Third Entry",font=("Arial", 20),width=400)
third_entry.pack(pady=10)

functions = ctk.CTkScrollableFrame(janela, width=300, height=200)
functions.pack(pady=10)

mainlabel2 = ctk.CTkLabel(janela, text="Functions", font=("Arial", 20))
mainlabel2.pack(pady=10)

open_app_button = ctk.CTkButton(functions, text="Open App (by terminal)", command=open_app,font=("Arial", 20))
open_app_button.pack(pady=10)

get_cotation_coins_button = ctk.CTkButton(functions, text="Get Cotation Coins", command=get_cotation_coins,font=("Arial", 20))
get_cotation_coins_button.pack(pady=10)

manual_to_user_button = ctk.CTkButton(functions, text="User Manual (Readme)", command=lambda: webbrowser.open("https://github.com/ArthurSilvaChaves/AssistentInPython?tab=readme-ov-file#manual-to-visual-version-of-this-app"),font=("Arial", 20))
manual_to_user_button.pack(pady=10)

convertion_tool_button = ctk.CTkButton(functions,text="Value conversion tool", command=convertion_tool,font=("Arial", 20))
convertion_tool_button.pack(pady=10)

weather_button = ctk.CTkButton(functions,text="See weather",command=lambda:print(1),font=("Arial",20))
weather_button.pack(pady=10)

microfone_button = ctk.CTkButton(functions, text="🎙️", command=microphone_function,font=("Arial", 40),width=60)
microfone_button.pack(pady=10)

atualizar_relogio()
janela.mainloop()