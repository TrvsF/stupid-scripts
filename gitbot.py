import requests 
from colorama import Fore, init

URL = 'https://camo.githubusercontent.com/1d0a9c97b32e5869b348f204a10f17cfa6b1427a/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d7472767366'

def getBanner():
    banner = f'''
           /$$   /$$     /$$$$$$$              /$$    
          |__/  | $$    | $$__  $$            | $$    
  /$$$$$$  /$$ /$$$$$$  | $$  \ $$  /$$$$$$  /$$$$$$  
 /$$__  $$| $$|_  $$_/  | $$$$$$$  /$$__  $$|_  $$_/  
| $$  \ $$| $$  | $$    | $$__  $$| $$  \ $$  | $$    
| $$  | $$| $$  | $$ /$$| $$  \ $$| $$  | $$  | $$ /$$
|  $$$$$$$| $$  |  $$$$/| $$$$$$$/|  $$$$$$/  |  $$$$/
 \____  $$|__/   \___/  |_______/  \______/    \___/  
 /$$  \ $$                                            
|  $$$$$$/                                            
 \______/                                             
                           
    '''.replace('█', f'{Fore.BLUE}█{Fore.RESET}')
    return banner

def startBot():
    print(getBanner())
    print(f'attempts', end=''); attempts = int(input('  :  '))

    for i in range(attempts):
        i+=1
        requests.get(URL)
        if (i % 100 == 0):
            print ('sent ' + str(i) + ' requests')

if __name__ == '__main__':
    startBot()