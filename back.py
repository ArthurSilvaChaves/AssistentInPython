import pyautogui
from InquirerPy import inquirer
import requests
import os
import json
import time
import random
import webbrowser
import gameins
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 100)

urls = [
    #index = 0 api to get cotation real coins
    "https://api.frankfurter.app/latest",
    #index = 1 api to get cotatin bitcoin
    "https://api.coingecko.com/api/v3/simple/price",
    #index = 2 api to get weather
    "https://api.open-meteo.com/v1/forecast",
    #index = 3 api to get ip (lat e long)
    "http://ip-api.com/json/"
]

def load_options():
    global nameuser
    global rounder

    with open("options.json","r") as f:
        options = json.load(f)
 
        nameuser = options[0]["name"]
        rounder = options[1]["round"]

def datajson():
    global audioptions_music
    global audioptions_musics_special
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


    with open("data.json","r") as f:
        data = json.load(f)

    audioptions_music = data["options"]["audioptions_music"]
    audioptions_musics_special = data["options"]["audioptions_musics_special"]
    audioptionsquit = data["options"]["audioptionsquit"]
    audioptionstime = data["options"]["audioptionstime"]
    audioptionstraining = data["options"]["audioptionstraining"]
    linkinpark = data["options"]["linkinpark"]
    oldmusics = data["options"]["oldmusics"]
    himymmusics = data["options"]["himymmusics"]
    progmetal = data["options"]["progmetal"]
    baroesdapisadinha = data["options"]["baroesdapisadinha"]
    movies = data["options"]["movies"]
    muscular_groups = data["options"]["muscular_groups"]
    youtube_channels = data["options"]["youtube_channels"]


def menu():
    choices = inquirer.select(
        message = f"Hello {nameuser}, what do you want that Rogério Tomate do?",
        choices = [
            {"name":"1 - Open Navegator", "value":1},
            {"name":"2 - Get Cotation", "value":2},
            {"name":"3 - Convertion Tool", "value":3},
            {"name":"4 - Options", "value":4},
            {"name":"5 - Get Weather", "value":5},
            {"name":"6 - Hour in Real Time","value":6},
            {"name":"7 - See notices about technology","value":7},
            {"name":"8 - choose something random","value":8},
            {"name":"9 - Play a little game (Falling Blocks)","value":9},
            {"name":"10 - Heads or Tails","value":10},
            {"name":"11 - Use the audio recongizer(beta use)","value":11},
            {"name":"Close","value":12}
        ]
    ).execute()

    return choices

def hour_real_time():
    current_time = inquirer.select(
        message="Do you want to see the current time",
        choices=[
            {"name":"Yes","value":1},
            {"name":"No","value":2}
        ]
    ).execute()

    return current_time

def options_menu():
    options = inquirer.select(
        message= "Which option do you wannna change?",
        choices = [
            {"name":"Change my user name","value":1},
            {"name":"Enable/Disable rouding numbers", "value":2},
            {"name":"Back to main menu","value":3}
        ]
    ).execute()

    return options

def rounder_option():
    round_choice = inquirer.select(
        message="Do you want to enable rounding numbers?",
        choices=[
            {"name":"Yes","value":True},
            {"name":"No","value":False}
        ]
    ).execute()

    return round_choice

def open_navegator():
    navegator = inquirer.select(
        message="Which navegador do you want to open?",
        choices = [
             {"name":"Firefox","value":1},
             {"name":"Chrome","value":2},
             {"name":"Edge","value":3},
             {"name":"Back to main menu","value":4}
        ]
    ).execute()

    return navegator

def get_cotation():
    cotation = inquirer.select(
        message="Which cotation do you want to know?",
        choices = [
            {"name":"Dollar - (USD) to Brazilian Real - (BRL)","value":1},
            {"name":"Euro - (EUR) to Brazilian Real - (BRL)","value":2},
            {"name":"Japonese Yen - (JPY) to Brazilian Real (BRL)","value":3},
            {"name":"Brazilian Real - (BRL) to Dollar - (USD)","value":4},
            {"name":"Brazilian Real - (BRL) to Euro - (EUR)","value":5},
            {"name":"Brazilian Real - (BRL) to Japonese Yen - (JPY)","value":6},
            {"name":"Bitcoin - (BTC) to Brazilian Real - (BRL)","value":7},
            {"name":"Back to main menu","value":8}
        ]
    ).execute()

    return cotation

