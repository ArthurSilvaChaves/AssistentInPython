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

def load_options():
    global nameuser
    global rounder
    global choicelanguage

    with open("options.json","r") as f:
        options = json.load(f)
 
        nameuser = options[0]["name"]
        rounder = options[1]["round"]
        choicelanguage = options[2]["language"]

load_options()

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
    global urls

    with open("data.json","r") as f:
        data = json.load(f)

    audioptions_music = data["options"]["audioptions_music"]
    audioptions_musics_special = data["options"]["audioptions_musics_special"]
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

def language_enus():
    global text_enus

    with open("language.json","r") as f:

        language = json.load(f)

        text_enus = language["enus"]

    return text_enus

def language_ptbr():
    global text_ptbr

    with open("language.json","r") as f:
         
         language = json.load(f)

         text_ptbr = language["ptbr"]

         
    return text_ptbr

language_enus()
language_ptbr() 

def language(choice=choicelanguage):
    if choice == 1:
        language = language_enus()
        return language
    elif choice == 2:
        language  = language_ptbr()
        return language 

text_language = language()


#menu principal
def menu():
    choices = inquirer.select(
        message = text_language[0] + nameuser + text_language[1],
        choices = [
            {"name":text_language[2], "value":1},
            {"name":text_language[3], "value":2},
            {"name":text_language[4], "value":3},
            {"name":text_language[5], "value":4},
            {"name":text_language[6], "value":5},
            {"name":text_language[7],"value":6},
            {"name":text_language[8],"value":7},
            {"name":text_language[9],"value":8},
            {"name":text_language[10],"value":9},
            {"name":text_language[11],"value":10},
            {"name":text_language[12],"value":11},
            {"name":text_language[13],"value":12}
        ]
    ).execute()

    return choices

def options_menu():
    options = inquirer.select(
        message= text_language[14],
        choices = [
            {"name":text_language[15],"value":1},
            {"name":text_language[16], "value":2},
            {"name":text_language[17],"value":3},
            {"name":text_language[18],"value":4},
        ]
    ).execute()

    return options

def language_menu():
    language = inquirer.select(
        message=text_language[19],
        choices = [
            {"name":text_language[20],"value":1},
            {"name":text_language[21],"value":2},
            {"name":text_language[22],"value":3}
        ]
    ).execute()

    return language

def rounder_option():
    round_choice = inquirer.select(
        message=text_language[23],
        choices=[
            {"name":text_language[24],"value":True},
            {"name":text_language[25],"value":False}
        ]
    ).execute()

    return round_choice

def open_navegator():
    navegator = inquirer.select(
        message=text_language[26],
        choices = [
             {"name":text_language[27],"value":1},
             {"name":text_language[28],"value":2},
             {"name":text_language[29],"value":3},
             {"name":text_language[30],"value":4}
        ]
    ).execute()

    return navegator

def get_cotation():
    cotation = inquirer.select(
        message=text_language[31],
        choices = [
            {"name":text_language[32],"value":1},
            {"name":text_language[33],"value":2},
            {"name":text_language[34],"value":3},
            {"name":text_language[35],"value":4},
            {"name":text_language[36],"value":5},
            {"name":text_language[37],"value":6},
            {"name":text_language[38],"value":7},
            {"name":text_language[39],"value":8}
        ]
    ).execute()

    return cotation

def temperature_converter():
    temperature_option = inquirer.select(
        message=text_language[40],
        choices = [
            {"name":text_language[41],"value":1},
            {"name":text_language[42],"value":2},
            {"name":text_language[43],"value":3}
        ]
    ).execute()

    return temperature_option

def distance_converter():
    distance_option = inquirer.select(
        message=text_language[44],
        choices = [
            {"name":text_language[45],"value":1},
            {"name":text_language[46],"value":2},
            {"name":text_language[47],"value":3}
        ]
    ).execute()

    return distance_option

def weight_converter():
    weight_option = inquirer.select(
        message=text_language[48],
        choices = [
            {"name":text_language[49],"value":1},
            {"name":text_language[50],"value":2},
            {"name":text_language[51],"value":3}
        ]
    ).execute()

    return weight_option

