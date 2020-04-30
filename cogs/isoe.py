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
        print(f'''[BOT:COG]              isoe.py loaded''')

    @commands.command(name='gdez')
    @isoeventCommand()
    async def gdeasy(self, ctx):
        author = ctx.message.author.id
        robtop = [
            'Beat any level from "Stereo Madness" -> "Can\'t let go."',
            'Beat any level from "Stereo Madness" -> "Base After Base."',
            'Beat: "Base After Base".']
        levels = [
            'Complete at least 2 levels from a gauntlet of choice',
            'Make a 30 second level and upload it.']
        quests = [
            'Get at least 1 User Coin in a level']
        embed = discord.Embed(title=f"GD Challenges for {ctx.message.author.name}")
        embed.add_field(name='Challenge 1:', value=f'{random.choice(robtop)}', inline=False)
        embed.add_field(name='Challenge 2:', value=f'{random.choice(levels)}', inline=False)
        embed.add_field(name='Challenge 3:', value=f'{random.choice(levels)}', inline=False)
        embed.add_field(name='Challenge 4:', value=f'{random.choice(quests)}', inline=False)
        embed.add_field(name='Challenge 5:', value=f'{random.choice(robtop)}', inline=False)
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await self.bot.get_user(author).send(embed=embed)
        await ctx.send(f"<@{author}> Check your DM's!")

    @commands.command()
    @isoeventCommand()
    async def isoe(self, ctx):
        embed = discord.Embed(colour=65280)
        embed = discord.Embed(title=f"The ISO Event: Help")
        embed.add_field(name='`/FAQ` (Frequently Asked Questions)', value=f'This allows you to see any question that has been asked so far.', inline=False)
        embed.add_field(name='(GD EVENT)', value=f'Coming soon!', inline=False)
        embed.add_field(name='`/requirements`', value=f'You\'re able to see any requirements too see if you\'re able to participate.', inline=False)
        embed.add_field(name='`/schedule`', value=f'Allows you to see in the schedule what will happen.', inline=False)
        embed.add_field(name='`/software`', value=f'From here, you can download any software you want.', inline=False)
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    @isoeventCommand()
    async def request(self, ctx, *, software):

        with open("requests.json", "r") as f:
            isoe = json.load(f)

            isoe(software)

            with open("requests.json", "w") as f:
                json.dump(isoe, f, indent=4)
        
        embed = discord.Embed(colour=48000)
        embed.add_field(name='Operation successful', value=f'"{software}" been added for checkup!')
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)
    
    @commands.command()
    @isoeventCommand()
    async def check(self, ctx, *, software):

        with open("requests.json", "r") as f:
            isoe = json.load(f)

            isoe[f"{software}"] = 0

            with open("requests.json", "w") as f:
                json.dump(isoe, f, indent=4)
        
        embed = discord.Embed(colour=48000)
        embed.add_field(name='Operation successful', value=f'"{software}" been added for checkup!')
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)
    
    @commands.command()
    @isoeventCommand()
    async def expectation(self, ctx):

            with open("expected.json", "r") as f:
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
            embed = discord.Embed(title=f"The ISO Event: Expected OS", description=":warning: When the ISO Event starts, no one be able to fill in the expectations :warning:")
            embed.add_field(name='What OS will the people think they\'ll get?', value=f"""
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
    
    @commands.command()
    @isoeventCommand()
    async def expect(self, ctx, *, expectation):

        with open("expected.json", "r") as f:
            isoe = json.load(f)

            isoe[f"{ctx.author.id}"] = f"``{expectation}``"

            with open("expected.json", "w") as f:
                json.dump(isoe, f, indent=4)
        
        embed = discord.Embed(colour=48000)
        embed.add_field(name='Operation successful', value=f'You\'re expctation is updated to: {expectation}')
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)

    @commands.command()
    @isoeventCommand()
    async def schedule(self, ctx, page=None):
        if page is None:
            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Schedule")
            embed.add_field(name='Nothing to see here...', value='Please specify what **page** you want to visit! (Up to 1)', inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)

        elif '1' in page:
            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Schedule")
            embed.add_field(name='**May 2nd**', value='We Install our OS, and this became Day 1 of your journey.', inline=False)
            embed.add_field(name='**July 2nd**', value='At this day, you can return to your own OS.', inline=False)
            embed.set_footer(text=f'{ctx.message.author.name} (Page 1/1)', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(colour=65280)
            embed = discord.Embed(title=f"The ISO Event: Schedule")
            embed.add_field(name='Nothing to see here...', value='The page you just typed isn\'t available. Please try a diffrent page.', inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(aliases=["qna", "q&a", "Faq", "FAQ", "QA", "qA", "Qa", "QnA"])
    async def faq(self, ctx, page=None):
        if page is None:
            embed = discord.Embed(title="Q&A help")
            embed.add_field(name="How to use FAQ:", value="``/FAQ {Page you want to visit.} (Up to 8)``",inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)

        elif '1' in page:
            embed = discord.Embed(colour=0x02FFCD)
            embed.add_field(name='Windows ISO Event: Questions & Answers', value=""":one: 
**Q**: What exactly is the main idea of this Event?

**A**: We will be getting a random version of Windows 10 (RTM-1903) and using it for the 2 months. You will not know what OS you are using, as we will have a domain to hide all of the differences. This will make it more exciting and add suspense as you will eventually find out at the end.

:two: 
**Q**: When does it start and when does it end?

**A**: It starts on May 2nd and ends on July 2nd.

:three:
**Q**: What if I accidentally find out my version?

**A**: You will still need to use it for the remainder of the challenge, however you will be allowed to leave the domain if you want since the domain is there for hiding things that could give away the version.""", inline=True)
            embed.set_thumbnail(url="https://cdn.discordapp.com/icons/451629088747159572/da763d64f7b01abd293e0d8ed1855ec9.webp?size=128")
            embed.set_footer(text=f'{ctx.message.author.name} - Page 1/8', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)

        elif '2' in page:
            embed = discord.Embed(colour=0x02FFCD)
            embed.add_field(name='Windows ISO Event: Questions & Answers', value=""":four: 
**Q**: Would if I am scared that I may find out the version?

**A**: Try and be careful what places you go, as we can't get everything. We are trying our best to make it more difficult to find it out by accident. If there is a difference you may spot, let us know so we can try and hide that. If it is impossible to hide, then do not go there or look there.

:five: 
**Q**: If someone finds out their version on accident, will it eliminate that version for everyone?

**A**: No, as we are not saying who is in what group. There is 2 groups but only the admins (Dudefox, Jake) know who is in which one. Since there are a few extra people participating, there could be 3 people running the same OS, so it is not eliminated unless 3 people revealed said OS.""", inline=True)
            embed.set_thumbnail(url="https://cdn.discordapp.com/icons/451629088747159572/da763d64f7b01abd293e0d8ed1855ec9.webp?size=128")
            embed.set_footer(text=f'{ctx.message.author.name} - Page 2/8', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        
        elif '3' in page:
            embed = discord.Embed(colour=0x02FFCD)
            embed.add_field(name='Windows ISO Event: Questions & Answers', value=""":six: 
**Q**: Would if my computer cannot run certain OSes (Such as RTM)?

**A**: Please let us know the lowest possible OS that your PC can run so I can mark that down. We will make sure your ISO is not a version that will not work. The admins will be checking them for the people it needs to be checked for only. I will be making a channel called #about-computer so please answer this question in there for us to prevent conflicts. @Event members (sorry for ping this is important for everyone to answer this one).
""", inline=True)
            embed.set_thumbnail(url="https://cdn.discordapp.com/icons/451629088747159572/da763d64f7b01abd293e0d8ed1855ec9.webp?size=128")
            embed.set_footer(text=f'{ctx.message.author.name} - Page 3/8', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        
        elif '4' in page:
            embed = discord.Embed(colour=0x02FFCD)
            embed.add_field(name='Windows ISO Event: Questions & Answers', value=""":seven: 
**Q**: Do we need to install another OS now?

**A**: If you are planning on completely wiping your computer, then no. If you are making another partition for dual booting, you can now if you want. Be sure to install the lowest Windows 10 version your PC can run. If your PC supports 10 RTM then do that. If you want to install Windows 7/8.1, that works too but 10 is recommended. You can ask me more detail about this question.

:eight: 
**Q**: How will this all be set up?

**A**: Everyone will have Windows 10 Pro (lowest supported version), then one of the trusted admins will connect to your computer to upgrade to the ISO. Then they will put the computer on the IDKU domain to hide all of the differences in Windows 10 versions.
""", inline=True)
            embed.set_thumbnail(url="https://cdn.discordapp.com/icons/451629088747159572/da763d64f7b01abd293e0d8ed1855ec9.webp?size=128")
            embed.set_footer(text=f'{ctx.message.author.name} - Page 4/8', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        
        elif '5' in page:
            embed = discord.Embed(colour=0x02FFCD)
            embed.add_field(name='Windows ISO Event: Questions & Answers', value=""":eight: 
**Q**: How will this all be set up?

**A**: Everyone will have Windows 10 Pro (lowest supported version), then one of the trusted admins will connect to your computer to upgrade to the ISO. Then they will put the computer on the IDKU domain to hide all of the differences in Windows 10 versions. 

:nine: 
**Q**: Can I do this on 2 different computers if I wanted to?

**A**: Yes you can, however we are setting up the main ones first as they are higher priority. Also if spectators see this being fun, we may be able to give them an ISO and help them after the challenge starts and everyone participating is on the OS.

:one: :zero: 
**Q**: Does the OS have to be 64 bit or can it support 32 bit aswell?

**A**: The ISOs will all be 64 bit. If there is a computer you want to do as 32 bit, Please talk to me about it.
""", inline=True)
            embed.set_thumbnail(url="https://cdn.discordapp.com/icons/451629088747159572/da763d64f7b01abd293e0d8ed1855ec9.webp?size=128")
            embed.set_footer(text=f'{ctx.message.author.name} - Page 5/8', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        
        elif '6' in page:
            embed = discord.Embed(colour=0x02FFCD)
            embed.add_field(name='Windows ISO Event: Questions & Answers', value=""":eight: 
**Q**: How will this all be set up?

**A**: Everyone will have Windows 10 Pro (lowest supported version), then one of the trusted admins will connect to your computer to upgrade to the ISO. Then they will put the computer on the IDKU domain to hide all of the differences in Windows 10 versions. 

:nine: 
**Q**: Can I do this on 2 different computers if I wanted to?

**A**: Yes you can, however we are setting up the main ones first as they are higher priority. Also if spectators see this being fun, we may be able to give them an ISO and help them after the challenge starts and everyone participating is on the OS.

:one: :zero: 
**Q**: Does the OS have to be 64 bit or can it support 32 bit aswell?

**A**: The ISOs will all be 64 bit. If there is a computer you want to do as 32 bit, Please talk to me about it.
""", inline=True)
            embed.set_thumbnail(url="https://cdn.discordapp.com/icons/451629088747159572/da763d64f7b01abd293e0d8ed1855ec9.webp?size=128")
            embed.set_footer(text=f'{ctx.message.author.name} - Page 6/8', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)

        elif '7' in page:
            embed = discord.Embed(colour=0x02FFCD)
            embed.add_field(name='Windows ISO Event: Questions & Answers', value=""":one::one:
**Q**: If there is another computer that is not in the event, can I still use it even if it is not on the same OS?

**A**: Yes, as long as you are using the computer with the event OS more.

:one: :two: 
**Q**: Will privacy be an issue or concern?

**A**: No. We are only using the domain for setting the policies to hide everything. We are not going to monitor what you are doing on your computer, and we will not be deleting/going through any of your personal data. If you have more questions on this, DM me.

:one: :three: 
**Q**: If something needs to be changed, but I cannot change it because settings\control panel is blocked, then what do I do?

**A**: DM an admin (Dudefox, Jake), and they will unblock settings/control panel then change the setting for you, then block it again. However if it is a setting that can be done with a policy, we can do that for you on our end.
""", inline=True)
            embed.set_thumbnail(url="https://cdn.discordapp.com/icons/451629088747159572/da763d64f7b01abd293e0d8ed1855ec9.webp?size=128")
            embed.set_footer(text=f'{ctx.message.author.name} - Page 7/8', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)

        elif '8' in page:
            embed = discord.Embed(colour=0x02FFCD)
            embed.add_field(name='Windows ISO Event: Questions & Answers', value="""I know some say they do not need a AV because they do not click bad links and stuff, but here's the thing. Exploits do exist, and some of these OSes have not gotten security updates in at least a few years. Having no AV is pretty risky, especially on like really old builds of Windows 10. I would recommend using one but if not, it is your choice I guess. We were just trying to protect you guys because we care, and we had to disable Windows Defender for reasons and differences between the versions. I will be using an AV for my own security sake. Hope you understand and no need to make an argument about this. Thanks!""", inline=True)
            embed.set_thumbnail(url="https://cdn.discordapp.com/icons/451629088747159572/da763d64f7b01abd293e0d8ed1855ec9.webp?size=128")
            embed.set_footer(text=f'{ctx.message.author.name} - Page 8/8', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        
        elif '9' in page:
            embed = discord.Embed(colour=0x02FFCD)
            embed.add_field(name='Windows ISO Event: Questions & Answers', value="""I am just going to say this:

I know some say they do not need a AV because they do not click bad links and stuff, but here's the thing. Exploits do exist, and some of these OSes have not gotten security updates in at least a few years. Having no AV is pretty risky, especially on like really old builds of Windows 10. I would recommend using one but if not, it is your choice I guess. We were just trying to protect you guys because we care, and we had to disable Windows Defender for reasons and differences between the versions. Hope you understand and no need to make an argument about this. Thanks!

~Julia""", inline=True)
            embed.set_thumbnail(url="https://cdn.discordapp.com/icons/451629088747159572/da763d64f7b01abd293e0d8ed1855ec9.webp?size=128")
            embed.set_footer(text=f'{ctx.message.author.name} - Page 9/8', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(isoe(bot))