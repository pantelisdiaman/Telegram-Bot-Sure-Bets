import warnings
# Ignore all warnings
warnings.filterwarnings("ignore")

import pandas as pd
import pyperclip
import webbrowser
import os
import time
import helpers.telegram_bot as telegram_bot

# Keep a list of the already sent notifications (per match + bet type)
sentNotifications = [[]]

while True:
    # wrap this in a try to ensure that even if it fails, it will still work
    try:
        # Open chrome on the odds safari site to scrape
        URL = "https://www.oddssafari.gr/en/sure-bets"
        webbrowser.open(URL)

        # Wait for the scrape
        time.sleep(90)

        # Kill chrome
        os.system("taskkill /im chrome.exe /f >nul 2>&1")

        # Read clipboard
        clipboard = pyperclip.paste()

        # Get all sure bets
        sureBets = clipboard.split("BREAK")[0:len(clipboard.split("BREAK")) - 2]
        
        # Split and check all sure bets
        for sureBet in sureBets:
            data = sureBet.split("|")[0:len(sureBet.split("|")) - 1]
            
            # Get all data
            league = data[0]
            match = data[1].replace("\r\n", "-")
            market = data[2]
            matchTime = data[3]
            profit = data[4]
            bookmaker1 = data[5]
            market1 = data[6]
            odd1 = data[7]
            bookmaker2 = data[8]
            market2 = data[9]
            odd2 = data[10]
            bookmaker3 = ""
            market3 = ""
            odd3 = ""
            
            # Get the 3rd market's details only if they exist
            if len(data) == 14:
                bookmaker3 = data[11]
                market3 = data[12]
                odd3 = data[13]
            
            # Send the match only if it is not sent yet
            if [match, market] not in sentNotifications:
                telegram_bot.sendNotification(league, match, market, matchTime, profit, bookmaker1, market1, odd1, bookmaker2, market2, odd2, bookmaker3, market3, odd3)
                sentNotifications.append([match, market]);

        # Sleep for 3 minutes then repeat
        time.sleep(180)
        
    except Exception as e:
        # Print the exception that happened
        print("Something failed. The error is: ",e)
