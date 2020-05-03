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
        print(f'''[BOT:COG]              Databases.py loaded''')
    
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
    async def bsoderror(self, ctx, *, error):
        try:
            with open("windowserrorcodes.json", "r") as f:
                code = json.load(f)

                identifier = code[f"{error}"]["identifier"]
                error_name = code[f"{error}"]["error_name"]
                meaning = code[f"{error}"]["meaning"]
                troubleshoot = code[f"{error}"]["Troubleshoot"]
                            
            embed = discord.Embed()
            embed.set_author(name=f'{error} -> Basic Information', icon_url=self.bot.user.avatar_url)
            embed.add_field(name="Error code:", value=f"`{error_name}`", inline=False)
            embed.add_field(name="Identified as", value=f"`{identifier}`", inline=False)
            embed.add_field(name="Meaning", value=f"{meaning}", inline=False)
            embed.add_field(name="Troubleshooting Options", value=f"{troubleshoot}", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        except KeyError:
            await ctx.send(f"Command raised an exception: KeyError: {error}")
        
    @commands.command()
    async def iso(self, ctx, *, image):
            try:
                with open("iso.json", "r") as f:
                    code = json.load(f)

                    identifier = code[f"{image}"]["Identifier"]
                    iso = code[f"{image}"]["iso_name"]
                    creator = code[f"{image}"]["Creator"]
                    size64 = code[f"{image}"]["Size64"]
                    size32 = code[f"{image}"]["Size32"]
                    Downloadx64 = code[f"{image}"]["Downloadx64"]
                    Downloadx32 = code[f"{image}"]["Downloadx32"]
                    Included_Editions = code[f"{image}"]["Included Editions"]
                    Logo = code[f"{image}"]["Logo"]
                                
                embed = discord.Embed(color=0x33BEFF)
                embed.set_author(name=f'Your {iso} image is ready for download!', icon_url=self.bot.user.avatar_url)
                embed.add_field(name="ISO Number:", value=f"`{identifier}`", inline=True)
                embed.add_field(name="ISO Name:", value=f"`{iso}`", inline=True)
                embed.add_field(name="Contributor(s)", value=f"{creator}", inline=True)
                embed.add_field(name="ISO Size (x64)", value=f"`{size64}`", inline=True)
                embed.add_field(name="ISO Size (x32)", value=f"`{size32}`", inline=True)
                embed.add_field(name="Included Editions:", value=f"{Included_Editions}", inline=True)
                embed.add_field(name="Download Link (64-Bits):", value=f"{Downloadx64}", inline=False)
                embed.add_field(name="Download Link (64-Bits):", value=f"{Downloadx32}", inline=False)
                embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url=f"{Logo}")
                embed.timestamp = datetime.datetime.now()
                await ctx.send(embed=embed)
            except KeyError:
                await ctx.send(f"`{image}` does not exist! Please type `help iso` to see what ISOs are available.\nMake sure that you have typed: `windows` or `linux`before the version you want.\n**P.S.** Make sure you type in: `windows 10` before typing the version.")

def setup(bot):
    bot.add_cog(cpu(bot))