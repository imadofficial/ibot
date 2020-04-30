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

start_time = time.time()
version = 0.12
class isoeadminCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'''[BOT:COG]              isoeadmin.py loaded''')
    
    @commands.group()
    @commands.has_permissions(manage_messages=True)
    async def isoeadmin(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('The command you just typed in does not exist! Please type `/isoeadmin help` for more information.')

    @isoeadmin.command()
    @commands.has_permissions(manage_messages=True)
    async def help(self, ctx):
        author = ctx.message.author.id
        embed = discord.Embed(Title=f"Hi, {ctx.message.author.name}!", colour=0x008cff)
        embed.add_field(name="/addleaderboard", value="Allowing a person to participate into the leaderboard")
        embed.add_field(name="/export", value="Exporting a database")
        embed.add_field(name="/removeleaderboard", value="Disallow someone to perticipate in the leaderboard. (May need some extra config by Imad)")
        embed.add_field(name="/updateleaderboard", value="Update someone's status in the leaderboard.")
        embed.add_field(name="/removerequest", value="Remove a certain request")
        embed.add_field(name="/assignrole", value="Assign a role to yourself")
        await self.bot.get_user(author).send(embed=embed)
        await ctx.send("Check your DMS!")
    
    @isoeadmin.command()
    @commands.has_permissions(manage_messages=True)
    async def export(self, ctx, file=None):
        if file is None:    
            embed = discord.Embed(colour=48000)
            embed.add_field(name='Files available for export:', value=f'Requests')
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        elif 'requests' in file:
            author = ctx.message.author.id
            await ctx.send("Please wait...")
            await self.bot.get_user(author).send(file=discord.File(fp="requests.json", filename="Requested Programs.json"))
            await ctx.send("Check your DMs")
        else:
            await ctx.send("The file you just typed, doesn't exist. Please try again later.")
    
    @isoeadmin.command()
    @commands.has_permissions(manage_messages=True)
    async def addleaderboard(self, ctx, id: int):

        with open("isoe.json", "r") as f:
            isoe = json.load(f)

            isoe[f"{id}"] = "Not Revealed"

            with open("isoe.json", "w") as f:
                json.dump(isoe, f, indent=4)
        
        embed = discord.Embed(colour=48000)
        embed.add_field(name='Operation successful', value=f'<@{id}> has been added into the leaderboard. The value has been set to `Not Revealed`')
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)

    @isoeadmin.command()
    @commands.has_permissions(manage_messages=True)
    async def removeleaderboard(self, ctx, id: int):

        with open("isoe.json", "r") as f:
            isoe = json.load(f)

            del isoe[f"{id}"]

            with open("isoe.json", "w") as f:
                json.dump(isoe, f, indent=4)
        
        embed = discord.Embed(colour=48000)
        embed.add_field(name='Operation successful', value=f'<@{id}> has been removed from the leaderboard.')
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)
    
    @isoeadmin.command()
    @commands.has_permissions(manage_messages=True)
    async def removerequest(self, ctx, *, software):

        with open("requests.json", "r") as f:
            isoe = json.load(f)

            del isoe[f"{software}" : 0]

            with open("isoe.json", "w") as f:
                json.dump(isoe, f, indent=4)
        
        embed = discord.Embed(colour=48000)
        embed.add_field(name='Operation successful', value=f'`{software}` has been successfully deleted.')
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)
    
    @isoeadmin.command()
    @commands.has_permissions(manage_messages=True)
    async def updateleaderboard(self, ctx, id: int, *, value):

        with open("isoe.json", "r") as f:
            isoe = json.load(f)

            isoe[f"{id}"] = f"{value}"

            with open("isoe.json", "w") as f:
                json.dump(isoe, f, indent=4)
        
        embed = discord.Embed(colour=48000)
        embed.add_field(name='Operation successful', value=f'The value for <@{id}> has been updated to: `{value}`')
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)
    
    @isoeadmin.command()
    @commands.has_permissions(manage_messages=True)
    async def createrole(self, ctx, *, role):

        guild = ctx.guild
        await guild.create_role(name=f"{role}")
        
        embed = discord.Embed(colour=48000)
        embed.add_field(name='Operation successful', value=f'The role has been created called: {role}')
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)
    
    @isoeadmin.command()
    @commands.has_permissions(manage_messages=True)
    async def assignrole(self, ctx, id: int, *, role):

        role = discord.utils.get(ctx.guild.roles, name=f"{role}")
        user = ctx.message.author
        await user.add_roles(role)
        
        embed = discord.Embed(colour=48000)
        embed.add_field(name='Operation successful', value=f'The role ``{role}`` has been assigned.')
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)
    
    @isoeadmin.command()
    @commands.has_permissions(manage_messages=True)
    async def removerole(self, ctx, *, role):

        role = discord.utils.get(ctx.guild.roles, name=f"{role}")
        user = ctx.message.author
        await user.remove_roles(user, role)
        
        embed = discord.Embed(colour=48000)
        embed.add_field(name='Operation successful', value=f'The role has been created called: {role}')
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(isoeadminCommands(bot))