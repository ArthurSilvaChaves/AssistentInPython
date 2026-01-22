import customtkinter as ctk
import json
import pyautogui
import requests

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

def get_cotation_coins():
    coin = second_entry.get()
    value_coin = main_entry.get()

    if not coin and not value_coin:
        mainlabel1.configure(text="Please enter a value and a coin.")
        main_entry.configure(placeholder_text="value")
        second_entry.configure(placeholder_text="coin(USD, EUR, JPY, BTC)")
    else:
        if coin in coins:
            url_cotation = urls[0]
            url_bitcoin = urls[1]
            if coin == coins[0] or coin == coins[4] or coin == coins[4].lower():
                paramsdollar = {
                    "from":"USD",
                    "to":"BRL",
                    "amount":value_coin
                }

                response = requests.get(url_cotation, params=paramsdollar)
                data = response.json()

                mainlabel1.configure(text=f"{value_coin} USD = {data['rates']['BRL']} BRL")

            elif coin == coins[1] or coin == coins[5] or coin == coins[5].lower():
                paramseuro = {
                    "from":"EUR",
                    "to":"BRL",
                    "amount":value_coin
                }

                response = requests.get(url_cotation, params=paramseuro)
                data = response.json()

                mainlabel1.configure(text=f"{value_coin} EUR = {data['rates']['BRL']} BRL")
            
            elif coin == coins[2] or coin == coins[6] or coin == coins[6].lower():
                paramsyen = {
                    "from":"JPY",
                    "to":"BRL",
                    "amount":value_coin
                }

                response = requests.get(url_cotation, params=paramsyen)
                data = response.json()

                mainlabel1.configure(text=f"{value_coin} YEN = {data['rates']['BRL']} BRL")
            
            elif coin == coins[3] or coin == coins[7] or coin == coins[7].lower():
                paramsbitcoin = {
                    "ids":"bitcoin",
                    "vs_currencies":"brl"
                }

                res = requests.get(url_bitcoin, params=paramsbitcoin)
                databitcoin = res.json()

                btc_brl = databitcoin["bitcoin"]["brl"]

                mainlabel1.configure(text=f"1 BTC = {btc_brl} BRL")
            else:
                mainlabel1.configure(text="Please enter a valid coin.")

janela = ctk.CTk()
width_janela = janela.winfo_screenwidth()
height_janela = janela.winfo_screenheight()
janela.geometry(f"{width_janela}x{height_janela}+0+0")
janela.title("VisualV")

mainlabel1 = ctk.CTkLabel(janela, text=f"Welcome, {nameuser}!", font=("Arial", 20))
mainlabel1.pack(pady=10)

main_entry = ctk.CTkEntry(janela, placeholder_text="main Entry",font=("Arial", 20),width=400)
main_entry.pack(pady=10)

second_entry = ctk.CTkEntry(janela, placeholder_text="second Entry",font=("Arial", 20),width=400)
second_entry.pack(pady=10)

functions = ctk.CTkScrollableFrame(janela, width=300, height=400)
functions.pack(pady=10)

mainlabel2 = ctk.CTkLabel(janela, text="Functions", font=("Arial", 20))
mainlabel2.pack(pady=10)

open_app_button = ctk.CTkButton(functions, text="Open App (by terminal)", command=open_app,font=("Arial", 20))
open_app_button.pack(pady=10)

get_cotation_coins_button = ctk.CTkButton(functions, text="Get Cotation Coins", command=get_cotation_coins,font=("Arial", 20))
get_cotation_coins_button.pack(pady=10)

janela.mainloop()