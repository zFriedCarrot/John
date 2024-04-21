import math
import re
import discord
from discord.ext import commands
import requests
import sqlite3
from dhooks import Webhook, Embed
import datetime
import time
import json

con = con = sqlite3.connect("alt-db.db")
cur = con.cursor()

prefixBot = '$'
intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix=f'{prefixBot}', intents=intents, status=discord.Status.online)
client.remove_command('help')



#=========================================================================================================#

@client.event
async def on_ready():
    # activity = discord.Activity(type=discord.ActivityType.watching, name=f"{prefixBot}help")
    activity = discord.Game(name="vapeV4")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('Success RaspPi!')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        msg = 'You dont have the facilities for that big man'
        await ctx.send(msg)
    elif isinstance(error, commands.MissingAnyRole):
        msg = 'You dont have the facilities for that big man'
        await ctx.send(msg)
    elif isinstance(error, commands.CommandNotFound):
        msg = f"That is not a valid command"
        await ctx.send(msg)
    elif isinstance(error, commands.CommandOnCooldown):
        msg = 'You are current on cooldown! Please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)

#=========================================================================================================#

def timeformat(raw_seconds):
    duration = ""
    raw_seconds = round(raw_seconds)
    if raw_seconds < 86400: days = 0
    else: days, raw_seconds = divmod(raw_seconds, 86400)

    if raw_seconds < 3600: hours = 0
    else: hours, raw_seconds = divmod(raw_seconds, 3600)

    if raw_seconds < 60: minutes = 0
    else: minutes, raw_seconds = divmod(raw_seconds, 60)

    seconds = raw_seconds

    if days != 0:
        duration += f"{round(days)} day"
        if days != 1: duration += "s"
        duration += ", "

    if hours != 0:
        duration += f"{round(hours)} hour"
        if hours != 1: duration += "s"
        duration += ", "

    if minutes != 0:
        duration += f"{round(minutes)} minute"
        if minutes != 1: duration += "s"

    if duration == "":
        duration += f"{round(seconds)} second"
        if seconds != 1: duration += "s"
        return duration

    if (hours == 0 and minutes == 0) or (days == 0 and minutes == 0): duration = duration[:-2]
    return duration

def title_check(wins: int) -> str:
    if wins >= 0 and wins <= 49:
        title = "None (Noob)"
    elif wins >= 50 and wins <= 59:
        title = "Rookie"
    elif wins >= 60 and wins <= 69:
        title = "Rookie II"
    elif wins >= 70 and wins <= 79:
        title = "Rookie III"
    elif wins >= 80 and wins <= 89:
        title = "Rookie IV"
    elif wins >= 90 and wins <= 99:
        title = "Rookie V"
    elif wins >= 100 and wins <= 129:
        title = "Iron"
    elif wins >= 130 and wins <= 159:
        title = "Iron II"
    elif wins >= 160 and wins <= 189:
        title = "Iron III"
    elif wins >= 190 and wins <= 219:
        title = "Iron IV"
    elif wins >= 220 and wins <= 249:
        title = "Iron V"
    elif wins >= 250 and wins <= 299:
        title = "Gold"
    elif wins >= 300 and wins <= 349:
        title = "Gold II"
    elif wins >= 350 and wins <= 399:
        title = "Gold III"
    elif wins >= 400 and wins <= 449:
        title = "Gold IV"
    elif wins >= 450 and wins <= 499:
        title = "Gold V"
    elif wins >= 500 and wins <= 599:
        title = "Diamond"
    elif wins >= 600 and wins <= 699:
        title = "Diamond II"
    elif wins >= 700 and wins <= 799:
        title = "Diamond III"
    elif wins >= 800 and wins <= 899:
        title = "Diamond IV"
    elif wins >= 900 and wins <= 999:
        title = "Diamond V"
    elif wins >= 1000 and wins <= 1199:
        title = "Master"
    elif wins >= 1200 and wins <= 1399:
        title = "Master II"
    elif wins >= 1400 and wins <= 1599:
        title = "Master III"
    elif wins >= 1600 and wins <= 1799:
        title = "Master IV"
    elif wins >= 1800 and wins <= 1999:
        title = "Master V"
    elif wins >= 2000 and wins <= 2599:
        title = "Legend"
    elif wins >= 2600 and wins <= 3199:
        title = "Legend II"
    elif wins >= 3200 and wins <= 3799:
        title = "Legend III"
    elif wins >= 3800 and wins <= 4399:
        title = "Legend IV"
    elif wins >= 4400 and wins <= 4999:
        title = "Legend V"
    elif wins >= 5000 and wins <= 5999:
        title = "Grandmaster"
    elif wins >= 6000 and wins <= 6999:
        title = "Grandmaster II"
    elif wins >= 7000 and wins <= 7999:
        title = "Grandmaster III"
    elif wins >= 8000 and wins <= 8999:
        title = "Grandmaster IV"
    elif wins >= 9000 and wins <= 9999:
        title = "Grandmaster V"
    elif wins >= 10000 and wins <= 12999:
        title = "Godlike"
    elif wins >= 13000 and wins <= 15999:
        title = "Godlike II"
    elif wins >= 16000 and wins <= 18999:
        title = "Godlike III"
    elif wins >= 19000 and wins <= 21999:
        title = "Godlike IV"
    elif wins >= 22000 and wins <= 24999:
        title = "Godlike V"
    elif wins >= 25000:
        title = "Wifeless"
    
    return title

def overallDuelsRankCheck(wins: int) -> str:
    if wins >= 0 and wins <= 99:
        title = "None (Noob)"
    elif wins >= 100 and wins <= 119:
        title = "Rookie"
    elif wins >= 120 and wins <= 139:
        title = "Rookie II"
    elif wins >= 140 and wins <= 159:
        title = "Rookie III"
    elif wins >= 160 and wins <= 179:
        title = "Rookie IV"
    elif wins >= 180 and wins <= 199:
        title = "Rookie V"
    elif wins >= 200 and wins <= 259:
        title = "Iron"
    elif wins >= 260 and wins <= 319:
        title = "Iron II"
    elif wins >= 320 and wins <= 379:
        title = "Iron III"
    elif wins >= 380 and wins <= 439:
        title = "Iron IV"
    elif wins >= 440 and wins <= 499:
        title = "Iron V"
    elif wins >= 500 and wins <= 599:
        title = "Gold"
    elif wins >= 600 and wins <= 699:
        title = "Gold II"
    elif wins >= 700 and wins <= 799:
        title = "Gold III"
    elif wins >= 800 and wins <= 899:
        title = "Gold IV"
    elif wins >= 900 and wins <= 999:
        title = "Gold V"
    elif wins >= 1000 and wins <= 1199:
        title = "Diamond"
    elif wins >= 1200 and wins <= 1399:
        title = "Diamond II"
    elif wins >= 1400 and wins <= 1599:
        title = "Diamond III"
    elif wins >= 1600 and wins <= 1799:
        title = "Diamond IV"
    elif wins >= 1800 and wins <= 1999:
        title = "Diamond V"
    elif wins >= 2000 and wins <= 2399:
        title = "Master"
    elif wins >= 2400 and wins <= 2799:
        title = "Master II"
    elif wins >= 2800 and wins <= 3199:
        title = "Master III"
    elif wins >= 3200 and wins <= 3599:
        title = "Master IV"
    elif wins >= 3600 and wins <= 3999:
        title = "Master V"
    elif wins >= 4000 and wins <= 5199:
        title = "Legend"
    elif wins >= 5200 and wins <= 6399:
        title = "Legend II"
    elif wins >= 6400 and wins <= 7599:
        title = "Legend III"
    elif wins >= 7600 and wins <= 8799:
        title = "Legend IV"
    elif wins >= 8800 and wins <= 9999:
        title = "Legend V"
    elif wins >= 10000 and wins <= 11999:
        title = "Grandmaster"
    elif wins >= 12000 and wins <= 13999:
        title = "Grandmaster II"
    elif wins >= 14000 and wins <= 15999:
        title = "Grandmaster III"
    elif wins >= 16000 and wins <= 17999:
        title = "Grandmaster IV"
    elif wins >= 18000 and wins <= 19999:
        title = "Grandmaster V"
    elif wins >= 200000 and wins <= 25999:
        title = "Godlike"
    elif wins >= 26000 and wins <= 31999:
        title = "Godlike II"
    elif wins >= 32000 and wins <= 37999:
        title = "Godlike III"
    elif wins >= 38000 and wins <= 43999:
        title = "Godlike IV"
    elif wins >= 44000 and wins <= 49999:
        title = "Godlike V"
    elif wins >= 50000:
        title = "Wifeless"
    
    return title
    
