import threading
import requests
import discord
import random
import time
import os

from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle

init(convert=True)
guildsIds = []
friendsIds = []
clear = lambda: os.system('cls')
clear()

class Login(discord.Client):
    async def on_connect(self):
        for g in self.guilds:
            guildsIds.append(g.id)
 
        for f in self.user.friends:
            friendsIds.append(f.id)

        await self.logout()

    def run(self, token):
        try:
            super().run(token, bot=False)
        except Exception as e:
            print(f"[{Fore.RED}-{Fore.RESET}] Invalid token", e)
            input("Press any key to exit..."); exit(0)

def tokenLogin(token):
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('lib/chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }
            """
    driver.get("https://discord.com/login")
    driver.execute_script(script + f'\nlogin("{token}")')

def getBanner():
    banner = f'''
   /$$                                   /$$           /$$                           /$$          
  | $$                                  |__/          | $$                          |__/          
 /$$$$$$    /$$$$$$  /$$$$$$  /$$    /$$ /$$  /$$$$$$$| $$        /$$$$$$   /$$$$$$  /$$ /$$$$$$$ 
|_  $$_/   /$$__  $$|____  $$|  $$  /$$/| $$ /$$_____/| $$       /$$__  $$ /$$__  $$| $$| $$__  $$
  | $$    | $$  \__/ /$$$$$$$ \  $$/$$/ | $$|  $$$$$$ | $$      | $$  \ $$| $$  \ $$| $$| $$  \ $$
  | $$ /$$| $$      /$$__  $$  \  $$$/  | $$ \____  $$| $$      | $$  | $$| $$  | $$| $$| $$  | $$
  |  $$$$/| $$     |  $$$$$$$   \  $/   | $$ /$$$$$$$/| $$$$$$$$|  $$$$$$/|  $$$$$$$| $$| $$  | $$
   \___/  |__/      \_______/    \_/    |__/|_______/ |________/ \______/  \____  $$|__/|__/  |__/
                                                                           /$$  \ $$              
                                                                          |  $$$$$$/              
                                                                           \______/                            
    '''.replace('█', f'{Fore.BLUE}█{Fore.RESET}')
    return banner

def startMenu():
    print(getBanner())
    print(f'token', end=''); token = input('  :  ')
    tokenLogin(token)


        
if __name__ == '__main__':
    startMenu()
