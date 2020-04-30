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
import sqlite3
import json

def isoeventCommand():
    async def predicate(ctx):
        return ctx.guild.id == 451629088747159572
    return commands.check(predicate)

class isoe(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'''[BOT:COG]              isoe_leaderboard.py loaded''')

    @commands.command()
    @isoeventCommand()
    async def leaderboard(self, ctx, id=None):
        if id is None:

            with open("isoe.json", "r") as f:
                isoe = json.load(f)
            
            Brian = isoe["155885691782299649"]
            Cory = isoe["411688891947679745"]
            Dudefox = isoe["216895311103262723"]
            Extundo = isoe["293076280344182794"]
            Imad = isoe["511212466487689216"]
            Jack = isoe["355808602730135553"]
            Julia = isoe["199660264977596417"]
            Megatobg = isoe["502044962905522177"]
            Mito = isoe["234447549044359168"]
            Pando = isoe["363793635944431617"]
            Pramudita = isoe["266169493745565696"]
            Rikis = isoe["616311961809977344"]
            Sapphire = isoe["615014335525289984"]
            Shaddow = isoe["306647489975418881"]
            Stoyan = isoe["317373436861087749"]
            StrawTech = isoe["499661303670112280"]
            Tam = isoe["246499597902544897"]
            Tonny = isoe["229709025824997377"]
        
            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Leaderboard")
            embed.add_field(name='Leaderboard', value=f"""
1) <@155885691782299649> - {Brian}
2) <@411688891947679745> - {Cory}
3) <@216895311103262723> - {Dudefox}
4) <@293076280344182794> - {Extundo}
5) <@511212466487689216> - {Imad}
6) <@355808602730135553> - {Jack}
7) <@199660264977596417> - {Julia}
8) <@502044962905522177> - {Megatobg}
9) <@234447549044359168> - {Mito}
10) <@363793635944431617> - {Pando}
11) <@266169493745565696> - {Pramudita}
12) <@616311961809977344> - {Rikis}
13) <@615014335525289984> - {Sapphire}
14) <@306647489975418881> - {Shaddow}
15) <@317373436861087749> - {Stoyan}
16) <@499661303670112280> - {StrawTech}
17) <@246499597902544897> - {Tam}
18) <@229709025824997377> - {Tonny}
""", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        
        elif '155885691782299649' in id:

            with open("isoe.json", "r") as f:
                isoe = json.load(f)
            
            Brian = isoe["155885691782299649"]

            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Leaderboard")
            embed.add_field(name='Leaderboard', value=f"1) <@155885691782299649> - {Brian}", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        
        elif '411688891947679745' in id:

            with open("isoe.json", "r") as f:
                isoe = json.load(f)

            Cory = isoe["411688891947679745"]

            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Leaderboard")
            embed.add_field(name='Leaderboard', value=f"1) <@411688891947679745> - {Cory}", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        
        elif '216895311103262723' in id:
            
            with open("isoe.json", "r") as f:
                isoe = json.load(f)

            Dudefox = isoe["216895311103262723"]

            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Leaderboard")
            embed.add_field(name='Leaderboard', value=f"1) <@216895311103262723> - {Dudefox}", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)

        elif '293076280344182794' in id:

            with open("isoe.json", "r") as f:
                isoe = json.load(f)

            Extundo = isoe["293076280344182794"]

            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Leaderboard")
            embed.add_field(name='Leaderboard', value=f"1) <@293076280344182794> - {Extundo}", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        
        elif '511212466487689216' in id:

            with open("isoe.json", "r") as f:
                isoe = json.load(f)

            Imad = isoe["511212466487689216"]   
            
            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Leaderboard")
            embed.add_field(name='Leaderboard', value=f"1) <@511212466487689216> - {Imad}", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        
        elif '355808602730135553' in id:

            with open("isoe.json", "r") as f:
                isoe = json.load(f)

            Jack = isoe["355808602730135553"]

            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Leaderboard")
            embed.add_field(name='Leaderboard', value=f"1) <@355808602730135553> - {Jack}", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        
        elif '199660264977596417' in id:

            with open("isoe.json", "r") as f:
                isoe = json.load(f)
            
            Julia = isoe["199660264977596417"]
            
            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Leaderboard")
            embed.add_field(name='Leaderboard', value=f"1) <@199660264977596417> - {Julia}", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        
        elif '502044962905522177' in id:

            with open("isoe.json", "r") as f:
                isoe = json.load(f)
            
            Megatobg = isoe["502044962905522177"]
            
            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Leaderboard")
            embed.add_field(name='Leaderboard', value=f"1) <@502044962905522177> - {Megatobg}", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        
        elif '234447549044359168' in id:

            with open("isoe.json", "r") as f:
                isoe = json.load(f)
            
            Mito = isoe["234447549044359168"]
    
            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Leaderboard")
            embed.add_field(name='Leaderboard', value=f"1) <@234447549044359168> - {Mito}", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        
        elif '363793635944431617' in id:

            with open("isoe.json", "r") as f:
                isoe = json.load(f)
            
            Pando = isoe["363793635944431617"]

            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Leaderboard")
            embed.add_field(name='Leaderboard', value=f"1) <@363793635944431617> - {Pando}", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        
        elif '266169493745565696' in id:

            with open("isoe.json", "r") as f:
                isoe = json.load(f)

            Pramudita = isoe["266169493745565696"]
            
            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Leaderboard")
            embed.add_field(name='Leaderboard', value=f"1) <@266169493745565696> - {Pramudita}", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)

        elif '616311961809977344' in id:

            with open("isoe.json", "r") as f:
                isoe = json.load(f)
            
            Rikis = isoe["616311961809977344"]

            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Leaderboard")
            embed.add_field(name='Leaderboard', value=f"1) <@616311961809977344> - {Rikis}", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        
        elif '615014335525289984' in id:

            with open("isoe.json", "r") as f:
                isoe = json.load(f)

            Sapphire = isoe["615014335525289984"]
            
            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Leaderboard")
            embed.add_field(name='Leaderboard', value=f"1) <@615014335525289984> - {Sapphire}", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        
        elif '306647489975418881' in id:

            with open("isoe.json", "r") as f:
                isoe = json.load(f)

            Shaddow = isoe["306647489975418881"]
            
            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Leaderboard")
            embed.add_field(name='Leaderboard', value=f"1) <@306647489975418881> - {Shaddow}", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        
        elif '317373436861087749' in id:

            with open("isoe.json", "r") as f:
                isoe = json.load(f)

            Stoyan = isoe["317373436861087749"]

            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Leaderboard")
            embed.add_field(name='Leaderboard', value=f"1) <@317373436861087749> - {Stoyan}", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)

        elif '499661303670112280' in id:

            with open("isoe.json", "r") as f:
                isoe = json.load(f)

            StrawTech = isoe["499661303670112280"]
            
            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Leaderboard")
            embed.add_field(name='Leaderboard', value=f"1) <@499661303670112280> - {StrawTech}", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        
        elif '246499597902544897' in id:

            with open("isoe.json", "r") as f:
                isoe = json.load(f)
            
            Tam = isoe["246499597902544897"]

            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Leaderboard")
            embed.add_field(name='Leaderboard', value=f"1) <@246499597902544897> - {Tam}", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        
        elif '229709025824997377' in id:

            with open("isoe.json", "r") as f:
                isoe = json.load(f)
            
            Tonny = isoe["229709025824997377"]

            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Leaderboard")
            embed.add_field(name='Leaderboard', value=f"1) <@229709025824997377> - {Tonny}", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(isoe(bot))