def titleColorBridge(wins: int) -> hex:
    if wins >= 0 and wins <= 49:
        color = 0x4b4949
    elif wins >= 50 and wins <= 99:
        color = 0x4b4949
    elif wins >= 100 and wins <= 249:
        color = 0xf1f1f1
    elif wins >= 250 and wins <= 499:
        color = 0xc29a02
    elif wins >= 500 and wins <= 999:
        color = 0x1192d1
    elif wins >= 1000 and wins <= 1999:
        color = 0x087e16
    elif wins >= 2000 and wins <= 4999:
        color = 0xa80905
    elif wins >= 4999 and wins <= 9999:
        color = 0xeef54d
    elif wins >= 10000 and wins <= 24999:
        color = 0x880173
    elif wins >= 25000:
        color = 0x00ddff
    
    return color

def overallTitleColor(wins: int) -> hex:
    if wins >= 0 and wins <= 99:
        color = 0x4b4949
    elif wins >= 100 and wins <= 199:
        color = 0x4b4949
    elif wins >= 200 and wins <= 499:
        color = 0xf1f1f1
    elif wins >= 500 and wins <= 999:
        color = 0xc29a02
    elif wins >= 1000 and wins <= 1999:
        color = 0x1192d1
    elif wins >= 2000 and wins <= 3999:
        color = 0x087e16
    elif wins >= 4000 and wins <= 9999:
        color = 0xa80905
    elif wins >= 10000 and wins <= 19999:
        color = 0xeef54d
    elif wins >= 20000 and wins <= 49999:
        color = 0x880173
    elif wins >= 50000:
        color = 0x00ddff
    
    return color

def nextRankCheck(wins: int):
    if wins >= 0 and wins <= 49:
        if wins > 0:
            title = 50-wins
        else:
            title = "First get a division"
    elif wins >= 50 and wins <= 59:
        title = f"{60-wins} Wins until next rank"
    elif wins >= 60 and wins <= 69:
        title = f"{70-wins} Wins until next rank"
    elif wins >= 70 and wins <= 79:
        title = f"{80-wins} Wins until next rank"
    elif wins >= 80 and wins <= 89:
        title = f"{90-wins} Wins until next rank"
    elif wins >= 90 and wins <= 99:
        title = f"{100-wins} Wins until next rank"
    elif wins >= 100 and wins <= 129:
        title = f"{130-wins} Wins until next rank"
    elif wins >= 130 and wins <= 159:
        title = f"{160-wins} Wins until next rank"
    elif wins >= 160 and wins <= 189:
        title = f"{190-wins} Wins until next rank"
    elif wins >= 190 and wins <= 219:
        title = f"{220-wins} Wins until next rank"
    elif wins >= 220 and wins <= 249:
        title = f"{250-wins} Wins until next rank"
    elif wins >= 250 and wins <= 299:
        title = f"{300-wins} Wins until next rank"
    elif wins >= 300 and wins <= 349:
        title = f"{350-wins} Wins until next rank"
    elif wins >= 350 and wins <= 399:
        title = f"{400-wins} Wins until next rank"
    elif wins >= 400 and wins <= 449:
        title = f"{450-wins} Wins until next rank"
    elif wins >= 450 and wins <= 499:
        title = f"{500-wins} Wins until next rank"
    elif wins >= 500 and wins <= 599:
        title = f"{600-wins} Wins until next rank"
    elif wins >= 600 and wins <= 699:
        title = f"{700-wins} Wins until next rank"
    elif wins >= 700 and wins <= 799:
        title = f"{800-wins} Wins until next rank"
    elif wins >= 800 and wins <= 899:
        title = f"{900-wins} Wins until next rank"
    elif wins >= 900 and wins <= 999:
        title = f"{1000-wins} Wins until next rank"
    elif wins >= 1000 and wins <= 1199:
        title = f"{1200-wins} Wins until next rank"
    elif wins >= 1200 and wins <= 1399:
        title = f"{1400-wins} Wins until next rank"
    elif wins >= 1400 and wins <= 1599:
        title = f"{1600-wins} Wins until next rank"
    elif wins >= 1600 and wins <= 1799:
        title = f"{1800-wins} Wins until next rank"
    elif wins >= 1800 and wins <= 1999:
        title = f"{2000-wins} Wins until next rank"
    elif wins >= 2000 and wins <= 2599:
        title = f"{2600-wins} Wins until next rank"
    elif wins >= 2600 and wins <= 3199:
        title = f"{3200-wins} Wins until next rank"
    elif wins >= 3200 and wins <= 3799:
        title = f"{3800-wins} Wins until next rank"
    elif wins >= 3800 and wins <= 4399:
        title = f"{4400-wins} Wins until next rank"
    elif wins >= 4400 and wins <= 4999:
        title = f"{5000-wins} Wins until next rank"
    elif wins >= 5000 and wins <= 5999:
        title = f"{6000-wins} Wins until next rank"
    elif wins >= 6000 and wins <= 6999:
        title = f"{7000-wins} Wins until next rank"
    elif wins >= 7000 and wins <= 7999:
        title = f"{8000-wins} Wins until next rank"
    elif wins >= 8000 and wins <= 8999:
        title = f"{9000-wins} Wins until next rank"
    elif wins >= 9000 and wins <= 9999:
        title = f"{10000-wins} Wins until next rank"
    elif wins >= 10000 and wins <= 12999:
        title = f"{13000-wins} Wins until next rank"
    elif wins >= 13000 and wins <= 15999:
        title = f"{16000-wins} Wins until next rank"
    elif wins >= 16000 and wins <= 18999:
        title = f"{19000-wins} Wins until next rank"
    elif wins >= 19000 and wins <= 21999:
        title = f"{22000-wins} Wins until next rank"
    elif wins >= 22000 and wins <= 24999:
        title = f"{25000-wins} Wins until next rank"
    elif wins >= 25000:
        title = "Just quit <3"
    
    return title

def rankCheck(data) -> str:
    if "newPackageRank" not in data["player"]:
        rank = "No Rank"
    elif data["player"]["newPackageRank"] == "VIP":
        rank = "VIP"
    elif data["player"]["newPackageRank"] == "VIP_PLUS":
        rank = "VIP+"
    elif data["player"]["newPackageRank"] == "MVP":
        rank = "MVP"
    elif 'monthlyPackageRank' in data['player']:
        if data['player']['monthlyPackageRank'] == 'SUPERSTAR':
            rank = "MVP++"
        else:
            rank = "MVP+"
    else:
        rank = "MVP+"
    
    return rank 

def is_integer_only(sample_str):
    result = re.match("[-+]?\d+$", sample_str)
    return result

def bridgeGameCheck(mode):
    if mode == "DUELS_BRIDGE_DUEL":
        gameMode = "Bridge Solo"
    elif mode == "DUELS_BRIDGE_DOUBLES":
        gameMode = "Bridge Doubles"
    elif mode == "DUELS_BRIDGE_THREES":
        gameMode = "Bridge Threes"
    elif mode == "DUELS_BRIDGE_FOUR":
        gameMode = "Bridge Fours"
    elif mode == "DUELS_BRIDGE_2V2V2V2":
        gameMode = "Bridge 2v2v2v2"
    elif mode == "DUELS_BRIDGE_3V3V3V3":
        gameMode = "Bridge 3v3v3v3"
    elif mode == "DUELS_CAPTURE_THREES":
        gameMode = "CTF"
    else:
        gameMode = ""    
    return gameMode

def linkingIgn(ctx) -> str:
    cur.execute(f"SELECT discordId FROM linking WHERE discordId = '{ctx.message.author.id}';")
    userCheck = cur.fetchone()
    if userCheck is not None:
        username = cur.execute(f"SELECT uuid FROM linking WHERE discordId = '{ctx.message.author.id}';")
        username = f"{cur.fetchone()}"
        username = username.split("'")[1]
        uuid = username.split("'")[0]
    else: 
        pass
    return uuid

def playerCheck(ign) -> str:
    if ign != "":
            usercheck = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}')
            if usercheck.status_code == 404:
                IsItaPlayer = True
            else:
                usercheck = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}').json()
                uuid = usercheck['id']
    else:
        pass
    return uuid

#=========================================================================================================#

@client.command()
async def apikey(ctx):
    if ctx.message.author.id == 677804130726576138 or ctx.message.author.id == 910505502113398824:
        await ctx.send('Please check your DM')
        await ctx.author.send("Please paste your new api key. You have 60 seconds")

        def check(message):
            return message.author == ctx.author
        
        try:
            newApiKeyMsg = await client.wait_for('message', check=check, timeout=60)
            newApiKey = newApiKeyMsg.content
            
            with open('data.json', 'r') as file:
                data = json.load(file)

            data['hypixelKeyJson'] = f"{newApiKey}"

            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)

            await ctx.author.send(f'Api key changed to "{newApiKey}"')
        except:
            await ctx.author.send("Password change request timed out.")
    else:
        await ctx.send('No permission')

#=========================================================================================================#


