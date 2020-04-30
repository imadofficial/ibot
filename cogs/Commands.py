
import discord
from discord.ext import commands
from datetime import datetime
import datetime
import time
import os
import csv
import random
import inspect
import base64
import praw
import qrcode

start_time = time.time()
version = 0.12
build = 44

class Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'''[BOT:COG]              Commands.py loaded''')

    @commands.command()
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=65280)
        embed.add_field(name='Uptime', value=text)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)
    
    @commands.command(name='bot')
    async def bot(self, ctx):
        servers = str(len(self.bot.guilds))
        users = 0
        for guild in self.bot.guilds:
            users += len(guild.members)
        channels = str(len(set(self.bot.get_all_channels())))
        embed = discord.Embed(Description="Some current stats for Spectrum")
        embed.add_field(name="Server count:", value=servers, inline=False)
        embed.add_field(name="Users bot can see:", value=str(users), inline=False)
        embed.add_field(name="Channels bot can see:", value=channels, inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=["invitelink"])
    async def invite(self, ctx):
            embed = discord.Embed(title="Invite link (Click me)", url='https://discordapp.com/oauth2/authorize?client_id=646728960381812736&permissions=8&scope=bot')
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
            
    @commands.command(aliases=["profile", "ui", "pf"])
    async def userinfo(self, ctx, user: discord.Member='own'):
        if user == 'own':
            user = ctx.author
        roles = ""
        for role in user.roles:
            roles += "{}, ".format(role.name)
        embed = discord.Embed(title="{}'s info".format(user.name), description="Here's the user's information", color=65280)
        embed.set_footer(text='This command was invoked by {}'.format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
        embed.set_author(name='Sapphire Bot', icon_url=self.bot.user.avatar_url)
        embed.add_field(name='Username', value=user.name, inline=True)
        embed.add_field(name='User discriminator/tag', value=user.discriminator, inline=True)
        embed.add_field(name='User ID', value=user.id, inline=True)
        embed.add_field(name='User status', value=user.status, inline=True)
        embed.add_field(name='Highest server role', value=user.top_role, inline=True)
        embed.add_field(name="Server join date:", value=user.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Account created at:", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name='User nickname', value=user.nick, inline=True)
        embed.add_field(name='Is the user on mobile?', value=user.is_on_mobile(), inline=True)
        embed.add_field(name='User voice state', value=user.voice, inline=True)
        embed.add_field(name='Is this user a bot?', value=user.bot, inline=True)
        embed.add_field(name='User roles', value=roles, inline=True)
        embed.add_field(name='Is avatar image animated?', value=user.is_avatar_animated(), inline=True)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def serverinfo(self, ctx):
        role_count = len(ctx.guild.roles)
        emoji_count = len(ctx.guild.emojis)
        channel_count = len([x for x in ctx.guild.channels if isinstance(x, discord.channel.TextChannel)])
        embed = discord.Embed()
        embed.add_field(name='Name (ID)', value=f"{ctx.guild.id}")
        embed.add_field(name='Owner', value=ctx.guild.owner, inline=False)
        embed.add_field(name='Members', value=ctx.guild.member_count)
        embed.add_field(name='Text Channels', value=str(channel_count))
        embed.add_field(name='Region', value=ctx.guild.region)
        embed.add_field(name='Verification Level', value=str(ctx.guild.verification_level))
        embed.add_field(name='Highest role', value=ctx.guild.roles[-1])
        embed.add_field(name='Number of roles', value=str(role_count))
        embed.add_field(name='Number of emotes', value=str(emoji_count))
        embed.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def discord(self, ctx):
        await ctx.send("Check it out! https://discord.gg/GRzpwp6")
    
    @commands.command(aliases=["botver","verbot","bver","botinfo", "about"])
    async def botversion(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        uptime = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=65280)
        embed = discord.Embed(title="iBot -> Properties")
        embed.add_field(name="Bot version", value=f"`{version}, build {build}`",inline=True)
        embed.add_field(name="1st Release Date", value="`March 7th 2020`",inline=True)
        embed.add_field(name="Uptime", value=f"`{uptime}`",inline=True)
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)
    
    @commands.command(aliases=["ALERT","Alert"])
    async def alert(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        uptime = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=65280)
        embed = discord.Embed(title="iBot -> Emergency")
        embed.add_field(name="Regarding Intel and AMDark", value=f"In previous releases i've encountered alot of crashed due to IntelArk and AMD Ark. So, i'm temp disabling them.",inline=True)
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def changelog(self, ctx):
        embed = discord.Embed(colour=65280)
        embed = discord.Embed(title=f"iBot -> Changelog v{version}, Build {build}", description='''- Updated AMD, more CPU's has been added!
        - Uptime added in ``/botver``
        - Bot owners are now able to use owner commands in every server.''')
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Commands(bot))
