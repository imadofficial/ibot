
import discord
from discord.ext import commands
from datetime import datetime
import datetime
import time
import os
import csv
import random
import inspect
import json

start_time = time.time()

class Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'''[BOT:COG]              Moderation.py loaded''')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member, *, reason=None):
        if reason == None:
            await ctx.send(f"Succesfully kicked {member}")
            await member.kick(reason=reason)
        else:
            await ctx.send(f"Successfully kicked {member} for {reason}")
            await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        if reason == None:
            await ctx.send(f"pleasee specify why {member.mention} should be banned!")
        else:
            memid = member.id
            await member.ban(reason=reason)
            await ctx.send(f"{member.mention} has been banned for: ```{reason}```")
            await self.bot.get_user(memid).send(f"You were banned in **{ctx.guild.name}** by **{ctx.message.author.name}** for ```{reason}```")
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, id: int ,* ,reason=None): 
        #I still need the counter. When it reaches 3, it will ban the user.
        if reason is None:
            await ctx.send(f"Please specify reason why <@{id}> should be warned!")
        else:
            try:
                file[ctx.guild.id][id]["warns"] = file[ctx.guild.id][id] + 1
            except:
                file[ctx.guild.id][id] = {}
                file[ctx.guild.id][id]["warns"] = 1
                with open("warns.json", "r") as f:
                    file = json.load(f)
                    file[ctx.guild.id][id]["warns"] = file[ctx.guild.id][id]["warns"] + 1
                    with open("warns.json", "w") as f:
                        json.dump(file, f, indent=4)
                await ctx.send(f"<@{id}> has been warned for {reason}")
                await self.bot.get_user(id).send(f"You were warned in **{ctx.guild.name}** by **{ctx.message.author.name}** for```{reason}```")

def setup(bot):
    bot.add_cog(Commands(bot))