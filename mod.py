import json, urllib.parse, sys, os
from http.server import BaseHTTPRequestHandler, HTTPServer
from subprocess import call
import subprocess
import time
import discord
import sys
import time
import asyncio
import aiohttp
from asyncio import sleep
from discord.utils import get
from discord.ext import commands, tasks
from datetime import datetime, timedelta, date
import re
import os
import csv

#TIME

import time
import datetime
from datetime import date
from datetime import datetime
import calendar

import database

intents = discord.Intents.default()
intents.members = True

client = discord.Client()
prefixx = input("Prefix: ")
bot = commands.Bot(command_prefix=(prefixx), intents=intents)

bot_token = input("Discord Bot Token: ")

nix_id = 418845658221641730




def get_date():
    now = datetime.now()
    day = now.strftime("%A")

    now = datetime.now().time()
    time = now.strftime("%I:%M %p")

    global timeofcommand
    timeofcommand = day+ ' at ' + time   

@bot.event
async def on_ready():
    global admin
    admin = bot.get_user(nix_id)
    get_date()
    await admin.send(f"Bots have started.\n{timeofcommand}")
    info = subprocess.Popen(['screen', '-ls'], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
    #print(info)
    stdout, stderr = info.communicate()
    print(stdout)
    info = str(stdout)
    result = re.search("b'(.*)'", info)
    info = result.group(1)
    embed=discord.Embed(title="**Hello Nick!**", description="How are you today?\n\nHere are the stats:", color=0xffffff)
    embed.set_author(name="Moderator Bot")
    embed.add_field(name="Output", value=f'```{info}```', inline=False)
    if 'No Sockets found' in info:
        embed.add_field(name="Simplify", value=f'No running bots at the moment', inline=False)
    if 'Mod' in info:
        embed.add_field(name="Simplify", value=f'**Moderation Bot** is running. Duh... 👨‍💻', inline=False)
    if 'AssetBot' in info:
        embed.add_field(name="Simplify", value=f'**Main Asset Bot** is running. 👑', inline=False)
    if 'SupportBot' in info:
        embed.add_field(name="Simplify", value=f'**Support Bot** is running. ⛑', inline=False)
    if 'TradesBot' in info:
        embed.add_field(name="Simplify", value=f'**Trades Bot** is running. 💹', inline=False)
    if 'GitAutoDeploy' in info:
        embed.add_field(name="Simplify", value=f'**GitAutoDeploy Bot** is running. 🚀', inline=False)
    embed.set_footer(text=timeofcommand)
    await admin.send(embed=embed)
    while True:
        index = 0
        os.chdir('AssetBot')
        os.system('git fetch')
        git_info = subprocess.Popen(['git','status'], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
        #print(info)

        up_embed=discord.Embed(title="**Hello Nick!**", description="How are you today?\n\nHere are the stats:", color=0xffffff)
        up_embed.set_author(name="Moderator Bot")
        
        stdout, stderr = git_info.communicate()
        info = str(stdout)
        if 'Your branch is behind' in info:
            if 'git pull' in info:
                #print(stdout)
                os.system('pkill -f main.py')
                os.system('git pull')
                os.system('screen -dmS "AssetBot" python3 main.py')
                up_embed.add_field(name="Updated Bot 👑", value=f'```Asset Main Bot```', inline=False)
                index = 1
                
        else:
            print('no new updates - AEB')
        os.chdir('..')
        
        os.chdir('SupportBot')
        os.system('git fetch')
        git_info = subprocess.Popen(['git','status'], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
        #print(info)
        
        stdout, stderr = git_info.communicate()
        info = str(stdout)
        if 'Your branch is behind' in info:
            if 'git pull' in info:
                #print(stdout)
                os.system('pkill -f sup_main.py')
                os.system('git pull')
                os.system('screen -dmS "SupportBot" python3 sup_main.py')
                up_embed.add_field(name="Updated Bot ⛑", value=f'```Support Bot```', inline=False)
                index = 1
        else:
            print('no new updates - SB')
        os.chdir('..')
        
        os.chdir('TradesBot')
        os.system('git fetch')
        git_info = subprocess.Popen(['git','status'], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
        #print(info)
        
        stdout, stderr = git_info.communicate()
        info = str(stdout)
        if 'Your branch is behind' in info:
            if 'git pull' in info:
                # print(stdout)
                os.system('pkill -f trades.py')
                os.system('git pull')
                os.system('screen -dmS "TradesBot" python3 trades.py')
                up_embed.add_field(name="Updated Bot 💹", value=f'```Trades Bot```', inline=False)
                index = 1
        else:
            print('no new updates - TB')
        os.chdir('..')

        get_date()
        up_embed.set_footer(text=timeofcommand)
        if index == 1:
            await admin.send(embed=up_embed)
        index = 0
        await asyncio.sleep(25)


@bot.command(description="List running")
async def check(ctx):
    if ctx.prefix == "nb!":
        if ctx.author.id == nix_id:
            info = subprocess.Popen(['screen', '-ls'], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT)
            #print(info)
            stdout, stderr = info.communicate()
            print(stdout)
            info = str(stdout)
            result = re.search("b'(.*)'", info)
            info = result.group(1)
            embed=discord.Embed(title="**Hello Nick!**", description="How are you today?\n\nHere are the stats:", color=0xffffff)
            embed.set_author(name="Moderator Bot")
            embed.add_field(name="Output", value=f'```{info}```', inline=False)
            if 'No Sockets found' in info:
                embed.add_field(name="Simplify", value=f'No running bots at the moment', inline=False)
            if 'Mod' in info:
                embed.add_field(name="Simplify", value=f'**Moderation Bot** is running. Duh... 👨‍💻', inline=False)
            if 'AssetBot' in info:
                embed.add_field(name="Simplify", value=f'**Main Asset Bot** is running. 👑', inline=False)
            if 'SupportBot' in info:
                embed.add_field(name="Simplify", value=f'**Support Bot** is running. ⛑', inline=False)
            if 'TradesBot' in info:
                embed.add_field(name="Simplify", value=f'**Trades Bot** is running. 💹', inline=False)
            get_date()
            embed.set_footer(text=timeofcommand)
            await ctx.send(embed=embed)


@bot.command(description="Run")
async def run(ctx, *, bot):
    if ctx.prefix == "nb!":
        if bot is None:
            ctx.send("Hey, enter a bot arg please.")
        else:
            embed=discord.Embed(title="**Hello Nick!**", description="Here are the stats:", color=0x0000ff)
            embed.set_author(name="Moderator Bot")
            get_date()
            embed.set_footer(text=timeofcommand)
            if bot == 'main' or bot == 'm':
                os.system('pkill -f main.py')
                os.chdir('AssetBot')
                os.system('screen -dmS "AssetBot" python3 main.py')
                os.chdir('..')
                embed.add_field(name="Started Bot 👑", value=f'```Asset Main Bot```', inline=False)
            elif bot == 'support' or bot == 'sup' or bot == 's':
                os.system('pkill -f sup_main.py')
                os.chdir('SupportBot')
                os.system('screen -dmS "SupportBot" python3 sup_main.py')
                os.chdir('..')
                embed.add_field(name="Started Bot ⛑", value=f'```Support Bot```', inline=False)
            elif bot == 'trade' or bot == 'trades' or bot == 't':
                os.system('pkill -f trades.py')
                os.chdir('TradesBot')
                os.system('screen -dmS "TradesBot" python3 trades.py')
                os.chdir('..')
                embed.add_field(name="Started Bot 💹", value=f'```Trades Bot```', inline=False)
            await ctx.send(embed=embed)

@bot.command(description="Run")
async def kill(ctx, *, bot):
    if ctx.prefix == "nb!":
        if ctx.author.id == nix_id:
            if bot is None:
                ctx.send("Hey, enter a bot arg please.")
            else:
                embed=discord.Embed(title="**Hello Nick!**", description="Here are the stats:", color=0x0000ff)
                embed.set_author(name="Moderator Bot")
                get_date()
                embed.set_footer(text=timeofcommand)
                if bot == 'main' or bot == 'm':
                    os.system('pkill -f main.py')
                    embed.add_field(name="Killed Bot 👑", value=f'```Asset Main Bot```', inline=False)
                elif bot == 'support' or bot == 'sup' or bot == 's':
                    os.system('pkill -f sup_main.py')
                    embed.add_field(name="Killed Bot ⛑", value=f'```Support Bot```', inline=False)
                elif bot == 'trade' or bot == 'trades' or bot == 't':
                    os.system('pkill -f trades.py')
                    embed.add_field(name="Killed Bot 💹", value=f'```Trades Bot```', inline=False)
                await ctx.send(embed=embed)

bot.run(bot_token)