@client.command()
async def help(ctx):
    linking = f"`{prefixBot}link [IGN]` \nLink your mc account"
    unlinking = f"`{prefixBot}unlink` \nUnlinks your account"
    duels = f"`{prefixBot}d/duels [IGN]` \nShows duels stats of player"
    bridge = f"`{prefixBot}b/bridge [IGN]` \nShows bridge stats of player"
    bedwars = f"`{prefixBot}bw/bedwars [IGN]` \nShows bedwars stats of player"
    track = f"`{prefixBot}track [IGN]` \nshows online/offline stats of player"
    discordCheck = f"`{prefixBot}dc/discord [IGN]` \nShows discord of player"
    skin = f"`{prefixBot}sk/skin [IGN]` \nShows skin of player"
    help_em = discord.Embed(title="Help Menu", description=f"`Prefix = [{prefixBot}]`", color=0xffffff)
    help_em.add_field(name="Commands", value=f"{linking} \n\n{unlinking} \n\n{duels} \n\n{bridge} \n\n{bedwars} \n\n{track} \n\n{discordCheck} \n\n{skin}", inline=True)
    await ctx.send(embed=help_em)

@client.command(pass_context=True)
@commands.has_guild_permissions(administrator=True)
async def purge(ctx, amount=0):
    if amount == 0:
        errorem = discord.Embed(title="Error", description="Eneter a valid amount", color=0xff0000)
        await ctx.send(embed=errorem)
    else:
        amount = amount + 1
        await ctx.channel.purge(limit=amount)

@client.command(name = "avatarCheck", aliases = ['av', 'avatar'])
async def avatarCheck(ctx, *, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar_url
    avatarEmbed = discord.Embed(title=f"The avatar of, {member}", description=f"", color=0xffffff)
    avatarEmbed.set_footer(text=f'Requested by {ctx.message.author}')
    avatarEmbed.set_image(url=userAvatar)
    await ctx.send(embed=avatarEmbed)

#=========================================================================================================#

@client.command(name = "playerStatus", aliases= ['track', 'status'])
async def playerStatus(ctx, ign=""):
    if ign == "":
        error_em = discord.Embed(title=f"Enter a valid ign", description="", color=0xff0000)
        await ctx.send(embed=error_em)
    else:
            data = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}')
            if data.status_code == 404:
                nplayerem = discord.Embed(title=f"`{ign}` is not a player", description="", color=0xff0000)
                await ctx.send(embed=nplayerem)
            else:
                try:
                    with open('data.json', 'r') as file:
                        dataJson = json.load(file)

                    hypixelKeyJson = dataJson['hypixelKeyJson']
                    
                    namedata = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}').json()
                    uuid = namedata['id']
                    name = namedata["name"]
                    status = requests.get(f'https://api.hypixel.net/status?key={hypixelKeyJson}&uuid={uuid}').json()
                    logindata = requests.get(f'https://api.hypixel.net/player?key={hypixelKeyJson}&uuid={uuid}').json()
                    if "online" in status["session"]:
                        if status["session"]["online"]:
                            if 'mode' in status["session"]:
                                online = ''.join(f"GameType - `{status['session']['gameType']}`")
                                online = ''.join(f"{online} \n{name} is playing - `{status['session']['mode']}`")
                                if 'map' in status["session"]:
                                    online = ''.join(f"{online} \nCurrent Map - `{status['session']['map']}`")
                            if "lastLogin" in logindata["player"]:
                                lastLogout = logindata["player"]["lastLogout"] / 1000
                                lastLogin = logindata["player"]["lastLogin"] / 1000
                                embed = discord.Embed(title=f"{name} is online", description=f"{name} has been online for `{timeformat(time.time() - lastLogin)}` \n\n{online}\n", color=0x02ff00)
                                embed.set_footer(text=f'Requested by {ctx.message.author}')
                                await ctx.send(embed=embed)
                        else:
                            lastlogindata = requests.get(f'https://api.hypixel.net/player?key={hypixelKeyJson}&uuid={uuid}').json()
                            if "lastLogin" not in lastlogindata["player"]:
                                offline_em = discord.Embed(title=f"Error", description=f'**{name} has their API OFF**', color=0xff0000)
                                offline_em.set_thumbnail(url=f"{fullSkin}")
                                offline_em.set_footer(text=f'Requested by {ctx.message.author}')
                                await ctx.send(embed=offline_em) 
                            else:
                                data = requests.get(f'https://api.hypixel.net/player?key={hypixelKeyJson}&uuid={uuid}').json()
                                lastLogout = data["player"]["lastLogout"] / 1000
                                lastLogin = data["player"]["lastLogin"] / 1000
                                embedtrack = discord.Embed(title=f"{name}, is offline", description=f"{name} was last online `{timeformat(time.time() - lastLogout)}` ago \nTheir last session lasted `{timeformat(lastLogout - lastLogin)}`", color=0xff0000)
                                embedtrack.set_footer(text=f'Requested by {ctx.message.author}')
                                await ctx.send(embed=embedtrack)
                    else:
                        ctx.send("API off")
                except:
                    namedata = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}').json()
                    name = namedata["name"]
                    await ctx.send(f"{name}, never joined hypixel")