def temperature_converter():
    temperature_option = inquirer.select(
        message="Which temperature conversion do you want to do?",
        choices = [
            {"name":"Celsius to Fahrenheit","value":1},
            {"name":"Fahrenheit to Celsius","value":2},
            {"name":"Back to main menu","value":3}
        ]
    ).execute()

    return temperature_option

def distance_converter():
    distance_option = inquirer.select(
        message="Which distance conversion do you want to do?",
        choices = [
            {"name":"Kilometers to Miles","value":1},
            {"name":"Miles to Kilometers","value":2},
            {"name":"Back to main menu","value":3}
        ]
    ).execute()

    return distance_option

def weight_converter():
    weight_option = inquirer.select(
        message="Which weight conversion do you want to do?",
        choices = [
            {"name":"Kilograms to Pounds","value":1},
            {"name":"Pounds to Kilograms","value":2},
            {"name":"Back to main menu","value":3}
        ]
    ).execute()

    return weight_option

def convertion_tool():
    convertion = inquirer.select(
        message="Which convertion tool do you want to use?",
        choices = [
            {"name":"Temperature Converter Tool","value":1},
            {"name":"Distance Converter Tool","value":2},
            {"name":"Weight Converter Tool","value":3},
            {"name":"Back to main menu","value":4}
        ]
    ).execute()

    return convertion

def get_notices():
    notices = inquirer.select(
        message="Do you want to see the latest technology notices?",
        choices = [
            {"name":"Yes","value":1},
            {"name":"No","value":2}
        ]
    ).execute()

    return notices

def notices_shows(query=None):

    if query:
        url = f"https://hn.algolia.com/api/v1/search?query={query}&tags=story"
    else:
        url = "https://hn.algolia.com/api/v1/search?tags=story"

    res = requests.get(url)
    data = res.json()

    print("Notices about Technology of the Hacker News\n")

    for i,n in enumerate(data['hits'][:5],start=1):
        title = n['title'] or "No title"
        link = n['url'] or 'no link available'
        author = n['author']

        print(f'{i}. {title}\n   Author: {author}\n   Link: {link}')
    
def weather_tool():
    weather = inquirer.select(
        message="Which weather tool do you want to use?",
        choices = [
            {"name":"Get temperature","value":1},
            {"name":"Get Wind Speed","value":2},
            {"name":"Get Rain and Precipitation","value":3},
            {"name":"Back to main menu","value":4}
        ]
    ).execute()

    return weather

def random_choice():
    rand_choice = inquirer.select(
        message="Want do you choose randomly?",
        choices = [
            {"name":"Choose a music to listen","value":1},
            {"name":"Choose a movie or series to watch","value":2},
            {"name":"Choose a muscular group to train","value":3},
            {"name":"Choose a random youtube channel","value":4},
            {"name":"Back to main menu","value":5}
        ]
    ).execute()

    return rand_choice

def falling_blocks_game():
    game = inquirer.select(
        message="Do you want to play falling blocks?",
        choices = [
            {"name":"Yes","value":1},
            {"name":"No","value":2}
        ]
    ).execute()

    return game

