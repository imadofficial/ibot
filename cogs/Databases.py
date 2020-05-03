import json
from datetime import datetime
import datetime
import time
import os
import csv
import random
import inspect
import asyncio
import discord
from discord.ext import commands

reactions = [':one:', ':two:', ':three:']

class cpu(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'''[BOT:COG]              Intelark.py loaded''')
    
    @commands.command(aliases=["ia","Intelark", "INTELARK", "Intel", "IntelArk"])
    async def intelark(self, ctx, *, model):
        try:
            with open("Intelarkdb.json", "r") as f:
                cpu = json.load(f)

                processor_name = cpu[f"{model}"]["name"]
                processor_base_fre = cpu[f"{model}"]["base_frequency"]
                processor_max_fre = cpu[f"{model}"]["max_frequency"]
                cache = cpu[f"{model}"]["cache"]
                max_memorysize = cpu[f"{model}"]["max_memorysize"]
                memory_types = cpu[f"{model}"]["memory_types"]
                instruction_set_extensions = cpu[f"{model}"]["instruction_set_extensions"]
                cores = cpu[f"{model}"]["cores"]
                threads = cpu[f"{model}"]["threads"]
                image_url = cpu[f"{model}"]["image_url"]
                lithography = cpu[f"{model}"]["lithography"]
                graphics = cpu[f"{model}"]["graphics"]
                graphicsbasefre = cpu[f"{model}"]["grahpics_base"]
                graphicsmaxfre = cpu[f"{model}"]["grahpics_maxfre"]
                tdp = cpu[f"{model}"]["tdp"]
                segment = cpu[f"{model}"]["segment"]
                page_url = cpu[f"{model}"]["page_url"]
                launch = cpu[f"{model}"]["launch"]
                            
            embed = discord.Embed()
            embed.set_author(name=f'{processor_name} -> Info', url=f"{page_url}")
            embed.add_field(name="Vertical Segment", value=f"`{segment}`", inline=True)
            embed.add_field(name="Launch Date", value=f"`{launch}`", inline=True)
            embed.add_field(name="Lithography", value=f"``{lithography}`` nm", inline=True)
            embed.add_field(name="Processor Base Frequency", value=f"``{processor_base_fre}`` GHz", inline=True)
            embed.add_field(name="Max Turbo Frequency", value=f"``{processor_max_fre}`` GHz", inline=True)
            embed.add_field(name="Cores", value=f"``{cores} cores``", inline=True)
            embed.add_field(name="Threads", value=f"``{threads} threads``", inline=True)
            embed.add_field(name="Cache", value=f"``{cache} MB``", inline=True)
            embed.add_field(name="Max Memory Size", value=f"``{max_memorysize}``", inline=True)
            embed.add_field(name="TDP", value=f"``{tdp} W``", inline=True)
            embed.add_field(name="Graphics Base Frequency", value=f"``{graphicsbasefre}`` GHz", inline=True)
            embed.add_field(name="Graphics Max Frequency", value=f"``{graphicsmaxfre}`` GHz", inline=True)
            embed.add_field(name="Processor Graphics", value=f"``{graphics}``", inline=False)
            embed.add_field(name="Memory Types", value=f"``{memory_types}``", inline=False)
            embed.add_field(name="Instruction Set Extensions", value=f"``{instruction_set_extensions}``", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url=f"{image_url}")
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        except KeyError:
            await ctx.send(f"Command raised an exception: KeyError: {model}")
    
    @commands.command(aliases=["bsod","BSOD", "SBOD", "sbod", "error", "Error", "ERRER"])
    async def errorcode(self, ctx, *, error):
        try:
            with open("windowserrorcodes.json", "r") as f:
                code = json.load(f)

                identifier = code[f"{error}"]["identifier"]
                error_name = code[f"{error}"]["error_name"]
                meaning = code[f"{error}"]["meaning"]
                troubleshoot = code[f"{error}"]["Troubleshoot"]
                            
            embed = discord.Embed()
            embed.set_author(name=f'{error} -> Basic Information', icon_url=self.bot.user.avatar_url)
            embed.add_field(name="Error name", value=f"`{error_name}`", inline=False)
            embed.add_field(name="Identified as", value=f"`{identifier}`", inline=False)
            embed.add_field(name="Meaning", value=f"{meaning}", inline=False)
            embed.add_field(name="Troubleshooting Options", value=f"{troubleshoot}", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        except KeyError:
            await ctx.send(f"Command raised an exception: KeyError: {error}")

def setup(bot):
    bot.add_cog(cpu(bot))
