import asyncio
import os
import json
import sys
from Battle import Battle
from Pixel import Pixel
from datetime import datetime
from colorama import Fore, Style, init


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def split_chunk(var):
    if isinstance(var, int):
        var = str(var)
    n = 3
    var = var[::-1]
    return ' '.join([var[i:i + n] for i in range(0, len(var), n)])[::-1]

async def main():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    init()
    battle = Battle()
    user = Pixel()
    users = user.get_users()

    print(f"👻 {Fore.CYAN+Style.BRIGHT}[ {users.get('username', 'Unknown')} ]"
          f"{Fore.WHITE+Style.BRIGHT} | "
          f"💰 {Fore.YELLOW+Style.BRIGHT}[ {split_chunk(str(int(users['clicksCount'])))} Coins ]")
    print(f"🍏 {Fore.GREEN+Style.BRIGHT}[ {split_chunk(str(int(battle.wins)))} Wins ]"
          f"{Fore.WHITE+Style.BRIGHT} | "
          f"🍎 {Fore.RED+Style.BRIGHT}[ {split_chunk(str(int(battle.loses)))} Loses ]"
          f"{Fore.WHITE+Style.BRIGHT} | "
          f"⚽️ {Fore.YELLOW+Style.BRIGHT}[ Winrate ] {battle.winrate:.2f}%")
    print(f"🍏 {Fore.GREEN+Style.BRIGHT}[ {split_chunk(str(int(battle.reward_wins)))} Wins Reward ]"
          f"{Fore.WHITE+Style.BRIGHT} | "
          f"🍎 {Fore.RED+Style.BRIGHT}[ {split_chunk(str(int(battle.reward_loses)))} Loses Reward ]"
          f"{Fore.WHITE+Style.BRIGHT} | "
          f"💰 {Fore.YELLOW+Style.BRIGHT}[ {split_chunk(str(int(battle.reward_wins + battle.reward_loses)))} Total Earned ]")
    user.claim()
    user.daily_rewards(auto_daily_rewards=config['auto_daily_rewards'])
    user.upgrade_pets(auto_upgrade_pets=config['auto_upgrade_pets'])
    
    current_date = datetime.now()
    if current_date.hour >= 23:
        await asyncio.sleep(3600)

    await battle.connect()
    del battle

if __name__ == '__main__':
    while True:
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            sys.exit(0)
        except Exception as e:
            print(f"🍓 {Fore.RED+Style.BRIGHT}[ {type(e).__name__} {e} ]")
        clear()