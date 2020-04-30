
import discord
from discord.ext import commands
from datetime import datetime
import datetime
import time
import os
import csv
import random
import inspect
import asyncio

class iso(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'''[BOT:COG]              ISO.py loaded''')

    @commands.command(aliases=["ISO",".iso"])
    async def iso(self, ctx, iso=None):
        if iso is None:
            embed = discord.Embed(title="The available ISO's")
            embed.add_field(name="Windows 10", value="``1511``\n``1607``\n``technical_preview``",inline=True)
            embed.add_field(name="Windows 7", value="``7``\n``thin_pc``",inline=True)
            embed.add_field(name="Windows 8", value="``8.0``\n``8.1``",inline=True)
            embed.add_field(name="Windows XP", value="``XP``",inline=True)
            embed.add_field(name="Windows Vista", value="``vista``",inline=True)
            embed.add_field(name="ImadOS", value="``aero10``",inline=True)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        elif 'aero10' in iso:
            embed = discord.Embed(title="ImadOS Aero10 RS5 Edition")
            embed.add_field(name="64-Bit (English)", value="Soon",inline=True)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/17/PNG/256/application_software_win_windows_windows8_1867.png')
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        elif '1511' in iso:
            embed = discord.Embed(title="Windows 10 1511 (TH2, NU)")
            embed.add_field(name="64-Bit (English)", value="http://bit.ly/ibot-iso-1511-x64",inline=True)
            embed.add_field(name="32-Bit (English)", value="http://bit.ly/ibot-iso-1511-x32",inline=True)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/17/PNG/256/application_software_win_windows_windows8_1867.png')
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        elif '1607' in iso:
            embed = discord.Embed(title="Windows 10 1607 (TH2, NU)")
            embed.add_field(name="64-Bit (English)", value="http://bit.ly/ibot-iso-win10_1607-x64",inline=True)
            embed.add_field(name="32-Bit (English)", value="http://bit.ly/ibot-iso-win10_1607-x32",inline=True)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/17/PNG/256/application_software_win_windows_windows8_1867.png')
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        elif 'technical_preview' in iso:
            embed = discord.Embed(title="Windows 10 Technical Preview ISO's", colour=0x52D0FF)
            embed.add_field(name="(Build 10074) 64-Bit (English)", value="http://bit.ly/ibot-iso-10074-x64",inline=False)
            embed.add_field(name="(Build 10074) 32-Bit (English)", value="http://bit.ly/ibot-iso-10074-x32",inline=False)
            embed.add_field(name="(Build 9926) 64-Bit (English)", value="http://bit.ly/ibot-iso-9926-x64",inline=False)
            embed.add_field(name="(Build 9926) 32-Bit (English)", value="http://bit.ly/ibot-iso-9926-x32",inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/17/PNG/256/application_software_win_windows_windows8_1867.png')
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        elif '7' in iso:
            embed = discord.Embed(title="Windows 7 with SP1")
            embed.add_field(name="64-Bit - Ultimate (English)", value="http://bit.ly/ibot-iso-win7-Ultimate-x64",inline=True)
            embed.add_field(name="32-Bit - Ultimate (English)", value="http://bit.ly/ibot-iso-win7-Ultimate-x32",inline=True)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/679756497504174085/e0157ce22ac4ae2c2fc2831ca8ff2261.webp?size=1024')
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        elif 'thin_pc' in iso:
            embed = discord.Embed(title="Windows Thin PC")
            embed.add_field(name="32-Bit - Enterprise (English)", value="https://the-eye.eu/public/MSDN/Windows%20Thin%20PC/en_windows_thin_pc_x86_697681.iso",inline=True)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/679756497504174085/e0157ce22ac4ae2c2fc2831ca8ff2261.webp?size=1024')
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        elif '8.0' in iso:
            embed = discord.Embed(title="Windows 8", colour=0x52D0FF)
            embed.add_field(name="64-Bit (English)", value="http://bit.ly/ibot-iso-win8-x64",inline=True)
            embed.add_field(name="32-Bit (English)", value="http://bit.ly/ibot-iso-win8-x32",inline=True)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/17/PNG/256/application_software_win_windows_windows8_1867.png')
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        elif '8.1' in iso:
            embed = discord.Embed(title="Windows 8.1", colour=0x52D0FF)
            embed.add_field(name="64-Bit (English)", value="http://bit.ly/ibot-iso-win8_1-x64",inline=True)
            embed.add_field(name="32-Bit (English)", value="http://bit.ly/ibot-iso-win8_1-x32",inline=True)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/17/PNG/256/application_software_win_windows_windows8_1867.png')
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        elif 'XP' in iso:
            embed = discord.Embed(title="Windows XP")
            embed.add_field(name="64-Bit (English)", value="http://bit.ly/ibot-iso-winXP-Pro-x64",inline=True)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url='http://www.pngmart.com/files/3/Windows-XP-PNG-Photos.png')
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        elif 'vista' in iso:
            embed = discord.Embed(title="Windows Vista")
            embed.add_field(name="64-Bit (English)", value="http://bit.ly/ibot-iso-winXP-Pro-x64",inline=True)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url='http://www.pngmart.com/files/3/Windows-XP-PNG-Photos.png')
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error! 0xc0001")
            embed.add_field(name="Command not found", value="The command you invoked does not exist, \nplease try again", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
    
    @commands.command()
    async def youtube(self, ctx):
        embed = discord.Embed(title="My YouTube channel", url='https://www.youtube.com/channel/UCYWIvAxrXIGXLWyA5V0vZSw')
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(iso(bot))