@client.command(name="bridgeStats", aliases=['b', 'bridge'])
async def bridgeStats(ctx, ign=""):
    IsItaPlayer = False
    uuid = ""

    if ign == "":
        cur.execute(f"SELECT discordId FROM linking WHERE discordId = '{ctx.message.author.id}';")
        userCheck = cur.fetchone()
        if userCheck is not None:
            username = cur.execute(f"SELECT uuid FROM linking WHERE discordId = '{ctx.message.author.id}';")
            username = f"{cur.fetchone()}"
            username = username.split("'")[1]
            uuid = username.split("'")[0]

    if uuid == "":
        if ign != "":
            usercheck = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}')
            if usercheck.status_code == 404:
                IsItaPlayer = True
            else:
                usercheck = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}').json()
                uuid = usercheck['id']
        else:
            pass
        
    if uuid != "":
            
            with open('data.json', 'r') as file:
                dataJson = json.load(file)

            hypixelKeyJson = dataJson['hypixelKeyJson']

            uuiddata = requests.get(f'https://sessionserver.mojang.com/session/minecraft/profile/{uuid}').json()
            uuid = uuiddata["id"]
            bridge_data = requests.get(f'https://api.hypixel.net/player?key={hypixelKeyJson}&uuid={uuid}').json()
            name = uuiddata["name"]
            if bridge_data['player'] != None:
                if "stats" in bridge_data["player"]:
                    if "Duels" in bridge_data["player"]["stats"]:
                        if "networkExp" in bridge_data["player"]:
                            network_experience = bridge_data["player"]["networkExp"]
                            network_level = (math.sqrt((2 * network_experience) + 30625) / 50) - 2.5
                            network_level = round(network_level)
                        bridgeDuels = bridge_data["player"]["stats"]["Duels"]
                        if "bridge_duel_wins" in bridgeDuels:
                            duelsWins = int(bridgeDuels["bridge_duel_wins"])
                        else:
                            duelsWins = 0
                        if "bridge_doubles_wins" in bridgeDuels:
                            doublesWins = int(bridgeDuels["bridge_doubles_wins"])
                        else:
                            doublesWins = 0
                        if "bridge_threes_wins" in bridgeDuels:
                            threesWins = int(bridgeDuels["bridge_threes_wins"])
                        else:
                            threesWins = 0
                        if "bridge_four_wins" in bridgeDuels:
                            foursWins = int(bridgeDuels["bridge_four_wins"])
                        else:
                            foursWins = 0
                        if "capture_threes_wins" in bridgeDuels:
                            captureWins = int(bridgeDuels["capture_threes_wins"])
                        else:
                            captureWins = 0
                        if "bridge_2v2v2v2_wins" in bridgeDuels:
                            fourTwoWins = int(bridgeDuels["bridge_2v2v2v2_wins"])
                        else:
                            fourTwoWins = 0
                        if "bridge_3v3v3v3_wins" in bridgeDuels:
                            fourThreesWins = int(bridgeDuels["bridge_3v3v3v3_wins"])
                        else:
                            fourThreesWins = 0
                        
                        if "bridge_duel_losses" in bridgeDuels:
                            duelsLosses = int(bridgeDuels["bridge_duel_losses"])
                        else:
                            duelsLosses = 0
                        if "bridge_doubles_losses" in bridgeDuels:
                            doublesLosses = int(bridgeDuels["bridge_doubles_losses"])
                        else:
                            doublesLosses = 0
                        if "bridge_threes_losses" in bridgeDuels:
                            threesLosses = int(bridgeDuels["bridge_threes_losses"])
                        else:
                            threesLosses = 0
                        if "bridge_four_losses" in bridgeDuels:
                            foursLosses = int(bridgeDuels["bridge_four_losses"])
                        else:
                            foursLosses = 0
                        if "capture_threes_losses" in bridgeDuels:
                            captureLosses = int(bridgeDuels["capture_threes_losses"])
                        else:
                            captureLosses = 0
                        if "bridge_2v2v2v2_losses" in bridgeDuels:
                            fourTwoLosses = int(bridgeDuels["bridge_2v2v2v2_losses"])
                        else:
                            fourTwoLosses = 0
                        if "bridge_3v3v3v3_losses" in bridgeDuels:
                            fourThreeLosses = int(bridgeDuels["bridge_3v3v3v3_losses"])
                        else:
                            fourThreeLosses = 0

                        total = 0
                        overallGoals = 0
                        overallKills = 0
                        overallDeaths = 0
                        sololGoals = 0
                        sololKills = 0
                        soloDeaths = 0
                        doublesGoals = 0
                        doublesKills = 0
                        doubesDeaths = 0
                        threesGoals = 0
                        threesKills = 0
                        threesDeaths = 0
                        foursGoals = 0
                        foursKills = 0
                        foursDeaths = 0
                        fourTwoGoals = 0
                        fourTwoKills = 0
                        fourTwoDeaths = 0
                        fourThreeGoals = 0
                        fourThreeKills = 0
                        fourThreeDeaths = 0
                        ctfGoals = 0
                        ctfKills = 0
                        ctfDeaths = 0

                        if "goals" in bridge_data["player"]["stats"]["Duels"]:
                            overallGoals = bridge_data["player"]["stats"]["Duels"]["goals"]
                        if "bridge_kills" in bridge_data["player"]["stats"]["Duels"]:
                            overallKills = bridge_data["player"]["stats"]["Duels"]["bridge_kills"]
                        if "bridge_deaths" in bridge_data["player"]["stats"]["Duels"]:
                            overallDeaths = bridge_data["player"]["stats"]["Duels"]["bridge_deaths"]
                        
                        if "bridge_duel_goals" in bridge_data["player"]["stats"]["Duels"]:
                            sololGoals = bridge_data["player"]["stats"]["Duels"]["bridge_duel_goals"]
                        if "bridge_duel_bridge_kills" in bridge_data["player"]["stats"]["Duels"]:
                            sololKills = bridge_data["player"]["stats"]["Duels"]["bridge_duel_bridge_kills"]
                        if "bridge_duel_bridge_deaths" in bridge_data["player"]["stats"]["Duels"]:
                            soloDeaths = bridge_data["player"]["stats"]["Duels"]["bridge_duel_bridge_deaths"]
                        
                        if "bridge_doubles_goals" in bridge_data["player"]["stats"]["Duels"]:
                            doublesGoals = bridge_data["player"]["stats"]["Duels"]["bridge_doubles_goals"]
                        if "bridge_doubles_bridge_kills" in bridge_data["player"]["stats"]["Duels"]:
                            doublesKills = bridge_data["player"]["stats"]["Duels"]["bridge_doubles_bridge_kills"]
                        if "bridge_doubles_bridge_deaths" in bridge_data["player"]["stats"]["Duels"]:
                            doubesDeaths = bridge_data["player"]["stats"]["Duels"]["bridge_doubles_bridge_deaths"]
                        
                        if "bridge_threes_goals" in bridge_data["player"]["stats"]["Duels"]:
                            threesGoals = bridge_data["player"]["stats"]["Duels"]["bridge_threes_goals"]
                        if "bridge_threes_bridge_kills" in bridge_data["player"]["stats"]["Duels"]:
                            threesKills = bridge_data["player"]["stats"]["Duels"]["bridge_threes_bridge_kills"]
                        if "bridge_threes_bridge_deaths" in bridge_data["player"]["stats"]["Duels"]:
                            threesDeaths = bridge_data["player"]["stats"]["Duels"]["bridge_threes_bridge_deaths"]
                        
                        if "bridge_four_goals" in bridge_data["player"]["stats"]["Duels"]:
                            foursGoals = bridge_data["player"]["stats"]["Duels"]["bridge_four_goals"]
                        if "bridge_four_bridge_kills" in bridge_data["player"]["stats"]["Duels"]:
                            foursKills = bridge_data["player"]["stats"]["Duels"]["bridge_four_bridge_kills"]
                        if "bridge_four_bridge_deaths" in bridge_data["player"]["stats"]["Duels"]:
                            foursDeaths = bridge_data["player"]["stats"]["Duels"]["bridge_four_bridge_deaths"]
                        
                        if "bridge_2v2v2v2_goals" in bridge_data["player"]["stats"]["Duels"]:
                            fourTwoGoals = bridge_data["player"]["stats"]["Duels"]["bridge_2v2v2v2_goals"]
                        if "bridge_2v2v2v2_bridge_kills" in bridge_data["player"]["stats"]["Duels"]:
                            fourTwoKills = bridge_data["player"]["stats"]["Duels"]["bridge_2v2v2v2_bridge_kills"]
                        if "bridge_2v2v2v2_bridge_deaths" in bridge_data["player"]["stats"]["Duels"]:
                            fourTwoDeaths = bridge_data["player"]["stats"]["Duels"]["bridge_2v2v2v2_bridge_deaths"]

                        if "bridge_3v3v3v3_goals" in bridge_data["player"]["stats"]["Duels"]:
                            fourThreeGoals = bridge_data["player"]["stats"]["Duels"]["bridge_3v3v3v3_goals"]
                        if "bridge_3v3v3v3_bridge_kills" in bridge_data["player"]["stats"]["Duels"]:
                            fourThreeKills = bridge_data["player"]["stats"]["Duels"]["bridge_3v3v3v3_bridge_kills"]
                        if "bridge_3v3v3v3_bridge_deaths" in bridge_data["player"]["stats"]["Duels"]:
                            fourThreeDeaths = bridge_data["player"]["stats"]["Duels"]["bridge_3v3v3v3_bridge_deaths"]

                        if "captures" in bridge_data["player"]["stats"]["Duels"]:
                            ctfGoals = bridge_data["player"]["stats"]["Duels"]["captures"]
                        if "capture_threes_bridge_kills" in bridge_data["player"]["stats"]["Duels"]:
                            ctfKills = bridge_data["player"]["stats"]["Duels"]["capture_threes_bridge_kills"]
                        if "capture_threes_bridge_deaths" in bridge_data["player"]["stats"]["Duels"]:
                            ctfDeaths = bridge_data["player"]["stats"]["Duels"]["capture_threes_bridge_deaths"]
                        
                        if "current_bridge_winstreak" in bridge_data["player"]["stats"]["Duels"]:
                            overallWinstreak = bridge_data["player"]["stats"]["Duels"]["current_bridge_winstreak"]
                        else:
                            overallWinstreak = 0
                        
                        if "current_winstreak_mode_bridge_duel" in bridge_data["player"]["stats"]["Duels"]:
                            soloWinstreak = bridge_data["player"]["stats"]["Duels"]["current_winstreak_mode_bridge_duel"]
                        else:
                            soloWinstreak = 0

                        if "current_winstreak_mode_bridge_doubles" in bridge_data["player"]["stats"]["Duels"]:
                            doublesWinstreak = bridge_data["player"]["stats"]["Duels"]["current_winstreak_mode_bridge_doubles"]
                        else:
                            doublesWinstreak = 0

                        if "current_winstreak_mode_bridge_threes" in bridge_data["player"]["stats"]["Duels"]:
                            threesWinstreak = bridge_data["player"]["stats"]["Duels"]["current_winstreak_mode_bridge_threes"]
                        else:
                            threesWinstreak = 0

                        if "current_winstreak_mode_bridge_four" in bridge_data["player"]["stats"]["Duels"]:
                            foursWinstreak = bridge_data["player"]["stats"]["Duels"]["current_winstreak_mode_bridge_four"]
                        else:
                            foursWinstreak = 0

                        if "current_winstreak_mode_bridge_2v2v2v2" in bridge_data["player"]["stats"]["Duels"]:
                            fourTwoWinstreak = bridge_data["player"]["stats"]["Duels"]["current_winstreak_mode_bridge_2v2v2v2"]
                        else:
                            fourTwoWinstreak = 0

                        if "current_winstreak_mode_bridge_3v3v3v3" in bridge_data["player"]["stats"]["Duels"]:
                            fourThreeWinstreak = bridge_data["player"]["stats"]["Duels"]["current_winstreak_mode_bridge_3v3v3v3"]
                        else:
                            fourThreeWinstreak = 0

                        if "current_winstreak_mode_bridge_capture" in bridge_data["player"]["stats"]["Duels"]:
                            ctfWinstreak = bridge_data["player"]["stats"]["Duels"]["current_winstreak_mode_bridge_capture"]
                        else:
                            ctfWinstreak = 0

                        if "best_bridge_winstreak" in bridge_data["player"]["stats"]["Duels"]:
                            overallBestWinstreak = bridge_data["player"]["stats"]["Duels"]["best_bridge_winstreak"]
                        else:
                            overallBestWinstreak = 0

                        if "best_winstreak_mode_bridge_duel" in bridge_data["player"]["stats"]["Duels"]:
                            soloBestWinstreak = bridge_data["player"]["stats"]["Duels"]["best_winstreak_mode_bridge_duel"]
                        else:
                            soloBestWinstreak = 0

                        if "best_winstreak_mode_bridge_doubles" in bridge_data["player"]["stats"]["Duels"]:
                            doublesBestWinstreak = bridge_data["player"]["stats"]["Duels"]["best_winstreak_mode_bridge_doubles"]
                        else:
                            doublesBestWinstreak = 0

                        if "best_winstreak_mode_bridge_threes" in bridge_data["player"]["stats"]["Duels"]:
                            threesBestWinstreak = bridge_data["player"]["stats"]["Duels"]["best_winstreak_mode_bridge_threes"]
                        else:
                            threesBestWinstreak = 0

                        if "best_winstreak_mode_bridge_four" in bridge_data["player"]["stats"]["Duels"]:
                            foursBestWinstreak = bridge_data["player"]["stats"]["Duels"]["best_winstreak_mode_bridge_four"]
                        else:
                            foursBestWinstreak = 0

                        if "best_winstreak_mode_bridge_2v2v2v2" in bridge_data["player"]["stats"]["Duels"]:
                            fourTwoBestWinstreak = bridge_data["player"]["stats"]["Duels"]["best_winstreak_mode_bridge_2v2v2v2"]
                        else:
                            fourTwoBestWinstreak = 0

                        if "best_winstreak_mode_bridge_3v3v3v3" in bridge_data["player"]["stats"]["Duels"]:
                            fourThreeBestwinstreak = bridge_data["player"]["stats"]["Duels"]["best_winstreak_mode_bridge_3v3v3v3"]
                        else:
                            fourThreeBestwinstreak = 0

                        if "best_winstreak_mode_capture_threes" in bridge_data["player"]["stats"]["Duels"]:
                            ctfBestWinstreak = bridge_data["player"]["stats"]["Duels"]["best_winstreak_mode_capture_threes"]
                        else:
                            ctfBestWinstreak = 0
                        
                        if fourTwoWins or fourThreesWins > 0:
                            total = fourTwoWins + fourThreesWins

                        rankCheckData = requests.get(f'https://api.hypixel.net/player?key={hypixelKeyJson}&uuid={uuid}').json()
                        overallWins = duelsWins + doublesWins + threesWins + foursWins + captureWins + fourTwoWins + fourThreesWins
                        overallLosses = duelsLosses + doublesLosses + threesLosses + foursLosses + captureLosses + fourTwoLosses + fourThreeLosses
                        title = title_check(overallWins)
                        title_color = titleColorBridge(overallWins)
                        rank = rankCheck(rankCheckData)
                        nextRank = nextRankCheck(overallWins)
                        fullSkin = (f"https://visage.surgeplay.com/full/{uuid}?y=-30")

                        if overallLosses != 0:
                            overallWlr = round(overallWins/overallLosses, 2)
                        else:
                            overallWlr = overallWins
                        if overallDeaths != 0:
                            overallKd = round(overallKills/overallDeaths, 2)
                        else:
                            overallKd = overallKills
                        
                        if duelsLosses != 0:
                            soloWlr = round(duelsWins/duelsLosses, 2)
                        else:
                            soloWlr = duelsWins
                        if soloDeaths != 0:
                            soloKd = round(sololKills/soloDeaths, 2)
                        else:
                            soloKd = sololKills
                        
                        if doublesLosses != 0:
                            doublesWlr = round(doublesWins/doublesLosses, 2)
                        else:
                            doublesWlr = doublesWins
                        if doubesDeaths != 0:
                            doublesKd = round(doublesKills/doubesDeaths, 2)
                        else:
                            doublesKd = doublesKills
                            
                        if threesLosses != 0:
                            threesWlr = round(threesWins/threesLosses, 2)
                        else:
                            threesWlr = threesWins
                        if threesDeaths != 0:
                            threesKd = round(threesKills/threesDeaths, 2)
                        else:
                            threesKd = threesKills
                        
                        if foursLosses != 0:
                            foursWlr = round(foursWins/foursLosses, 2)
                        else:
                            foursWlr = foursWins
                        if foursDeaths != 0:
                            foursKd = round(foursKills/foursDeaths, 2)
                        else:
                            foursKd = foursKills

                        if fourTwoLosses != 0:
                            fourTwoWlr = round(fourTwoWins/fourTwoLosses, 2)
                        else:
                            fourTwoWlr = fourTwoWins
                        if fourTwoDeaths != 0:
                            fourTwpKd = round(fourTwoKills/fourTwoDeaths, 2)
                        else:
                            fourTwpKd = fourTwoKills
                            
                        if fourThreeLosses != 0:
                            fourThreeWlr = round(fourThreesWins/fourThreeLosses, 2)
                        else:
                            fourThreeWlr = fourThreesWins
                        if fourThreeDeaths != 0:
                            fourThreeKd = round(fourThreeKills/fourThreeDeaths, 2)
                        else:
                            fourThreeKd = fourThreeKills
                            
                        if captureLosses != 0:
                            ctfWlr = round(captureWins/captureLosses, 2)
                        else:
                            ctfWlr = captureWins
                        if ctfDeaths != 0:
                            ctfKd = round(ctfKills/ctfDeaths, 2)
                        else:
                            ctfKd = ctfKills
                        
                        overallBestWinstreak = "{:,}".format(overallBestWinstreak)
                        soloBestWinstreak = "{:,}".format(soloBestWinstreak)
                        doublesBestWinstreak = "{:,}".format(doublesBestWinstreak)
                        threesBestWinstreak = "{:,}".format(threesBestWinstreak)
                        foursBestWinstreak = "{:,}".format(foursBestWinstreak)
                        fourTwoBestWinstreak = "{:,}".format(fourTwoBestWinstreak)
                        fourThreeBestwinstreak = "{:,}".format(fourThreeBestwinstreak)
                        ctfBestWinstreak = "{:,}".format(ctfBestWinstreak)

                        overallWinstreak = "{:,}".format(overallWinstreak)
                        soloWinstreak = "{:,}".format(soloWinstreak)
                        doublesWinstreak = "{:,}".format(doublesWinstreak)
                        threesWinstreak = "{:,}".format(threesWinstreak)
                        foursWinstreak = "{:,}".format(foursWinstreak)
                        fourTwoWinstreak = "{:,}".format(fourTwoWinstreak)
                        fourThreeWinstreak = "{:,}".format(fourThreeWinstreak)
                        ctfWinstreak = "{:,}".format(ctfWinstreak)

                        overallWins = "{:,}".format(overallWins)
                        duelsWins = "{:,}".format(duelsWins)
                        doublesWins = "{:,}".format(doublesWins)
                        threesWins = "{:,}".format(threesWins)
                        foursWins = "{:,}".format(foursWins)
                        fourTwoWins = "{:,}".format(fourTwoWins)
                        fourThreesWins = "{:,}".format(fourThreesWins)
                        captureWins = "{:,}".format(captureWins)

                        overallLosses = "{:,}".format(overallLosses)
                        duelsLosses = "{:,}".format(duelsLosses)
                        doublesLosses = "{:,}".format(doublesLosses)
                        threesLosses = "{:,}".format(threesLosses)
                        foursLosses = "{:,}".format(foursLosses)
                        fourTwoLosses = "{:,}".format(fourTwoLosses)
                        fourThreeLosses = "{:,}".format(fourThreeLosses)
                        captureLosses = "{:,}".format(captureLosses)

                        overallKills = "{:,}".format(overallKills)
                        sololKills = "{:,}".format(sololKills)
                        doublesKills = "{:,}".format(doublesKills)
                        threesKills = "{:,}".format(threesKills)
                        foursKills = "{:,}".format(foursKills)
                        fourTwoKills = "{:,}".format(fourTwoKills)
                        fourThreeKills = "{:,}".format(fourThreeKills)
                        ctfKills = "{:,}".format(ctfKills)

                        overallGoals = "{:,}".format(overallGoals)
                        sololGoals = "{:,}".format(sololGoals)
                        doublesGoals = "{:,}".format(doublesGoals)
                        threesGoals = "{:,}".format(threesGoals)
                        foursGoals = "{:,}".format(foursGoals)
                        fourTwoGoals = "{:,}".format(fourTwoGoals)
                        fourThreeGoals = "{:,}".format(fourThreeGoals)
                        ctfGoals = "{:,}".format(ctfGoals)

                        total = "{:,}".format(total)

                        statusCheck = requests.get(f"https://api.hypixel.net/status?key={hypixelKeyJson}&uuid={uuid}").json()
                        
                        gamemodeCheck = False
                        online = False
                        apiOnOff = False
                        
                        if statusCheck["session"]["online"]:
                            online = True
                            if "mode" in statusCheck["session"]:
                                bridgeGame = bridgeGameCheck(statusCheck["session"]["mode"])
                                if bridgeGame != "":
                                    gamemodeCheck = True
                        else:
                            if "lastLogin" in bridge_data["player"]:
                                apiOnOff = True
                
                        overallStats = f"`•`Best WS - `{overallBestWinstreak}` \n`•`Winstreak - `{overallWinstreak}` \n`•`Wins - `{overallWins}` \n`•`Losses - `{overallLosses}` \n`•`Kills - `{overallKills}` \n`•`WLR - `{overallWlr}` \n`•`KDR - `{overallKd}` \n`•`Goals - `{overallGoals}`"
                        soloStats = f"`•`Best WS - `{soloBestWinstreak}` \n`•`Winstreak - `{soloWinstreak}` \n`•`Wins - `{duelsWins}` \n`•`Losses - `{duelsLosses}` \n `•`Kills - `{sololKills}` \n`•`WLR - `{soloWlr}` \n`•`KDR - `{soloKd}` \n`•`Goals - `{sololGoals}`"
                        doublesStats = f"`•`Best WS - `{doublesBestWinstreak}` \n`•`Winstreak - `{doublesWinstreak}` \n`•`Wins - `{doublesWins}` \n`•`Losses - `{doublesLosses}` \n`•`Kills - `{doublesKills}` \n`•`WLR - `{doublesWlr}` \n`•`KDR - `{doublesKd}` \n`•`Goals - `{doublesGoals}`"
                        threesStats = f"`•`Best WS - `{threesBestWinstreak}` \n`•`Winstreak - `{threesWinstreak}` \n`•`Wins - `{threesWins}` \n`•`Losses - `{threesLosses}` \n`•`Kills - `{threesKills}` \n`•`WLR - `{threesWlr}` \n`•`KDR - `{threesKd}` \n`•`Goals - `{threesGoals}`" 
                        foursStats = f"`•`Best WS - `{foursBestWinstreak}` \n`•`Winstreak - `{foursWinstreak}` \n`•`Wins - `{foursWins}` \n`•`Losses - `{foursLosses}` \n`•`Kills - `{foursKills}` \n`•`WLR - `{foursWlr}` \n`•`KDR - `{foursKd}` \n`•`Goals - `{foursGoals}`" 
                        fourTwoStats = f"`•`Best WS - `{fourTwoBestWinstreak}` \n`•`Winstreak - `{fourTwoWinstreak}` \n`•`Wins - `{fourTwoWins}` \n`•`Losses - `{fourTwoLosses}` \n`•`Kills - `{fourTwoKills}` \n`•`WLR - `{fourTwoWlr}` \n`•`KDR - `{fourTwpKd}` \n`•`Goals - `{fourTwoGoals}`" 
                        fourThreeStats = f"`•`Best WS - `{fourThreeBestwinstreak}` \n`•`Winstreak - `{fourThreeWinstreak}` \n`•`Wins - `{fourThreesWins}` \n`•`Losses - `{fourThreeLosses}` \n`•`Kills - `{fourThreeKills}` \n`•`WLR - `{fourThreeWlr}` \n`•`KDR - `{fourThreeKd}` \n`•`Goals - `{fourThreeGoals}`"
                        ctfStats = f"`•`Best WS - `{ctfBestWinstreak}` \n`•`Winstreak - `{ctfWinstreak}` \n`•`Wins - `{captureWins}` \n`•`Losses - `{captureLosses}` \n`•`Kills - `{ctfKills}` \n`•`WLR - `{ctfWlr}` \n`•`KDR - `{ctfKd}` \n`•`Goals - `{ctfGoals}`"
                     
                        if gamemodeCheck == True: 
                            duelsEmbed = Embed(description=f"**Bridge Stats - Currently Playing:** `{bridgeGame}`", color=title_color)
                        else:
                            duelsEmbed = Embed(description=f"**Bridge Stats**", color=title_color)                   
                        
                        if online == True:
                            duelsEmbed.set_title(title=f"[{rank}] {name} Lvl: {network_level} - Status : :green_circle:")
                        else:
                            if apiOnOff == True:
                                duelsEmbed.set_title(title=f"[{rank}] {name} Lvl: {network_level} - Status: :red_circle:")
                            else:
                                duelsEmbed.set_title(title=f"[{rank}] {name} Lvl: {network_level} - Status: API OFF")

                        duelsEmbed.set_thumbnail(url=fullSkin)
                        duelsEmbed.add_field(name="Overall", value=f"{overallStats}", inline=True)
                        duelsEmbed.add_field(name="1v1", value=f"{soloStats}", inline=True)
                        duelsEmbed.add_field(name="2v2", value=f"{doublesStats}", inline=True)
                        duelsEmbed.add_field(name="3v3", value=f"{threesStats}", inline=True)
                        duelsEmbed.add_field(name="4v4", value=f"{foursStats}", inline=True)
                        duelsEmbed.add_field(name="2v2v2v2", value=f"{fourTwoStats}", inline=True)
                        duelsEmbed.add_field(name="3v3v3v3", value=f"{fourThreeStats}", inline=True)
                        duelsEmbed.add_field(name="CTF", value=f"{ctfStats}", inline=True)
                        duelsEmbed.add_field(name = 'Teams', value = f'`•`Wins - `{total}`' ,inline = True)
                        duelsEmbed.set_author(name=f"{title}  »  {nextRank}")
                        duelsEmbed.set_footer(text="")
                        duelsEmbed.set_footer(text=f'Requested by {ctx.message.author}')
                        await ctx.send(embed=duelsEmbed)
                    else:
                        noStatsEm = discord.Embed(title=f"`{name}` has no Bridge stats!", description="", color=0xff0000)
                        await ctx.send(embed=noStatsEm)
                else:
                    noStatsEm = discord.Embed(title=f"`{name}` has no Bridge stats!", description="", color=0xff0000)
                    await ctx.send(embed=noStatsEm)
            else:
                noStatsEm = discord.Embed(title=f"`{name}` has no Bridge stats!", description="", color=0xff0000)
                await ctx.send(embed=noStatsEm)
    else:
        if ign == "":
            await ctx.send(f"fill in a valid username!")
        else:
            if IsItaPlayer == True:
                nplayerem = discord.Embed(title=f"`{ign}` is not a player", description="", color=0xff0000)
                await ctx.send(embed=nplayerem)
            else:
                await ctx.send('Error')

