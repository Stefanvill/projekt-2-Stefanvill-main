import requests
import os
import time
import json

def append_to_json_file(data): #funktion som appendar data till json filen 
    try: #en try för att försöka öppna filen och om det ej går eller att den ej existerar så skapas en ny fil
        with open("data.json", "r") as file: #öppnar filen med "r" = read [OBS] kommer ej ihåg om detta var det korrekta sättet
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):#exceptions är felkoderna för en tom fil eller en fil som ej existerar
        existing_data = [] #skapar en lista om filen är tom

    existing_data.append(data) 

    with open("data.json", "w") as file: #öppnar filen i write "läge"
        json.dump(existing_data, file, indent=4) #skriver in datan i filen med en indent på 4 som motsvarar en tab kod tagen från [https://ioflood.com/blog/python-json-pretty-print/]

while True:
    os.system('cls' if os.name == 'nt' else 'clear') #clearar terminalen kod från stackoverflow [https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python]
    time.sleep(1) #gör så att programmet väntar 1 sekund för att få användaren att hinna läsa vad som står
    print("1. Save login credentials\n2. Print login credentials\n3. Print fuel prices\n4. Exit") #printar ut valen som användaren kan göra
    user_input = int(input("Choose an option: "))

    if user_input == 1:#här matar användaren in url, username och password som sedan apendas in till json filen data.json
        url = input("Enter the URL: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        data = {"url": url, "username": username, "password": password}
        append_to_json_file(data)
    elif user_input == 2:
        # printar login credentials
        pass
    elif user_input == 3:
        response = requests.get("https://henrikhjelm.se/api/getdata.php?lan=stockholms-lan")
        answer = response.json()
        print(f"Cirkle K vikdalsvägens Diesel pris ligger på {answer['stockholmslan_Circle_K_NackaVikdalsvagen_41__diesel']} kr")
        print(f"Cirkle K vikdalsvägens 95 oktan pris ligger på {answer['stockholmslan_Circle_K_NackaVikdalsvagen_41__95']} kr")
        time.sleep(3)
        # printar bensin priser
        pass
    elif user_input == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid input, please try again.")
        time.sleep(1)
        pass