def main():
        while True:
            datajson()
            load_options()
            option = menu()

            match option:
                #Open Navegator
                case 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
                    nav = open_navegator()

                    match nav:
                        case 1:
                            pyautogui.press("win")
                            pyautogui.PAUSE = 0.7
                            pyautogui.write("firefox")
                            pyautogui.PAUSE = 0.7
                            pyautogui.press("enter")
                        case 2:
                            pyautogui.press("win")
                            pyautogui.PAUSE = 0.7
                            pyautogui.write("chrome")
                            pyautogui.PAUSE = 0.7
                            pyautogui.press("enter")    
                        case 3:
                            pyautogui.press("win")
                            pyautogui.PAUSE = 0.7
                            pyautogui.write("edge")
                            pyautogui.PAUSE = 0.7
                            pyautogui.press("enter")
                        case 4:
                            continue
                #Get Cotation
                case 2:
                    url = urls[0]
                    
                    cot = get_cotation()

                    match cot:
                        case 1:
                            amountdollar = input("How many Dollars do you want to convert to BRL?: ")
                            
                            paramsdollar = {
                                "from":"USD",
                                "to":"BRL",
                                "amount":amountdollar
                            }

                            response = requests.get(url,params=paramsdollar)
                            data = response.json()

                            os.system("cls" if os.name == "nt" else "clear")
                            
                            print(f"{amountdollar} Dollars is equal to {data['rates']['BRL']:.2f} BRL (Brazilian Real)")
                        case 2:
                            amounteuro = input("How many Euros do you want to convert to BRL?: ")
                            
                            paramseuro = {
                                "from":"EUR",
                                "to":"BRL",
                                "amount":amounteuro
                            }

                            response = requests.get(url,params=paramseuro)
                            data = response.json()

                            os.system("cls" if os.name == "nt" else "clear")
                            
                            print(f"{amounteuro} euro is equal to {data['rates']['BRL']:.2f} BRL (Brazilian Real)")

                        case 3:
                            amountyen = input("How many Japonese Yen do you want to convert to BRL?: ")
                            
                            paramsyen = {
                                "from":"JPY",
                                "to":"BRL",
                                "amount":amountyen
                            }

                            response = requests.get(url,params=paramsyen)
                            data = response.json()

                            os.system("cls" if os.name == "nt" else "clear")
                            print(f"{amountyen} Japonese Yen in equal to {data['rates']['BRL']:.2f} BRL (Brazilian Real)")
                        case 4:
                            amount_BRL_to_USD = input("How many Brazilian Real do you want to convert to Dollar?: ")

                            params_BRL_to_USD = {
                                "from":"BRL",
                                "to":"USD",
                                "amount":amount_BRL_to_USD
                            }

                            response = requests.get(url,params=params_BRL_to_USD)
                            data = response.json()

                            os.system("cls" if os.name == "nt" else "clear")
                            print(f"{amount_BRL_to_USD} BRL (Brazilian Real) is equal to {data['rates']['USD']:.2f} Dollars")
                        case 5:
                            amount_BRL_to_EUR = input("How many Brazilian Real do you want to convert to Euro?: ")

                            params_BRL_to_EUR = {
                                "from":"BRL",
                                "to":"EUR",
                                "amount":amount_BRL_to_EUR
                            }

                            response = requests.get(url,params=params_BRL_to_EUR)
                            data = response.json()

                            os.system("cls" if os.name == "nt" else "clear")
                            print(f"{amount_BRL_to_EUR} BRL (Brazilian Real) is equal to {data['rates']['EUR']:.2f} Euros")
                        case 6:
                            amount_BRL_to_JPY = input("How many Brazilian Real do you want to convert to Japonese Yen?: ")

                            params_BRL_to_JPY = {
                                "from":"BRL",
                                "to":"JPY",
                                "amount":amount_BRL_to_JPY
                            }

                            response = requests.get(url,params=params_BRL_to_JPY)
                            data = response.json()

                            os.system("cls" if os.name == "nt" else "clear")
                            print(f"{amount_BRL_to_JPY} BRL (Brazilian Real) is equal to {data['rates']['JPY']:.2f} Japonese Yen")
                        case 7:
                            url_btc = urls[1]
                            paramsbtc = {
                                "ids":"bitcoin",
                                "vs_currencies":"brl"
                            }

                            res = requests.get(url_btc,params=paramsbtc)
                            data = res.json()

                            os.system("cls" if os.name == "nt" else "clear")
                            print(f"1 Bitcoin (BTC) is equal to {data['bitcoin']['brl']} BRL (Brazilian Real)")
                #Convertion Tool                
                case 3:
                    convertool = convertion_tool()

                    match convertool:
                        case 1:
                             temp_option = temperature_converter()

                             match temp_option:
                                case 1:
                                    celsius_to_fahrenheit = float(input("Enter the temperature in Celsius: "))
                                    fahrenheit = (celsius_to_fahrenheit * (9/5)) + 32
                                    
                                    os.system("cls" if os.name == "nt" else "clear")
                                    if rounder == True:
                                        fahrenheit = round(fahrenheit)
                                    else:
                                        fahrenheit = fahrenheit
                                    print(f"{celsius_to_fahrenheit}°C is equal to {fahrenheit}°F")
                                case 2:
                                    fahrenheit_to_celsius = float(input("Enter the temperature in Fahrenheit: "))
                                    celsius = (fahrenheit_to_celsius - 32) * (5/9)
                                    
                                    os.system("cls" if os.name == "nt" else "clear")
                                    print(f"{fahrenheit_to_celsius}°F is equal to {celsius}°C")
                                case 3:
                                    continue
                        case 2:
                            distance_option = distance_converter()

                            match distance_option:
                                case 1:
                                    km_to_miles = float(input("Enter the distance in Kilometers: "))
                                    miles = km_to_miles * 0.621371
                                    
                                    if rounder == True:
                                        miles = round(miles)
                                    else:
                                        miles = miles

                                    os.system("cls" if os.name == "nt" else "clear")
                                    print(f"{km_to_miles} Kilometers is equal to {miles} Miles")
                                case 2:
                                    miles_to_km = float(input("Enter the distance in Miles: "))
                                    kilometers = miles_to_km / 0.621371
                                    
                                    if rounder == True:
                                        kilometers = round(kilometers)
                                    else:
                                        kilometers = kilometers

                                    os.system("cls" if os.name == "nt" else "clear")
                                    print(f"{miles_to_km} Miles is equal to {kilometers} Kilometers")
                        case 3:
                            weight_option = weight_converter()

                            match weight_option:
                                case 1:
                                    kg_to_pounds = float(input("Enter the weight in Kilograms: "))
                                    pounds = kg_to_pounds * 2.20462
                                    
                                    os.system("cls" if os.name == "nt" else "clear")
                                    if rounder == True:
                                        pounds = round(pounds)
                                    else:
                                        pounds = pounds
                                    print(f"{kg_to_pounds} Kilograms is equal to {pounds} Pounds")
                                case 2:
                                    pounds_to_kg = float(input("Enter the weight in Pounds: "))
                                    kilograms = pounds_to_kg / 2.20462
                                    
                                    os.system("cls" if os.name == "nt" else "clear")
                                    print(f"{pounds_to_kg} Pounds is equal to {kilograms:.2f} Kilograms")
                                case 3:
                                    continue
                #Options                        
                case 4:
                    options = options_menu()

                    match options:
                        case 1:
                            new_name = input("Enter your user name: ") 
                            with open("options.json","w") as f:
                                json.dump([
                                    {
                                        "name":new_name
                                    },
                                    {
                                        "round":rounder
                                    }
                                ],f,indent=4)
                        case 2:
                            new_round = rounder_option()
                            with open("options.json","w") as f:
                                json.dump([
                                    {
                                        "name":nameuser
                                    },
                                    {
                                        "round":new_round
                                    }
                                ],f,indent=4)
                #weather tool
                case 5:
                    url_weather = urls[2]
                    url_geo = urls[3]

                    weather = weather_tool()

                    match weather:
                        case 1:
                            geo_response = requests.get(url_geo)
                            data_geo = geo_response.json()

                            if data_geo['status'] == 'success':
                                lat = data_geo['lat']
                                lon = data_geo['lon']
                                city = data_geo['city']
                                region = data_geo["regionName"]

                                params_weather = {
                                    "latitude":lat,
                                    "longitude":lon,
                                    "current_weather":"true"
                                }

                                response__weather = requests.get(url_weather,params=params_weather)
                                data_weather = response__weather.json()

                                os.system("cls" if os.name == 'nt' else "clear")
                                print(f'The current temperature in {city} - {region}  is {data_weather["current_weather"]["temperature"]}°C')                   
                            else:
                                os.system("cls" if os.name == 'nt' else "clear")
                                print("Program was not able to get your location")
                        case 2:
                            geo_response = requests.get(url_geo)
                            data_geo = geo_response.json()
                            
                            if data_geo["status"] == 'success':
                                lat = data_geo['lat']
                                lon = data_geo['lon']
                                city = data_geo['city']
                                region = data_geo["regionName"]

                                params_weather = {
                                    "latitude":lat,
                                    "longitude":lon,
                                    "current_weather":"true"
                                }


                                response__weather = requests.get(url_weather,params=params_weather)
                                data_weather = response__weather.json()
                                
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"The current wind speed in {city} - {region} is {data_weather['current_weather']['windspeed']}km/h")
                            else:
                                os.system("cls" if os.name == 'nt' else "clear")
                                print("Program was not able to get your location")
                        case 3:
                            geo_response = requests.get(url_geo)
                            data_geo = geo_response.json()

                            if data_geo["status"] == 'success':
                                lat = data_geo['lat']
                                lon = data_geo['lon']
                                city = data_geo['city']
                                region = data_geo["regionName"]

                                params_weather = {
                                    "latitude":lat,
                                    "longitude":lon,
                                    "current":"rain,precipitation"
                                }

                                response__weather = requests.get(url_weather,params=params_weather)
                                data_weather = response__weather.json()

                                current_data_rain = data_weather["current"]
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"The current rain in {city} - {region} is {current_data_rain['rain']}mm and precipitation is {current_data_rain['precipitation']}")
                case 6:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"right now the time is {time.strftime('%H:%M:%S')}, day is {time.strftime('%d/%m/%Y')} and week day is {time.strftime('%A')}")
                case 7:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    notices = get_notices()

                    match notices:
                        case 1:
                            notices_shows()
                        case 2:
                            continue
                case 8:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    random_option = random_choice()

                    match random_option:
                        case 1:
                            musics = [                             
                                random.choice(linkinpark),
                                random.choice(oldmusics),
                                random.choice(himymmusics),
                                random.choice(progmetal),
                                random.choice(baroesdapisadinha)
                            ]
                            
                            music = random.choice(musics)
                            print(f"The music chosen is: {music.replace('+',' ')}")
                            webbrowser.open(f"https://www.youtube.com/results?search_query={music}")
                        case 2:
                            movie = random.choice(movies)

                            print(f"The movie chosen is : {movie.replace('+',' ')}")
                            webbrowser.open(f"https://duckduckgo.com/?origin=funnel_home_google&t=h_&q={movie}&ia=web")
                        case 3:
                            muscular_group = random.choice(muscular_groups)
                            print(f"The muscular group chosen is: {muscular_group}")
                            webbrowser.open(f"https://duckduckgo.com/?origin=funnel_home_google&t=h_&q=exercises+for+{muscular_group}+workout&ia=web")
                        case 4:
                            youtube_channel = random.choice(youtube_channels)
                            print(f"The youtube channel chosen is : {youtube_channel}")
                            webbrowser.open(f"https://www.youtube.com/{youtube_channel}")
                        case 5:
                            continue
                case 9:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    game_choice = falling_blocks_game()

                    match game_choice:
                        case 1:
                            game = gameins.Game()
                            game.run()
                        case 2:
                            continue
                case 10:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    headortail = random.choice([1,2])

                    match headortail:
                        case 1:
                            print("The coin landed on heads")
                            engine.say("the coin landed on heads")
                            engine.runAndWait()
                        case 2:
                            print("The coin landed on tails")
                            engine.say("the coin landed on tails")
                            engine.runAndWait()
                case 11:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
                    r = sr.Recognizer()

                    with sr.Microphone() as source:
                        print("say something")
                        audio = r.listen(source)

                    try:
                        text = r.recognize_google(audio, language="pt-BR")
                        print(f"You said: {text}")
                    except sr.UnknownValueError:
                        print("could not understand audio")
                    except sr.RequestError as e:
                        print(f"could not request results; {e}")

                    if text.lower() in audioptions_music:
                        os.system('cls' if os.name == 'nt' else 'clear')

                        musics = [
                            random.choice(linkinpark),
                            random.choice(oldmusics),
                            random.choice(himymmusics),
                            random.choice(progmetal),
                            random.choice(baroesdapisadinha)
                        ]

                        music = random.choice(musics)

                        print(f"The music chosen is: {music.replace('+',' ')}")
                        engine.say("the music chosen is" + music.replace('+',' '))
                        engine.runAndWait()
                        webbrowser.open(f"https://www.youtube.com/results?search_query={music}")

                    elif text.lower() in audioptionsquit:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"Good bye {nameuser}!")
                        engine.say("Good bye" + nameuser)
                        engine.runAndWait()
                        break
                    elif text.lower() == audioptions_musics_special[0] or text.lower() == audioptions_musics_special[1]:
                        linkinparkrandom = random.choice(linkinpark)

                        os.system('cls' if os.name == 'nt' else 'clear')
                        webbrowser.open(f"https://www.youtube.com/results?search_query={linkinparkrandom}")
                        print(f"The linkin park music chosen is: {linkinparkrandom.replace('+',' ')}")
                        engine.say("the linkin park music chosen is" + linkinparkrandom.replace('+',' '))
                        engine.runAndWait()
                    elif text.lower() == audioptions_musics_special[2]:
                        oldmusicsrandom = random.choice(oldmusics)

                        os.system('cls' if os.name == 'nt' else 'clear')
                        webbrowser.open(f"https://www.youtube.com/results?search_query={oldmusicsrandom}")
                        print(f"The old music chosen is: {oldmusicsrandom.replace('+',' ')}")
                        engine.say("the old music chosen is" + oldmusicsrandom.replace('+',' '))
                        engine.runAndWait()

                    elif text.lower() == audioptions_musics_special[3]:
                        himymmusicsrandom = random.choice(himymmusics)

                        os.system('cls' if os.name == 'nt' else 'clear')
                        webbrowser.open(f"https://www.youtube.com/results?search_query={himymmusicsrandom}")
                        print(f"The how i met your mother music chosen is: {himymmusicsrandom.replace('+',' ')}")
                        engine.say("the how i met your mother music chosen is" + himymmusicsrandom.replace('+',' '))
                        engine.runAndWait()
                    elif text.lower() == audioptions_musics_special[4]:
                        progmetalrandom = random.choice(progmetal)

                        os.system("cls" if os.name == "nt" else "clear")
                        webbrowser.open(f"https://www.youtube.com/results?search_query={progmetalrandom}")
                        print(f"the prog metal music chosen is: {progmetalrandom.replace('+',' ')}")
                        engine.say("the prog metal music chosen is" + progmetalrandom.replace('+',' '))
                        engine.runAndWait()
                    elif text.lower() == audioptions_musics_special[5]:
                        baroesdapisadinharandom = random.choice(baroesdapisadinha)

                        os.system("cls" if os.name == 'nt' else 'clear')
                        webbrowser.open(f"https://www.youtube.com/results?search_query={baroesdapisadinharandom}")
                        print(f"The baroes da pisadinha music chosen is: {baroesdapisadinharandom.replace('+',' ')}")
                        engine.say("the baroes da pisadinha music chosen is" + baroesdapisadinharandom.replace('+',' '))
                        engine.runAndWait()
                    elif text.lower() in audioptionstime:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"right now the time is {time.strftime('%H:%M:%S')}, day is {time.strftime('%d/%m/%Y')} and week day is {time.strftime('%A')}")
                        engine.say("right now the time is" + time.strftime('%H:%M:%S') + "day is" + time.strftime('%d/%m/%Y') + "and week day is" + time.strftime('%A'))
                        engine.runAndWait()
                    
                    elif text.lower() in audioptionstraining:
                        os.system('cls' if os.name == 'nt' else 'clear')

                        muscular_group = random.choice(muscular_groups)
                        print(f"The muscular group chosen is: {muscular_group}")
                        engine.say("the muscular group chosen is" + muscular_group)
                        engine.runAndWait()
                        webbrowser.open(f"https://duckduckgo.com/?origin=funnel_home_google&t=h_&q=exercises+for+{muscular_group}+workout&ia=web")
                    
                    elif text.lower() == "o que sobra para o beta":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Nothing (brutal)")
                        engine.say("nothing")
                        engine.runAndWait()
                    elif text.lower() == "comando":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("comandos de música:")
                        for i, n in enumerate(audioptions_music, start=1):
                            print(f"{i}. {n}")
                        
                        print("comandos de saída:")
                        for i, n in enumerate(audioptionsquit, start=1):
                            print(f"{i}. {n}")

                        print("comandos de data e hora:")
                        for i, n in enumerate(audioptionstime, start=1):
                            print(f"{i}. {n}")

                        print("comandos de treino:")
                        for i, n in enumerate(audioptionstraining, start=1):
                            print(f"{i}. {n}")
                        
                        print("comandos de música especial:")
                        for i, n in enumerate(audioptions_musics_special, start=1):
                            print(f"{i}. {n}")
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"we do not have the option '{text}' in our voice commands")   
                case 12:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"Good bye {nameuser}!")
                    break