@client.command(name="bedwarsStats", aliases=["bedwars", "bw"])
async def bedwarsStats(ctx, ign=""):
    IsItaPlayer = False
    uuid = ""
    if ign == "":
        cur.execute(f"SELECT discordId FROM linking WHERE discordId = '{ctx.message.author.id}';")
        userCheck = cur.fetchone()
        if userCheck is not None:
            username = cur.execute(f"SELECT uuid FROM linking WHERE discordId = '{ctx.message.author.id}';")
            username = f"{cur.fetchone()}"
            username = username.split("'")[1]
            uuid = username.split("'")[0]
    if uuid == "":
        if ign != "":
            usercheck = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}')
            if usercheck.status_code == 404:
                IsItaPlayer = True
            else:
                usercheck = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}').json()
                uuid = usercheck['id']
        else:
            pass
    if uuid != "":

        with open('data.json', 'r') as file:
            dataJson = json.load(file)

        hypixelKeyJson = dataJson['hypixelKeyJson']

        uuiddata = requests.get(f'https://sessionserver.mojang.com/session/minecraft/profile/{uuid}').json()
        uuid = uuiddata["id"]
        name = uuiddata["name"]
        bwdata = requests.get(f'https://api.hypixel.net/player?key={hypixelKeyJson}&uuid={uuid}').json()
        rank = rankCheck(bwdata)
        coins = 0
        star = 0
        lootChetst = 0 
        gamesPlayed = 0
        wins = 0
        losses = 0
        finalKills = 0
        finalDeaths = 0
        kills = 0
        deaths = 0
        bedsBroken = 0
        bedsLost = 0
        winstreak = 0

        if "coins" in bwdata["player"]["stats"]["Bedwars"]:
            coins = bwdata["player"]["stats"]["Bedwars"]["coins"]

        if "winstreak" in bwdata["player"]["stats"]["Bedwars"]:
            winstreak = bwdata["player"]["stats"]["Bedwars"]["winstreak"]

        if "achievements" in bwdata["player"]:
            if "bedwars_level" in bwdata["player"]["achievements"]:
                star = bwdata["player"]["achievements"]["bedwars_level"]
        
        if "bedwars_boxes" in bwdata["player"]["stats"]["Bedwars"]:
            lootChetst = bwdata["player"]["stats"]["Bedwars"]["bedwars_boxes"]
        
        if "games_played_bedwars" in bwdata["player"]["stats"]["Bedwars"]:
            gamesPlayed = bwdata["player"]["stats"]["Bedwars"]["games_played_bedwars"]
        
        if "wins_bedwars" in bwdata["player"]["stats"]["Bedwars"]:
            wins = bwdata["player"]["stats"]["Bedwars"]["wins_bedwars"]
        
        if "losses_bedwars" in bwdata["player"]["stats"]["Bedwars"]:
            losses = bwdata["player"]["stats"]["Bedwars"]["losses_bedwars"]
        
        if "final_kills_bedwars" in bwdata["player"]["stats"]["Bedwars"]:
            finalKills = bwdata["player"]["stats"]["Bedwars"]["final_kills_bedwars"]
        
        if "final_deaths_bedwars" in bwdata["player"]["stats"]["Bedwars"]:
            finalDeaths = bwdata["player"]["stats"]["Bedwars"]["final_deaths_bedwars"]
        
        if "kills_bedwars" in bwdata["player"]["stats"]["Bedwars"]:
            kills = bwdata["player"]["stats"]["Bedwars"]["kills_bedwars"]
        
        if "deaths_bedwars" in bwdata["player"]["stats"]["Bedwars"]:
            deaths = bwdata["player"]["stats"]["Bedwars"]["deaths_bedwars"]
        
        if "beds_broken_bedwars" in bwdata["player"]["stats"]["Bedwars"]:
            bedsBroken = bwdata["player"]["stats"]["Bedwars"]["beds_broken_bedwars"]
        
        if "beds_lost_bedwars" in bwdata["player"]["stats"]["Bedwars"]:
            bedsLost = bwdata["player"]["stats"]["Bedwars"]["beds_lost_bedwars"]
        
        if losses != 0:
            wlr = round(wins/losses, 2)
        else:
            wlr = wins
        
        if deaths != 0:
            kdr = round(kills/deaths, 2)
        else:
            kdr = kills

        if finalDeaths != 0:
            fkdr = round(finalKills/finalDeaths, 2)
        else:
            fkdr = finalKills
        if bedsLost != 0:
            bblr = round(bedsBroken/bedsLost, 2)
        else:
            bblr = bedsBroken
        
        coins = "{:,}".format(coins)
        star = "{:,}".format(star)
        lootChetst = "{:,}".format(lootChetst)
        wins = "{:,}".format(wins)
        losses = "{:,}".format(losses)
        kills = "{:,}".format(kills)
        deaths = "{:,}".format(deaths)
        finalKills = "{:,}".format(finalKills)
        finalDeaths = "{:,}".format(finalDeaths)
        bedsBroken = "{:,}".format(bedsBroken)
        bedsLost = "{:,}".format(bedsLost)

        fullSkin = (f"https://visage.surgeplay.com/full/{uuid}?y=-30")
        
        overallMessage = f":coin: `{coins}` \n:gift: `{lootChetst}` \n`•`**WS** - `{winstreak}`"
        gameMessage = f"`•`**Wins** - `{wins}` \n`•`**Losses** - `{losses}` \n`•`**WLR** - `{wlr}`"
        pvpMessage = f"`•`**Kills** - `{kills}` \n`•`**Deaths** - `{deaths}` \n`•`**KDR** - `{kdr}`"
        finalMessage = f"`•`**Final Kills** - `{finalKills}` \n`•`**Final Deaths** - `{finalDeaths}` \n`•`**FKDR** - `{fkdr}`"
        bedsMessage = f"`•`**Beds Broken** - `{bedsBroken}` \n`•`**Beds Lost** - `{bedsLost}` \n`•`**BBLR** - `{bblr}` "

        bedwarsEmbed = Embed(description="", color=0xffffff)
        bedwarsEmbed.set_author(name=f"[{rank}] {name} » {star}✰")
        bedwarsEmbed.set_thumbnail(url = fullSkin)
        bedwarsEmbed.set_title(title="Bedwars Stats")
        bedwarsEmbed.add_field(name="Overall", value=f"{overallMessage}", inline=True)
        bedwarsEmbed.add_field(name="Genral Stats", value=f"{gameMessage}", inline=True)
        bedwarsEmbed.add_field(name = '\u200B', value = '\u200B' ,inline = True)
        bedwarsEmbed.add_field(name="PvP", value=f"{pvpMessage}", inline=True)
        bedwarsEmbed.add_field(name="Finals", value=f"{finalMessage}", inline=True)
        bedwarsEmbed.add_field(name = '\u200B', value = '\u200B' ,inline = True)
        bedwarsEmbed.add_field(name="Beds", value=f"{bedsMessage}", inline=True)
        bedwarsEmbed.set_footer(text=f'Requested by {ctx.message.author}') 
        await ctx.send(embed=bedwarsEmbed)
    else:
        if ign == "":
            await ctx.send(f"fill in a valid username!")
        else:
            if IsItaPlayer == True:
                nplayerem = discord.Embed(title=f"`{ign}` is not a player", description="", color=0xff0000)
                await ctx.send(embed=nplayerem)
            else:
                await ctx.send('Error')


