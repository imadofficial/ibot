import discord
import json
from discord.ext import commands, tasks
import random
import itertools
import urllib.parse, urllib.request, re
import asyncio
import logging
import pandas as pd
import os
import matplotlib.pyplot as plt
import io
from discord import File
import praw
from datetime import datetime
import sqlite3
from sqlite3 import Error
import utils
import csv
from osuapi import OsuApi, ReqConnector
import requests
import pycountry

api = OsuApi("a94bbfff2534aefe24071a9943328c8587025b0b", connector=ReqConnector())
results = api.get_user("ImadOfficial")

with open('Config.csv', 'r') as f:
    ConfigReader = csv.reader(f)
    Config = list(ConfigReader)
footertext = Config[2][1]
disabledcommandslist = Config[4]

def user_is_owner(ctx):
    return str(ctx.author.id) in Config[3][1]

with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

def get_prefix(bot, message):
    try:
        return prefixes[str(message.guild.id)]
    except KeyError:
        return "/"

version = 0.13
build = 44
bot = commands.Bot(command_prefix = get_prefix)
bot.remove_command('help')

@bot.event
async def on_ready():
    activeGuilds = bot.guilds
    totalguilds = len(activeGuilds)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"on {version} b{build} [{totalguilds}] (/)"))
    print(' ')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@.            ...,,,,,***@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@            ....,,,,***@@@ . @@@@@@@@@@@@@@@@@@@@ @@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@            ....,,,,,**@@@ ..          @          ,@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@.            ...,,,,,**,@@ ..                     .@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@,            ...,,,,,***@@@..                       @@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@            ....,,,,***@@@ .                      ,@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@            ....,,,,***@@@ .                      ,@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@.  ,@@@@@@@@@@@@@@, ,***@@ ..                      @@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@         ....@@@@@@@@@..                      ,@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@..           .....,,,*.@@@@                       ,@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@,.            ....,,,***@@ @@@@@@              .@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@*.            ....,,,,**@@       @@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@..           ....,,,,**@@@                         @@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@..           .....,,,**@@@                         @@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@,.            ....,,,,**@@                         @@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@..           ....,,,,**@@@                         @@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@..     *******  ..,,,**@@@                         @@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@* *@@@                         @@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          @@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      @@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print(' ')
    print(f'''[BOT:STARTUP]          iBot#2263 has been logged in! Active in {totalguilds} servers!''')
    print(f'''                       version {version}, build {build}''')

@bot.event
async def on_guild_remove(guild):
    activeGuilds = bot.guilds
    totalguilds = len(activeGuilds)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"on {version} b{build} [{totalguilds}] (/)"))
    print(f'''[UPDATE SERVER COUNT]  {totalguilds} servers''')

    try:
        prefixes.pop(str(guild.id))

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)
    except KeyError:
        pass

@bot.command()
@commands.has_permissions(manage_messages=True)
async def changeprefix(ctx, prefix):

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    
    embed = discord.Embed(colour=48000)
    embed.add_field(name='**Prefix status**', value=f'Your prefix has updated to: "{prefix}"')
    embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
    embed.timestamp = datetime.datetime.now()
    await ctx.send(embed=embed)

@bot.command(name='unban')
@commands.has_permissions(ban_members=True)
async def unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.send(f'<@{id}> has been successfully unbanned')

@bot.event
async def on_guild_join(ctx):
    activeGuilds = bot.guilds
    totalguilds = len(activeGuilds)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"on {version} b{build} [{totalguilds}] (/)"))
    print(f'''[UPDATE SERVER COUNT]  {totalguilds} servers''')
    message = f"""Thank you for adding me! You can use `/help` to find out how to use me.
    Features: `Moderation, Fun, Searching, etc.` With your support, we can keep our bot up to date!"""
    await ctx.owner.send(message)

@bot.command()
@commands.check(user_is_owner)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
@commands.check(user_is_owner)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.load_extension('Stats')

bot.run('PASTE TOKEN HERE!')
