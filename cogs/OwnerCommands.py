import discord
from discord.ext import commands
from datetime import datetime
import datetime
import time
import os
import csv
import inspect
import psutil
import sqlite3

with open('Config.csv', 'r') as f:
    ConfigReader = csv.reader(f)
    Config = list(ConfigReader)
footertext = Config[2][1]
disabledcommandslist = Config[4]

def user_is_owner(ctx):
    return str(ctx.author.id) in Config[3][1]

start_time = time.time()
version = 0.12
class OwnerCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'''[BOT:COG]              OwnerCommands.py loaded''')
        
    @commands.group()
    @commands.check(user_is_owner)
    async def owner(self, ctx):
        'Bot Owner Commands'
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid owner command invoked')

    @owner.command()
    @commands.check(user_is_owner)
    async def help(self, ctx):
        author = ctx.message.author.id
        embed = discord.Embed(Title="Bot owner commands", description="Bot owner commands list", colour=0x008cff)
        embed.set_footer(text='Invoked by {}'.format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
        embed.add_field(name="shutdown", value="Shuts down the bot")
        embed.add_field(name="disable", value="Disables a command")
        embed.add_field(name="enablecommand", value="Enable a command")
        embed.add_field(name="vm", value="Make the VM do something")
        embed.add_field(name="run", value="Make the VM run a program.")
        await self.bot.get_user(author).send(embed=embed)
        await ctx.send("Check your DMS!")

    @owner.command()
    @commands.check(user_is_owner)
    async def shutdown(self, ctx):
        await ctx.send("Shutting down...")
        await self.bot.logout()
        await os._exit(0)
    
    @owner.command()
    @commands.check(user_is_owner)
    async def status(self, ctx):
        embed = discord.Embed(title="VM Status:")
        embed.add_field(name='Memory Usage (In %)', value=psutil.virtual_memory()[2], inline=False)
        embed.add_field(name='CPU Usage (In %)', value=psutil.cpu_percent(), inline=False)
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)
    
    @owner.command()
    @commands.check(user_is_owner)
    async def team(self, ctx):
        embed = discord.Embed(title="iBot Owner team!")
        embed.add_field(name='Amount: 4', value="1) Imad (Added: N/A ago)\n2) Dudefox (Added N/A ago)\n3) Julia (Added N/A ago)\n4) Sapphire (Added on Apr 11, 2020)", inline=False)
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)

    @owner.command(aliases=["VM", "Vm", "vM"])
    @commands.check(user_is_owner)
    async def vm(self, ctx, state=None):
        if state is None:
            embed = discord.Embed(title="Make the VM do something")
            embed.add_field(name='Shutdown', value='``shutdown``', inline=False)
            embed.add_field(name='Restart', value='``reboot, restart``', inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        elif 'reboot' in state:
            current_time = time.time()
            difference = int(round(current_time - start_time))
            uptime = str(datetime.timedelta(seconds=difference))
            embed = discord.Embed(colour=0xFF5A5A)
            embed.set_author(name='Preparing the server for reboot...')
            embed.add_field(name='Requested by:', value=f'{ctx.message.author.name}', inline=True)
            embed.add_field(name='Final Uptime:', value=f'{uptime}', inline=True)
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
            os.system('shutdown /r')
            await self.bot.logout()
            await os._exit(0)
        elif 'restart' in state:
            current_time = time.time()
            difference = int(round(current_time - start_time))
            uptime = str(datetime.timedelta(seconds=difference))
            embed = discord.Embed(colour=0xFF5A5A)
            embed.set_author(name='Preparing the server for reboot...')
            embed.add_field(name='Requested by:', value=f'{ctx.message.author.name}', inline=True)
            embed.add_field(name='Final Uptime:', value=f'{uptime}', inline=True)
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
            os.system('shutdown /r')
            await self.bot.logout()
            await os._exit(0)
        elif 'shutdown' in state:
            current_time = time.time()
            difference = int(round(current_time - start_time))
            uptime = str(datetime.timedelta(seconds=difference))
            embed = discord.Embed(colour=0xFF5A5A)
            embed.set_author(name='Preparing the server for shutdown...')
            embed.add_field(name='Requested by:', value=f'{ctx.message.author.name}', inline=True)
            embed.add_field(name='Final Uptime:', value=f'{uptime}', inline=True)
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
            os.system('shutdown /r')
        else:
            embed = discord.Embed(title="Make the VM do something")
            embed.add_field(name='Shutdown', value='``shutdown``', inline=False)
            embed.add_field(name='Restart', value='``reboot, restart``', inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)

    @owner.command()
    @commands.check(user_is_owner)
    async def disable(self, ctx, *, cmd: str='None'):
        cmdstr = cmd
        if cmd == 'None':
            await ctx.send('Missing command argument')
        elif cmd in disabledcommandslist:
            await ctx.send('This command is already disabled')
        elif cmd == 'owner':
            await ctx.send('You can\'t disable the owner command')
        else:
            try:
                cmd = self.bot.get_command(cmd)
                cmd.enabled = False
                await ctx.send("Disabling command '{}'".format(cmd))
                Config[4].append(cmdstr)
                TEMPConfig = open('Conf/Config.csv', 'w', newline='')
                csv_writer = csv.writer(TEMPConfig)
                csv_writer.writerows(Config)
                TEMPConfig.close()
            except AttributeError:
                await ctx.send("Attempt to disable command '{}' failed, possibly due to the command not existing".format(cmdstr))

    @owner.command()
    @commands.check(user_is_owner)
    async def enablecommand(self, ctx, *, cmd: str='None'):
        print(cmd)
        cmdstr = cmd
        if cmd == 'None':
            await ctx.send('Missing command argument')
        elif cmd not in disabledcommandslist:
            print(disabledcommandslist)
            await ctx.send('Command is not disabled')
        else:
            try:
                cmd = self.bot.get_command(cmd)
                cmd.enabled = True
                print(disabledcommandslist)
                Config[4].remove(cmdstr)
                TEMPConfig = open('Config.csv', 'w', newline='')
                csv_writer = csv.writer(TEMPConfig)
                csv_writer.writerows(Config)
                TEMPConfig.close()
                await ctx.send("Enabling command '{}'".format(cmd))
            except AttributeError:
                await ctx.send("Attempt to enable command '{}' failed, possibly due to the command not existing".format(cmdstr))

    @owner.command()
    @commands.check(user_is_owner)
    async def disabledcommands(self, ctx):
        discommand = []
        for cmd in disabledcommandslist:
            if cmd == 'Discommand':
                continue
            else:
                discommand.append(cmd)
        if discommand == []:
            discommand = 'None'
        await ctx.send('Disabled command(s) {}'.format(discommand))
    
    @owner.command()
    @commands.check(user_is_owner)
    async def installpackage(self, ctx, *, pkg):
        os.system(f'py -3 -m pip install -U {pkg}')

    @owner.command()
    @commands.check(user_is_owner)
    async def createrole(self, ctx, *, role):

        perms = discord.Permissions(manage_messages=True, manage_roles=True, manage_guild=True, manage_channels=True, create_instant_invite=True, manage_nicknames=True)
        await ctx.guild.create_role(name=f"{role}", permissions=perms)
        
        embed = discord.Embed(colour=48000)
        embed.add_field(name='Operation successful', value=f'The role has been created called: {role}')
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)
    
    @owner.command()
    @commands.check(user_is_owner)
    async def assignrole(self, ctx, id: int, *, role):

        role = discord.utils.get(ctx.guild.roles, name=f"{role}")
        user = ctx.message.author
        await user.add_roles(role)
        
        embed = discord.Embed(colour=48000)
        embed.add_field(name='Operation successful', value=f'The role ``{role}`` has been assigned.')
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)
    
    @owner.command()
    @commands.check(user_is_owner)
    async def removerole(self, ctx, *, role):

        role = discord.utils.get(ctx.guild.roles, name=f"{role}")
        user = ctx.message.author
        await user.remove_roles(role)
        
        embed = discord.Embed(colour=48000)
        embed.add_field(name='Operation successful', value=f'The role has been created called: {role}')
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(OwnerCommands(bot))