@client.command(name="fullSkin", aliases=["skin", "sk"])
async def fullSkin(ctx, ign=""):
    if ign == "":
        await ctx.send("Please fill in a valid username!")
    else:
        usercheck = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}')
        if usercheck.status_code == 404:
            nplayerem = discord.Embed(title=f"`{ign}` is not a player", description="", color=0xff0000)
            await ctx.send(embed=nplayerem)
        else:
            try:
                uuiddata = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}').json()
                uuid = uuiddata["id"]
                fullSkin = (f"https://visage.surgeplay.com/full/{uuid}?y=-30")
                name = uuiddata["name"]
                skinLink = f"[`Skin List`](https://namemc.com/minecraft-skins/profile/{uuid})"
                downloadLink = f"[`Download`](https://crafatar.com/skins/{uuid}?size=160&default=MHF_Steve&overlay)"
                skin = (f"https://crafatar.com/avatars/{uuid}?size=160&default=MHF_Steve&overlay")
                skinEmbed = discord.Embed(title="", description=f"", color=0x070708)
                skinEmbed.add_field(name="Username", value=f"`{name}`", inline=False)
                skinEmbed.add_field(name="See All Skins", value=f"{skinLink}", inline=False)
                skinEmbed.add_field(name="Skin Download", value=f"{downloadLink}", inline=False)
                skinEmbed.set_footer(text=f'Requested by {ctx.message.author}')
                skinEmbed.set_thumbnail(url = f'{skin}')
                skinEmbed.set_image(url = fullSkin)
                await ctx.send(embed=skinEmbed)
            except:
                error = discord.Embed(title=f"ERROR", description=f"", color=0xff0000)
                await ctx.send(embed=error)

