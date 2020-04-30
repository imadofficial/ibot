
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

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'''[BOT:COG]              Help.py loaded''')

    @commands.command(aliases=["HELP","Help","h"])
    async def help(self, ctx, cog=None):
        if cog is None:
            embed = discord.Embed(title="Please specify what category you want to use!")
            embed.add_field(name="Public Commands", value="``help public``",inline=False)
            embed.add_field(name="Moderation commands", value="``help mod`` or ``help moderation``",inline=False)
            embed.add_field(name="COVID19 Commands", value="``help COVID19``",inline=False)
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        elif 'public' in cog:
            embed = discord.Embed(title="Command help")

            embed.add_field(name="Commands available to use!", value="""``uptime``
``botver``
``iso``
``serverinfo``
``invitelink``
``AMD``
``discord``""", inline=True)

            embed.add_field(name="Encryption (BETA)", value="""``encode``
``decode``""", inline=True)

            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
        elif 'moderation' in cog:
            embed = discord.Embed(title="Command help")
            embed.add_field(name="Commands available to use!", value="""``kick``
``ban``
``warn``
``unban``
``changeprefix``
``clear``
``userinfo``""", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
        elif 'mod' in cog:
            embed = discord.Embed(title="Command help")
            embed.add_field(name="Commands available to use!", value="""``kick``
``ban``
``warn``
``unban``
``changeprefix``
``clear``
``userinfo``""", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
        elif 'COVID19' in cog:
            embed = discord.Embed(title="COVID19 commands")
            embed.add_field(name="Commands available to use!", value="``stat``", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error")
            embed.add_field(name="Invalid command passed", value="The command you just invoked does not exist or has been disabled, please try again.", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))