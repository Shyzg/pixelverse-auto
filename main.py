from Battle import Battle
from Pixelverse import UserPixel
from random import randint
import asyncio
from colorama import Fore, Style, init, Back 
import os
from time import sleep
import traceback

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clear()

def split_chunk(var):
    n = 3
    var = var[::-1]
    return ' '.join([var[i:i + n] for i in range(0, len(var), n)])[::-1]

async def main():
    init() # colorama
    
    user = UserPixel()

    while True:
        userInfo = user.getUser()
        stats = user.getStats()
        
        message = f"""
                                    {Back.MAGENTA}{Fore.WHITE}PixelBot{Style.RESET_ALL} | Made by {Back.MAGENTA + Fore.WHITE}S1NJED{Style.RESET_ALL}
                                    
                                        Support me please :)
                            {Fore.GREEN}$USDT{Style.RESET_ALL} (ERC20 or BEP20): {Back.WHITE + Fore.BLACK}0x0A9072E3C4Fae8e239Db12B3287eF88A3e9Da5A2{Style.RESET_ALL}
                                                                                
                                        Logged in as {Style.BRIGHT + Fore.GREEN}{userInfo['username']}{Style.RESET_ALL}{Fore.GREEN + Style.BRIGHT}
                                         
============================================== {Style.RESET_ALL} {Back.YELLOW + Fore.BLACK}STATS{Style.RESET_ALL} {Fore.GREEN + Style.BRIGHT} ==============================================  {Style.RESET_ALL}

                                        > {Back.YELLOW + Fore.BLACK}Balance{Style.RESET_ALL}: {Style.BRIGHT}{split_chunk(str(int(userInfo['clicksCount'])))}{Style.RESET_ALL}

                                        > battlesCount{Style.RESET_ALL}: {Style.BRIGHT}{split_chunk(str(stats['battlesCount']))}{Style.RESET_ALL} 
                                        > {Back.GREEN}Wins{Style.RESET_ALL}:         {Style.BRIGHT}{split_chunk(str(stats['wins']))}{Style.RESET_ALL}
                                        > {Back.RED}Loses{Style.RESET_ALL}:        {Style.BRIGHT}{split_chunk(str(stats['loses']))}{Style.RESET_ALL}
                                        > {Back.GREEN}Money Won{Style.RESET_ALL}:    {Style.BRIGHT}{split_chunk(str(stats['winsReward']))}{Style.RESET_ALL}
                                        > {Back.RED}Money Lost{Style.RESET_ALL}:   {Style.BRIGHT}-{split_chunk(str(abs(stats['losesReward'])))}{Style.RESET_ALL}
                                        > {Back.GREEN}Total earned{Style.RESET_ALL}: {Style.BRIGHT}{split_chunk(str(stats['winsReward'] - stats['losesReward']))}{Style.RESET_ALL}

        """
        print(message)
        
        # We create a new Battle instance
        battle = Battle()
        
        await battle.connect()
        del battle
        
        user.claim()
        user.upgradePets()
        
        timeToWait = randint(5, 10)
        print(f"                                        > Waiting {Back.RED + Fore.WHITE}{timeToWait}{Style.RESET_ALL} seconds.")
        await asyncio.sleep(timeToWait)

        clear()   

''' TODO:
POST https://api-clicker.pixelverse.xyz/api/pets/buy?tg-id=&secret=
'''

if __name__ == '__main__':
    while True:
        try:
            asyncio.run(main())       
        except KeyboardInterrupt:
            print("                                        > Goodbye :)")
            break
        except Exception as err:
            clear()
            traceback.print_exc()
            print("BOT HAS CRASHED :(")
            pixelverse = UserPixel()
            
            if pixelverse.isBroken():
                print(f"Pixelverse seems to be down for the moment, retrying again in 5 minutes ...")
                sleep(60*5)
            else:
                print("The problem does not come from the server, try to restart the bot or if the problem persist open a ticket with a screen of this error ...")
                
                print("Trygin again in 60 seconds ...")
                sleep(60)
                