@client.command(name="discordCheck", aliases=["dc", "discord"])
async def discordCheck(ctx, ign=""):
    if ign == "":
        await ctx.send("Please enter a valid username!")
    else:
        usercheck = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}')
        if usercheck.status_code == 404:
            nplayerem = discord.Embed(title=f"`{ign}` is not a player", description="", color=0xff0000)
            await ctx.send(embed=nplayerem)
        else:

            with open('data.json', 'r') as file:
                dataJson = json.load(file)

            hypixelKeyJson = dataJson['hypixelKeyJson']

            uuiddata = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}').json()
            uuid = uuiddata["id"]
            name = uuiddata["name"]
            discordData = requests.get(f'https://api.hypixel.net/player?key={hypixelKeyJson}&uuid={uuid}').json()
            try:
                if "socialMedia" in discordData["player"]:
                    if "links" in discordData["player"]["socialMedia"]:
                        if "DISCORD" in discordData["player"]["socialMedia"]["links"]:
                            discordUser = discordData["player"]["socialMedia"]["links"]["DISCORD"]
                            discordEmbed = Embed(description="", color=0x7289DA)
                            skin = (f"https://i.pinimg.com/564x/44/94/3b/44943b589d4545a5a78f29fa560a65e4.jpg")
                            discordEmbed.set_thumbnail(url = f'{skin}')
                            discordEmbed.set_title(title=f"Social Media")
                            discordEmbed.add_field(name=f"Username - {name}", value=f"`•`Discord - `{discordUser}`")
                            discordEmbed.set_footer(text=f'Requested by {ctx.message.author}')
                            await ctx.send(embed=discordEmbed)
                        else:
                            errorEm = discord.Embed(title="Error", description=f"{name} dont have linked there discord to hypixel", color=0xff0000)
                            await ctx.send(embed=errorEm)
                    else:
                        errorEm = discord.Embed(title="Error", description=f"{name} dont have linked there discord to hypixel", color=0xff0000)
                        await ctx.send(embed=errorEm)
                else:
                    errorEm = discord.Embed(title="Error", description=f"{name} dont have linked there discord to hypixel", color=0xff0000)
                    await ctx.send(embed=errorEm)
            except:
                errorEm = discord.Embed(title="Error", description=f"{name} dont have linked there discord to hypixel", color=0xff0000)
                await ctx.send(embed=errorEm)

