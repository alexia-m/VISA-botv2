import discord
import asyncio
from discord.ext import commands
import logging
from pathlib import Path
import platform
import json
################################################SETUP STUFF############################################################################


intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)

logging.basicConfig(level=logging.INFO)

bot.load_extension("about")
bot.load_extension("server")
bot.load_extension("docs")

############################################## BOT COMMANDS AND THE BODY SHIT ####################################################
@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}")
    await bot.change_presence(activity=discord.Game(name=f"with the lives of mortals."))

@bot.event
async def on_member_join(member):
    channeljoin = bot.get_channel()
    embed=discord.Embed(title=f"Welcome {member.name}", description=f"Thanks for joining {member.guild.name}!") # F-Strings!
    embed.set_thumbnail(url=member.avatar_url) # Set the embed's thumbnail to the member's avatar image!
    role = discord.utils.get(member.guild.roles, name="Applicant")
    await member.add_roles(role)
    await member.send('Welcome to Vulture International Security. Please @ a member of recruiting, admin or a director to arrange an induction/interview. If you have any questions please feel free to ask them in #new-recruits. The interview is only a formality to prevent spammers and trolls. ')
    await channeljoin.send(embed=embed)

@bot.event
async def on_member_remove(member):
    channelleave = bot.get_channel()
    embed=discord.Embed(title=f"{member.name} has left the server.", description=f"Fuck them, I guess.")
    await channelleave.send(embed=embed)

@bot.slash_command(name="stats", guild_ids=[])
async def stats(ctx):
    """
    A usefull command that displays bot statistics.
    """
    
    embed = discord.Embed(title=f'{bot.user.name} Stats', colour=ctx.author.colour)

    embed.add_field(name='Python Version:', value='3.2')
    embed.add_field(name='Discord.Py Version', value='2.0')
    embed.add_field(name='Bot Developers:', value="AlexaM#3020")

    embed.set_footer(text=f"{bot.user.name}")
    embed.set_author(name=bot.user.name)

    await ctx.respond(embed=embed)

@bot.slash_command(name="modpack", guild_ids=[])
async def Modpack(ctx):
    """
    Displays the current modpack.
    """
   
    embed = discord.Embed(title=f'{bot.user.name} Modpack', colour=ctx.author.colour)
    embed.add_field(name='The current modpack is:', value="VIS MOD")

    await ctx.respond(embed=embed)



################################################### RUNS THE BOT ####################################################################
bot.run("ODYyODU2OTczNjk4MjAzNzA4.YOecLQ.zTU-Pek7huuTBGWetakYzGyQbP4")