def convertion_tool():
    convertion = inquirer.select(
        message=text_language[52],
        choices = [
            {"name":text_language[53],"value":1},
            {"name":text_language[54],"value":2},
            {"name":text_language[55],"value":3},
            {"name":text_language[56],"value":4}
        ]
    ).execute()

    return convertion

def get_notices():
    notices = inquirer.select(
        message=text_language[57],
        choices = [
            {"name":text_language[58],"value":1},
            {"name":text_language[59],"value":2}
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

    print(text_language[60])

    for i,n in enumerate(data['hits'][:5],start=1):
        title = n['title'] or "No title"
        link = n['url'] or 'no link available'
        author = n['author']

        print(f'{i}. {title}\n   Author: {author}\n   Link: {link}')
    
def weather_tool():
    weather = inquirer.select(
        message=text_language[61],
        choices = [
            {"name":text_language[62],"value":1},
            {"name":text_language[63],"value":2},
            {"name":text_language[64],"value":3},
            {"name":text_language[65],"value":4}
        ]
    ).execute()

    return weather

def random_choice():
    rand_choice = inquirer.select(
        message=text_language[66],
        choices = [
            {"name":text_language[67],"value":1},
            {"name":text_language[68],"value":2},
            {"name":text_language[69],"value":3},
            {"name":text_language[70],"value":4},
            {"name":text_language[71],"value":5}
        ]
    ).execute()

    return rand_choice

def falling_blocks_game():
    game = inquirer.select(
        message=text_language[72],
        choices = [
            {"name":text_language[73],"value":1},
            {"name":text_language[74],"value":2}
        ]
    ).execute()

    return game

def main():
        while True:
            language()
            datajson()
            load_options()
            option = menu()
            text_language = language()

            if option == 1:
                    #Open Navegator
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
                    nav = open_navegator()

                    if nav == 1:
                            pyautogui.press("win")
                            pyautogui.PAUSE = 0.7
                            pyautogui.write("firefox")
                            pyautogui.PAUSE = 0.7
                            pyautogui.press("enter")
                    elif nav == 2:
                            pyautogui.press("win")
                            pyautogui.PAUSE = 0.7
                            pyautogui.write("chrome")
                            pyautogui.PAUSE = 0.7
                            pyautogui.press("enter")    
                    elif nav ==  3:
                            pyautogui.press("win")
                            pyautogui.PAUSE = 0.7
                            pyautogui.write("edge")
                            pyautogui.PAUSE = 0.7
                            pyautogui.press("enter")
                    else :
                            continue
                    #Get Cotation
            elif option == 2:
                    url = urls[0]
                    
                    cot = get_cotation()

                    language()
                    
                    text_language = language()
                    if cot == 1:
                        amountdollar = input(text_language[75])
                            
                        paramsdollar = {
                            "from":"USD",
                            "to":"BRL",
                            "amount":amountdollar
                        }

                        response = requests.get(url,params=paramsdollar)
                        data = response.json()

                        os.system("cls" if os.name == "nt" else "clear")
                            
                        print(amountdollar + text_language[76],data['rates']['BRL'],text_language[77])
                    elif cot == 2:
                        amounteuro = input(text_language[78])
                            
                        paramseuro = {
                            "from":"EUR",
                            "to":"BRL",
                            "amount":amounteuro
                        }

                        response = requests.get(url,params=paramseuro)
                        data = response.json()

                        os.system("cls" if os.name == "nt" else "clear")
                            
                        print(amounteuro, text_language[79],data['rates']['BRL'],text_language[80])

                    elif cot == 3:
                        amountyen = input(text_language[81])
                            
                        paramsyen = {
                            "from":"JPY",
                            "to":"BRL",
                            "amount":amountyen
                        }

                        response = requests.get(url,params=paramsyen)
                        data = response.json()

                        os.system("cls" if os.name == "nt" else "clear")
                        print(amountyen, text_language[82] ,data['rates']['BRL'], text_language[83])
                    elif cot ==  4:
                        amount_BRL_to_USD = input(text_language[84])

                        params_BRL_to_USD = {
                            "from":"BRL",
                            "to":"USD",
                            "amount":amount_BRL_to_USD
                        }

                        response = requests.get(url,params=params_BRL_to_USD)
                        data = response.json()

                        os.system("cls" if os.name == "nt" else "clear")
                        print(amount_BRL_to_USD,text_language[85],data['rates']['USD'], text_language[86])
                    elif cot == 5:
                        amount_BRL_to_EUR = input(text_language[87])

                        params_BRL_to_EUR = {
                            "from":"BRL",
                            "to":"EUR",
                            "amount":amount_BRL_to_EUR
                        }

                        response = requests.get(url,params=params_BRL_to_EUR)
                        data = response.json()

                        os.system("cls" if os.name == "nt" else "clear")
                        print(amount_BRL_to_EUR, text_language[88], data['rates']['EUR'], text_language[89])
                    elif cot == 6:
                        amount_BRL_to_JPY = input(text_language[90])

                        params_BRL_to_JPY = {
                            "from":"BRL",
                            "to":"JPY",
                            "amount":amount_BRL_to_JPY
                        }

                        response = requests.get(url,params=params_BRL_to_JPY)
                        data = response.json()

                        os.system("cls" if os.name == "nt" else "clear")
                        print(amount_BRL_to_JPY, text_language[91],data['rates']['JPY'], text_language[92])
                    elif cot == 7:
                        url_btc = urls[1]
                        paramsbtc = {
                            "ids":"bitcoin",
                            "vs_currencies":"brl"
                        }

                        res = requests.get(url_btc,params=paramsbtc)
                        data = res.json()

                        os.system("cls" if os.name == "nt" else "clear")
                        print(text_language[93],{data['bitcoin']['brl']},text_language[94])
                    else:
                        continue
                #Convertion Tool                
            elif option == 3:
                    convertool = convertion_tool()

                    language()
                    text_language = language()

                    match convertool:
                        case 1:
                             temp_option = temperature_converter()

                             match temp_option:
                                case 1:
                                    celsius_to_fahrenheit = float(input(text_language[95]))
                                    fahrenheit = (celsius_to_fahrenheit * (9/5)) + 32
                                    
                                    os.system("cls" if os.name == "nt" else "clear")
                                    if rounder == True:
                                        fahrenheit = round(fahrenheit)
                                    else:
                                        fahrenheit = fahrenheit
                                    print(celsius_to_fahrenheit, text_language[96],  fahrenheit,"°F")
                                case 2:
                                    fahrenheit_to_celsius = float(input(text_language[97]))
                                    celsius = (fahrenheit_to_celsius - 32) * (5/9)
                                    
                                    os.system("cls" if os.name == "nt" else "clear")
                                    print(fahrenheit_to_celsius,text_language[98],celsius,"°C")
                                case 3:
                                    continue
                        case 2:
                            distance_option = distance_converter()

                            match distance_option:
                                case 1:
                                    km_to_miles = float(input(text_language[99]))
                                    miles = km_to_miles * 0.621371
                                    
                                    if rounder == True:
                                        miles = round(miles)
                                    else:
                                        miles = miles

                                    os.system("cls" if os.name == "nt" else "clear")
                                    print(km_to_miles,text_language[100],miles,text_language[101])
                                case 2:
                                    miles_to_km = float(input(text_language[102]))
                                    kilometers = miles_to_km / 0.621371
                                    
                                    if rounder == True:
                                        kilometers = round(kilometers)
                                    else:
                                        kilometers = kilometers

                                    os.system("cls" if os.name == "nt" else "clear")
                                    print(miles_to_km,text_language[103],kilometers, text_language[104])
                        case 3:
                            weight_option = weight_converter()

                            match weight_option:
                                case 1:
                                    kg_to_pounds = float(input(text_language[105]))
                                    pounds = kg_to_pounds * 2.20462
                                    
                                    os.system("cls" if os.name == "nt" else "clear")
                                    if rounder == True:
                                        pounds = round(pounds)
                                    else:
                                        pounds = pounds
                                    print(kg_to_pounds,text_language[106], pounds, text_language[107])
                                case 2:
                                    pounds_to_kg = float(input(text_language[108]))
                                    kilograms = pounds_to_kg / 2.20462

                                    os.system("cls" if os.name == "nt" else "clear")
                                    print(pounds_to_kg,text_language[109], kilograms,text_language[110])
                                case 3:
                                    continue
                #Options                        
            elif option ==  4:
                    options = options_menu()

                    language()
                    text_language = language()

                    match options:
                        case 1:
                            new_name = input(text_language[111]) 
                            with open("options.json","w") as f:
                                json.dump([
                                    {
                                        "name":new_name
                                    },
                                    {
                                        "round":rounder
                                    },
                                    {
                                        "language":choicelanguage
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
                                    },
                                    {
                                        "language":choicelanguage
                                    }
                                ],f,indent=4)
                        case 3:
                            new_language = language_menu()
                            with open("options.json","w") as f:
                                json.dump([
                                    {
                                        "name":nameuser
                                    },
                                    {
                                        "round":rounder
                                    },
                                    {
                                        "language":new_language
                                    }
                                ],f,indent=4)
                            
                #weather tool
            elif option == 5:
                    url_weather = urls[2]
                    url_geo = urls[3]

                    weather = weather_tool()

                    language()
                    text_language = language()

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
                                print(text_language[112], f"{city} - {region}",  text_language[113], data_weather["current_weather"]["temperature"],"°C")                   
                            else:
                                os.system("cls" if os.name == 'nt' else "clear")
                                print(text_language[114])
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
                                print(text_language[115], f"{city} - {region}", text_language[116], data_weather['current_weather']['windspeed'],"km/h")
                            else:
                                os.system("cls" if os.name == 'nt' else "clear")
                                print(text_language[117])
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
                                print(text_language[118], f"{city} - {region}",text_language[119], f"{current_data_rain['rain']}mm ", text_language[120], current_data_rain['precipitation'])
            elif option == 6:
                    language()
                    text_language = language()
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(text_language[121], time.strftime('%H:%M:%S'), text_language[122] ,time.strftime('%d/%m/%Y'), text_language[123], time.strftime('%A'))
            elif option == 7:
                    language()
                    text_language = language()
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    notices = get_notices()

                    match notices:
                        case 1:
                            notices_shows()
                        case 2:
                            continue
            elif option == 8:
                    language()
                    text_language = language()
                    
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
                            print(text_language[124],music.replace('+',' '))
                            webbrowser.open(f"https://www.youtube.com/results?search_query={music}")
                        case 2:
                            movie = random.choice(movies)

                            print(text_language[125], movie.replace('+',' '))
                            webbrowser.open(f"https://duckduckgo.com/?origin=funnel_home_google&t=h_&q={movie}&ia=web")
                        case 3:
                            muscular_group = random.choice(muscular_groups)
                            print(text_language[126],muscular_group)
                            webbrowser.open(f"https://duckduckgo.com/?origin=funnel_home_google&t=h_&q=exercises+for+{muscular_group}+workout&ia=web")
                        case 4:
                            youtube_channel = random.choice(youtube_channels)
                            print(text_language[127],youtube_channel)
                            webbrowser.open(f"https://www.youtube.com/{youtube_channel}")
                        case 5:
                            continue
            elif option == 9:
                    language()
                    text_language = language()
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    game_choice = falling_blocks_game()

                    match game_choice:
                        case 1:
                            game = gameins.Game()
                            game.run()
                        case 2:
                            continue
            elif option == 10:
                    language()
                    text_language = language()
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    headortail = random.choice([1,2])

                    match headortail:
                        case 1:
                            print(text_language[128])
                            engine.say("the coin landed on heads")
                            engine.runAndWait()
                        case 2:
                            print(text_language[129])
                            engine.say("the coin landed on tails")
                            engine.runAndWait()
            elif option == 11:
                    language()
                    text_language = language()
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
                    r = sr.Recognizer()

                    with sr.Microphone() as source:
                        print(text_language[130])
                        audio = r.listen(source)

                    try:
                        text = r.recognize_google(audio, language="pt-BR")
                        print(text_language[131],text)
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

                        print(text_language[132], music.replace('+',' '))
                        engine.say("the music chosen is" + music.replace('+',' '))
                        engine.runAndWait()
                        webbrowser.open(f"https://www.youtube.com/results?search_query={music}")

                    elif text.lower() in audioptionsquit:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(text_language[133], f"{nameuser}!")
                        engine.say("Good bye" + nameuser)
                        engine.runAndWait()
                        break
                    elif text.lower() == audioptions_musics_special[0] or text.lower() == audioptions_musics_special[1]:
                        linkinparkrandom = random.choice(linkinpark)

                        os.system('cls' if os.name == 'nt' else 'clear')
                        webbrowser.open(f"https://www.youtube.com/results?search_query={linkinparkrandom}")
                        print(text_language[134], linkinparkrandom.replace('+',' '))
                        engine.say("the linkin park music chosen is" + linkinparkrandom.replace('+',' '))
                        engine.runAndWait()
                    elif text.lower() == audioptions_musics_special[2]:
                        oldmusicsrandom = random.choice(oldmusics)

                        os.system('cls' if os.name == 'nt' else 'clear')
                        webbrowser.open(f"https://www.youtube.com/results?search_query={oldmusicsrandom}")
                        print(text_language[135], oldmusicsrandom.replace('+',' '))
                        engine.say("the old music chosen is" + oldmusicsrandom.replace('+',' '))
                        engine.runAndWait()

                    elif text.lower() == audioptions_musics_special[3]:
                        himymmusicsrandom = random.choice(himymmusics)

                        os.system('cls' if os.name == 'nt' else 'clear')
                        webbrowser.open(f"https://www.youtube.com/results?search_query={himymmusicsrandom}")
                        print(text_language[136],himymmusicsrandom.replace('+',' '))
                        engine.say("the how i met your mother music chosen is" + himymmusicsrandom.replace('+',' '))
                        engine.runAndWait()
                    elif text.lower() == audioptions_musics_special[4]:
                        progmetalrandom = random.choice(progmetal)

                        os.system("cls" if os.name == "nt" else "clear")
                        webbrowser.open(f"https://www.youtube.com/results?search_query={progmetalrandom}")
                        print("the prog metal music chosen is:" ,progmetalrandom.replace('+',' '))
                        engine.say("the prog metal music chosen is" + progmetalrandom.replace('+',' '))
                        engine.runAndWait()
                    elif text.lower() == audioptions_musics_special[5]:
                        baroesdapisadinharandom = random.choice(baroesdapisadinha)

                        os.system("cls" if os.name == 'nt' else 'clear')
                        webbrowser.open(f"https://www.youtube.com/results?search_query={baroesdapisadinharandom}")
                        print(text_language[137] ,baroesdapisadinharandom.replace('+',' '))
                        engine.say("the baroes da pisadinha music chosen is" + baroesdapisadinharandom.replace('+',' '))
                        engine.runAndWait()
                    elif text.lower() in audioptionstime:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(text_language[138], f"{time.strftime('%H:%M:%S')},", text_language[139], time.strftime('%d/%m/%Y'), text_language[140],time.strftime('%A'))
                        engine.say("right now the time is" + time.strftime('%H:%M:%S') + "day is" + time.strftime('%d/%m/%Y') + "and week day is" + time.strftime('%A'))
                        engine.runAndWait()
                    
                    elif text.lower() in audioptionstraining:
                        os.system('cls' if os.name == 'nt' else 'clear')

                        muscular_group = random.choice(muscular_groups)
                        print(text_language[141],muscular_group)
                        engine.say("the muscular group chosen is" + muscular_group)
                        engine.runAndWait()
                        webbrowser.open(f"https://duckduckgo.com/?origin=funnel_home_google&t=h_&q=exercises+for+{muscular_group}+workout&ia=web")
                    
                    elif text.lower() == "o que sobra para o beta":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(text_language[142])
                        engine.say("nothing")
                        engine.runAndWait()
                    elif text.lower() == "comando":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(text_language[143])
                        for i, n in enumerate(audioptions_music, start=1):
                            print(f"{i}. {n}")
                        
                        print(text_language[144])
                        for i, n in enumerate(audioptionsquit, start=1):
                            print(f"{i}. {n}")

                        print(text_language[145])
                        for i, n in enumerate(audioptionstime, start=1):
                            print(f"{i}. {n}")

                        print(text_language[146])
                        for i, n in enumerate(audioptionstraining, start=1):
                            print(f"{i}. {n}")
                        
                        print(text_language[147])
                        for i, n in enumerate(audioptions_musics_special, start=1):
                            print(f"{i}. {n}")
                    elif text.lower() == "teste":
                        print(text_language[0])
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(text_language[148], f"({text})")   
            elif option == 12:
                    language()
                    text_language = language()
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(text_language[149], f"{nameuser}!")
                    break