@client.command(name="overallDuels", aliases=["d", "duels"])
async def overallDuels(ctx, ign=""):
    IsItaPlayer = False
    uuid = ""

    if ign == "":
        cur.execute(f"SELECT discordId FROM linking WHERE discordId = '{ctx.message.author.id}';")
        userCheck = cur.fetchone()
        if userCheck is not None:
            username = cur.execute(f"SELECT uuid FROM linking WHERE discordId = '{ctx.message.author.id}';")
            username = f"{cur.fetchone()}"
            username = username.split("'")[1]
            uuid = username.split("'")[0]

    if uuid == "":
        if ign != "":
            usercheck = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}')
            if usercheck.status_code == 404:
                IsItaPlayer = True
            else:
                usercheck = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}').json()
                uuid = usercheck['id']
        else:
            pass
        
    if uuid != "":
        
        with open('data.json', 'r') as file:
            dataJson = json.load(file)

        hypixelKeyJson = dataJson['hypixelKeyJson']

        userCheck = requests.get(f'https://sessionserver.mojang.com/session/minecraft/profile/{uuid}').json()
        name = userCheck["name"]
        playerCheck = requests.get(f'https://api.hypixel.net/player?key={hypixelKeyJson}&uuid={uuid}')
        if playerCheck.status_code != 200:
            await ctx.send(f'Unable to fetch the stats of `{name}`')
        else:
            userData = requests.get(f'https://sessionserver.mojang.com/session/minecraft/profile/{uuid}').json()
            uuid = userData["id"]
            name = userData["name"]
            statsData = requests.get(f'https://api.hypixel.net/player?key={hypixelKeyJson}&uuid={uuid}').json()
            try:
                statsData["player"]["stats"]["Duels"]
            except:
                await ctx.send(f"`{name}` has no Duels stats")
            wins = 0
            losses = 0
            kills = 0
            deaths = 0
            chest = 0
            coins = 0
            ping = 300
            winstreak = 0
            bestWS = 0
            
            if "wins" in statsData["player"]["stats"]["Duels"]:
                wins = statsData["player"]["stats"]["Duels"]["wins"]
            if "wins" in statsData["player"]["stats"]["Duels"]:
                overallDevision = overallDuelsRankCheck(wins)
            if "losses" in statsData["player"]["stats"]["Duels"]:
                losses = statsData["player"]["stats"]["Duels"]["losses"]
            if "kills" in statsData["player"]["stats"]["Duels"]:
                kills = statsData["player"]["stats"]["Duels"]["kills"]
            if "deaths" in statsData["player"]["stats"]["Duels"]:
                deaths = statsData["player"]["stats"]["Duels"]["deaths"]
            if "current_winstreak" in statsData["player"]["stats"]["Duels"]:
                winstreak = statsData["player"]["stats"]["Duels"]["current_winstreak"]
            if "best_overall_winstreak" in statsData["player"]["stats"]["Duels"]:
                bestWS = statsData["player"]["stats"]["Duels"]["best_overall_winstreak"]
            if "duels_chests" in statsData["player"]["stats"]["Duels"]:
                chest = statsData["player"]["stats"]["Duels"]["duels_chests"]
            if "pingPreference" in statsData["player"]["stats"]["Duels"]:
                ping = statsData["player"]["stats"]["Duels"]["pingPreference"]
            if "coins" in statsData["player"]["stats"]["Duels"]:
                coins = statsData["player"]["stats"]["Duels"]["coins"]
            
            if losses != 0:
                overallWlr = round(wins/losses, 2)
            else:
                overallWlr = wins
            if deaths != 0:
                kdr = round(kills/deaths, 2)
            else:
                kdr = "{:,}".format(kills)
            
            playerRank = rankCheck(statsData)
            embedColor = overallTitleColor(wins)
                                
            wins = "{:,}".format(wins)
            losses = "{:,}".format(losses)
            kills = "{:,}".format(kills)
            deaths = "{:,}".format(deaths)
            coins = "{:,}".format(coins)
            bestWS = "{:,}".format(bestWS)
            winstreak = "{:,}".format(winstreak)

            fullSkin = (f"https://visage.surgeplay.com/full/{uuid}?y=-30")

            mainMessage = f"`•`**Coins** - `{coins}` \n`•`**Ping range** - `{ping}` \n`•`**Loot chetst** - `{chest}`"
            statsMessage = f"`•`**Wins** - `{wins}` \n`•`**Losses** - `{losses}` \n`•`**WLR** - `{overallWlr}`"
            winstreakMessage = f"`•`**Best WS** - `{bestWS}` \n`•`**Winstreak** - `{winstreak}`"
            combatMessage = f"`•`**Kills** - `{kills}` \n`•`**Deaths** - `{deaths}` \n`•`**KDR** - `{kdr}`"
            
            duelsEmbed = Embed(description="", color=embedColor)
            duelsEmbed.set_author(name=f"[{playerRank}] {name} » {overallDevision}")
            duelsEmbed.set_title(title="Duels Stats")
            duelsEmbed.set_thumbnail(url = f'{fullSkin}')
            duelsEmbed.add_field(name="Main", value=f"{mainMessage}", inline=True)
            duelsEmbed.add_field(name="Game Stats", value=f"{statsMessage}", inline=True)
            duelsEmbed.add_field(name = '\u200B', value = '\u200B' ,inline = True)
            duelsEmbed.add_field(name="Combat", value=f"{combatMessage}", inline=True)                   
            duelsEmbed.add_field(name="Winstreak", value=f"{winstreakMessage}", inline=True)
            duelsEmbed.add_field(name = '\u200B', value = '\u200B' ,inline = True)
            duelsEmbed.set_footer(text=f'Requested by {ctx.message.author}') 
            #duelsEmbed.add_field(name="Test5", value="Test", inline=True)
            #duelsEmbed.add_field(name="Test6", value="Test", inline=True)
            await ctx.send(embed=duelsEmbed)
    else:
        if ign == "":
            await ctx.send(f"fill in a valid username!")
        else:
            if IsItaPlayer == True:
                nplayerem = discord.Embed(title=f"`{ign}` is not a player", description="", color=0xff0000)
                await ctx.send(embed=nplayerem)
            else:
                await ctx.send('Error')

#=========================================================================================================#

@client.command()
async def link(ctx, ign=""):
    cur.execute(f"SELECT discordId FROM linking WHERE discordId = '{ctx.message.author.id}';")
    check = cur.fetchone()
    if check is not None:
        cur.execute(f"SELECT uuid FROM linking WHERE discordId = '{ctx.message.author.id}';")
        username = f"{cur.fetchone()}"
        username = username.split("'")[1]
        uuid = username.split("'")[0]
        userCheck = requests.get(f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid}")
        if userCheck.status_code == 404:
            nplayerem = discord.Embed(title=f"You are linked with an unknown ign", description="", color=0xff0000)
            await ctx.send(embed=nplayerem)
        else:
            userData= requests.get(f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid}").json()
            name = userData['name']
            await ctx.send(f"Your already linked to `{name}` \nUUID = `{uuid}`")
    else:
        if ign == "":
            await ctx.send("Fill in a valid username!")
        else:
            playerCheck = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{ign}")
            if playerCheck.status_code == 404:
                nplayerem = discord.Embed(title=f"`{ign}` is not a player", description="", color=0xff0000)
                await ctx.send(embed=nplayerem)
            else:

                with open('data.json', 'r') as file:
                    dataJson = json.load(file)

                hypixelKeyJson = dataJson['hypixelKeyJson']

                playerData = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{ign}").json()
                uuid = playerData["id"]
                name = playerData["name"]
                discordId = ctx.message.author.id
                playerInfo = requests.get(f"https://api.hypixel.net/player?key={hypixelKeyJson}&uuid={uuid}").json()
                if "socialMedia" in playerInfo["player"]:
                    if "links" in playerInfo["player"]["socialMedia"]:
                        if "DISCORD" in playerInfo["player"]["socialMedia"]["links"]:
                            discordTag = f'{playerInfo["player"]["socialMedia"]["links"]["DISCORD"]}'
                            ctxAuthor = f'{ctx.message.author}'
                            if ctxAuthor.lower() == discordTag.lower():
                                try:
                                    cur.execute(f"INSERT INTO linking (discordID, uuid) VALUES ('{discordId}', '{uuid}');")
                                    await ctx.send(f"You linked `{ctx.message.author}` to `{name}`")
                                except:
                                    await ctx.send(f"Your already linked")
                            else:
                                await ctx.send(f"`{name}` is linked to `{discordTag}` not `{ctx.message.author}`")
                        else:
                            await ctx.send(f"`{name}` hans't linked their discord")
                    else:
                        await ctx.send(f"`{name}` hans't linked their discord")
                else:
                    await ctx.send(f"`{name}` hans't linked their discord")
                
                con.commit()

@client.command()
async def unlink(ctx):
    cur.execute(f"SELECT discordId FROM linking WHERE discordId = '{ctx.message.author.id}';")
    checkUser = cur.fetchone()
    if checkUser is not None:
        cur.execute(f"DELETE FROM linking WHERE discordId = '{ctx.message.author.id}';")
        await ctx.send(f"Succesfully unlinked")
    else:
        await ctx.send(f"You didnt linked your account")
    con.commit()

@client.command()
async def ign(ctx, ping: discord.Member = None):
    try:
        if ping == None:
            await ctx.send(f"$ign [@discord member]")
        else:
            userId = ping.id
            cur.execute(f"SELECT discordId FROM linking WhERE discordId = '{userId}';")
            checkUser = cur.fetchone()
            if checkUser is not None:
                cur.execute(f"SELECT UUID FROM linking WHERE discordId = '{userId}';")
                username = f"{cur.fetchone()}"
                username = username.split("'")[1]
                uuid = username.split("'")[0]
                userCheck = requests.get(f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid}").json()
                name = userCheck["name"]
                await ctx.send(f"`{ping}` is linked to `{name}`")
            else:
                await ctx.send(f"`{ping}` isnt linked")
    except:
        await ctx.send(f"Error")

#=========================================================================================================#

client.run('TOKEN')
con.close()

#=========================================================================================================#
